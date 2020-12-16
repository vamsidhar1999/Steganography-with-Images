from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
import encrypt
import decrypt1

def hide(root):
    root.withdraw()

def show(root):
    root.update()
    root.deiconify()

def home():
    root = Toplevel()
    hide(root)
    root.title("STEGNOGRAPHY")
    root.geometry("1360x650+0+0")
    root.config(bg="blue")
    label = Label(root, text="STEGNOGRAPHY PROJECT", font=("araial", 47, "bold"), fg="white", bg="grey").grid(
        row=0, column=0)

    photo2 = ImageTk.PhotoImage(file='crypto15.png')
    photo = Label(root, image=photo2, bg='grey')
    photo.place(relx=0.05, rely=0.450, anchor=W)



    def Exit():
        root.destroy()


    def ad():
        encrypt.encode()

    def bd():
        decrypt1.main()

    btnexit = Button(root, text="Exit", padx=16, pady=16, bd=5, bg='green', fg='white', font=('arial', 15, 'bold'),
                     width=15, height=1,command=Exit).place(relx=0.75, rely=0.600)
    btnencry = Button(root, text="Encryption", padx=16, pady=16, bd=5, bg='green', fg='white',
                      font=('arial', 15, 'bold'),
                      command=ad, width=15, height=1).place(relx=0.75, rely=0.200)
    btndecry = Button(root, text="Decryption", padx=16, pady=16, bd=5, bg='green', fg='white',
                      font=('arial', 15, 'bold'),
                      command=bd, width=15, height=1).place(relx=0.75, rely=0.400)

    show(root)
    root.mainloop()
home()