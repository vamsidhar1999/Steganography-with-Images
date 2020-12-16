# Python program implementing Image Steganography

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk, Image

image = Image.open("new.png")
root = Toplevel()
data1 = ''
def genData(data):

    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

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


# Decode the data in the image
def decode(image):

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

        # Main Function


def main():
    root = Toplevel()
    root.title("Decryption")
    root.geometry("1350x650+0+0")
    root.config(bg="blue")

    def browse():
        img = filedialog.askopenfilename(title='Select the image')
        global image
        image = Image.open(img, mode='r')
        image1 = image.resize((500,500), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image1)
        panel = Label(root, image=image1)
        panel.image = image1
        panel = panel.place(relx=0.050, rely=0.050)
    browse = Button(root, text="Browse", padx=16,pady=16,fg='white', bg='green', font=('arial', 10, 'bold'),
                   width=10, height=1, command=browse).place(relx=0.75, rely=0.200)
    def temp():
        global data1
        data1 = decode(image)
        print(data1)
        label0 = Label(root, text="Secret Message - "+data1, font=("araial", 16, "bold"), fg="white", bg="blue",
                       height=3).place(relx=0.50, rely=0.600)

    decrypt = Button(root, text="Decrypt",padx=16,pady=16, fg='white', bg='green', font=('arial', 10, 'bold'),
                    width=10, height=1, command=temp).place(relx=0.75, rely=0.400)


    root.mainloop()
