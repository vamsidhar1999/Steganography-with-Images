from tkinter import *

from PIL import ImageTk


def encrypt():
    root = Toplevel()
    root.title("Encryption")
    root.geometry("1350x650+0+0")
    root.config(bg="grey")
    label = Label(root, text="ENCRYPTION", font=("araial", 32, "bold"), fg="black", bg="grey").grid(row=0, column=0)
    label0 = Label(root, text="PlainText :", font=("araial", 16, "bold"), fg="black", bg="grey", height=3).grid(row=5,
                                                                                                                 column=0)
    label1 = Label(root, text="Key :", font=("araial", 16, "bold"), fg="black", bg="grey", height=3).grid(row=7,
                                                                                                          column=0)
    label2 = Label(root, text="Key1 :", font=("araial", 16, "bold"), fg="black", bg="grey", height=3).grid(row=9,
                                                                                                           column=0)
    label3 = Label(root, text="Key2 :", font=("araial", 16, "bold"), fg="black", bg="grey", height=3).grid(row=11,
                                                                                                           column=0)
    label4 = Label(root, text="CipherText :", font=("araial", 16, "bold"), fg="black", bg="grey", height=3).grid(
        row=13,
        column=0)

    photo2 = ImageTk.PhotoImage(file='decrypt15.png')
    photo = Label(root, image=photo2, bg='grey')
    photo.place(relx=0.414, rely=0.400, anchor=W)

    global etplaintext
    global etkey
    global etkey1
    global etkey2
    global etctext
    plain_text = IntVar()
    key = IntVar()
    key_1 = IntVar()
    key_2 = IntVar()
    Cipher_Text = IntVar()

    etplaintext = Entry(root, font=('arial', 16, 'bold'), bd=5, width=22, justify='left')
    etplaintext.grid(
        row=5, column=1)
    etkey = Entry(root, font=('arial', 16, 'bold'), bd=5, width=22, justify='left')
    etkey.grid(
        row=7, column=1)
    etkey1 = Entry(root, font=('arial', 16, 'bold'), bd=5, width=22, justify='left')
    etkey1.grid(
        row=9, column=1)

    etkey2 = Entry(root, font=('arial', 16, 'bold'), bd=5, width=22, justify='left')
    etkey2.grid(
        row=11, column=1)
    etctext = Entry(root, font=('arial', 16, 'bold'), bd=5, width=22, justify='left')
    etctext.grid(
        row=13, column=1)

    def Exit():
        root.destroy()
    def iReset():
        plain_text.set("")
        key.set("")
        key_1.set("")
        key_2.set("")
        Cipher_Text.set("")



    def encryptresult():
        FIXED_IP = [2, 6, 3, 1, 4, 8, 5, 7]
        FIXED_EP = [4, 1, 2, 3, 2, 3, 4, 1]
        FIXED_IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
        FIXED_P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        FIXED_P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        FIXED_P4 = [2, 4, 3, 1]

        S0 = [[1, 0, 3, 2],
              [3, 2, 1, 0],
              [0, 2, 1, 3],
              [3, 1, 3, 2]]

        S1 = [[0, 1, 2, 3],
              [2, 0, 1, 3],
              [3, 0, 1, 0],
              [2, 1, 0, 3]]

        KEY = etkey.get()
        plain_text = etplaintext.get()

        def permutate(original, fixed_key):
            new = ''
            for i in fixed_key:
                new += original[i - 1]
            # print("new",new)
            return new

        def left_half(bits):
            # print('lefthalf',bits[:len(bits) // 2])
            return bits[:len(bits) // 2]

        def right_half(bits):
            # print('righthalf',bits[len(bits) // 2:])
            return bits[len(bits) // 2:]

        def shift(bits):
            rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
            rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
            return rotated_left_half + rotated_right_half

        def key1():
            return permutate(shift(permutate(KEY, FIXED_P10)), FIXED_P8)

        def key2():
            return permutate(shift(shift(shift(permutate(KEY, FIXED_P10)))), FIXED_P8)

        def xor(bits, key):
            new = ''
            for bit, key_bit in zip(bits, key):
                new += str(((int(bit) + int(key_bit)) % 2))
            return new

        def lookup_in_sbox(bits, sbox):
            row = int(bits[0] + bits[3], 2)
            col = int(bits[1] + bits[2], 2)
            return '{0:02b}'.format(sbox[row][col])

        def f_k(bits, key):
            L = left_half(bits)
            R = right_half(bits)
            bits = permutate(R, FIXED_EP)
            bits = xor(bits, key)
            bits = lookup_in_sbox(left_half(bits), S0) + lookup_in_sbox(right_half(bits), S1)
            bits = permutate(bits, FIXED_P4)
            return xor(bits, L)

        def encryptr():
            bits = permutate(plain_text, FIXED_IP)
            temp = f_k(bits, key1())
            bits = right_half(bits) + temp
            bits = f_k(bits, key2())
            return permutate(bits + temp, FIXED_IP_INVERSE)

        key_1 = key1()
        key_2 = key2()
        etkey1.delete(0, END)
        etkey1.insert(0, key_1)
        etkey2.delete(0, END)
        etkey2.insert(0, key_2)
        Cipher_Text = encryptr()
        # print('Cipher_text',Cipher_Text)
        etctext.delete(0, END)
        etctext.insert(0, Cipher_Text)

    btnexit = Button(root, text="Home", padx=16, pady=16, bd=5, bg='white', fg='black', font=('arial', 10, 'bold'),
                     width=10, height=1, command=Exit).place(relx=0.05, rely=0.680)
    btnreset = Button(root, text="reset", padx=16, pady=16, bd=5, bg='white', fg='black', font=('arial', 10, 'bold'),
                     width=10, height=1, command=iReset).place(relx=0.175, rely=0.680)
    btnEncrpt = Button(root, text="Encrypt", padx=16, pady=16, bd=5, bg='white', fg='black', font=('arial', 10, 'bold'),
                       width=10, height=1, command=encryptresult).place(relx=0.30, rely=0.680)

    root.mainloop()