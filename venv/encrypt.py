# Python program implementing Image Steganography

# PIL module is used to extract
# pixels of image and modify it
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk, Image


# Convert encoding data into 8-bit binary
# form using ASCII value of characters
image = Image.open("crypto15.PNG", 'r')
data = "lhjknxz"


def hide(root):
    root.withdraw()


def show(root):
    root.update()
    root.deiconify()

def genData(data):
    # list of binary codes
    # of given data
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd


# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                if (pix[j] % 2 != 0):
                    pix[j] -= 1

            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                pix[j] -= 1

        # Eigh^th pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means the
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                pix[-1] -= 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


# Encode data into image
def encode():
    root = Toplevel()

    hide(root)
    root.title("Encryption")
    root.geometry("1350x650+0+0")
    root.config(bg="blue")

    label0 = Label(root, text="Image with extension", font=("araial", 16, "bold"), fg="black",bg="blue", height=3).grid(row=5,column=0)

    def browse():
        img = filedialog.askopenfilename(title='Select the image')
        global image
        image = Image.open(img, mode='r')
        image1 = image.resize((500, 600), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image1)
        panel = Label(root, image=image1)
        panel.image = image1
        panel = panel.place(relx=0.550, rely=0.050)
        return image

    browse = Button(root, text="Browse", bg='green', fg='white', font=('arial', 10, 'bold'),
                    width=10, height=1, command=browse).grid(row=5, column=2)



    label0 = Label(root, text="Secret message", font=("araial", 16, "bold"),bg="blue", fg="black", height=3).grid(row=7,column=0)

    dataen = Entry(root, font=('arial', 16, 'bold'),bd=5, width=22, justify='left')
    dataen.grid(row=7, column=1)


    label0 = Label(root, text="new image name with extension", font=("araial", 16, "bold"), fg="black",bg="blue",
                   height=3).grid(row=11, column=0)
    new_img = Entry(root, font=('arial', 16, 'bold'), bd=5, width=22, justify='left')
    new_img.grid(row=11, column=1)

    def encrypt():
        global data
        data = str(dataen.get())
        if (len(data) == 0):
            raise ValueError('Data is empty')

        global image
        newimg = image.copy()
        encode_enc(newimg, data)
        new_img_name = str(new_img.get())

        newimg.save("C:/Users/VAMSI/Desktop/"+new_img_name, str(new_img_name.split(".")[1].upper()))

    ency = Button(root, text="Encrypt", bg='green', fg='white', font=('arial', 10, 'bold'),
                  width=10, height=1, command=encrypt).grid(row=13, column=2)

    show(root)
    root.mainloop()