# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:49:25 2020

@author: kirtika jain
"""

from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2

def Edge_Detection():
    global panelA, panelB
    
    path = filedialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)
        if panelA is None or panelB is None:
    		# the first panel will store our original image
            panelA = Label(image=image,font=14)
            panelA.image = image
            panelA.grid(row=1,column=0,columnspan=5,sticky='news')
    		# while the second panel will store the edge map
            panelB = Label(image=edged,font=14)
            panelB.image = edged
            panelB.grid(row=1,column=6,columnspan=5,sticky='news')
    		# otherwise, update the image panels
        else:
    		# update the pannels
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged
         
def Pencil_Sketch():
    global panelA, panelB
    path = filedialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grayImageInv = 255-gray
        grayImageInv = cv2.GaussianBlur(grayImageInv, (21, 21), 0)
        sketch = cv2.divide(gray, 255-grayImageInv, scale=256.0)
        image = Image.fromarray(image)
        sketch = Image.fromarray(sketch)
        image = ImageTk.PhotoImage(image)
        sketch = ImageTk.PhotoImage(sketch)
        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.grid(row=1,column=0,columnspan=5,sticky='news')
			# while the second panel will store the edge map
            panelB = Label(image=sketch)
            panelB.image = sketch
            panelB.grid(row=1,column=6,columnspan=5,sticky='news')
		# otherwise, update the image panels
        else:
			# update the pannels
            panelA.configure(image=image)
            panelB.configure(image=sketch)
            panelA.image = image
            panelB.image = sketch

def Cartooning():
    num_down = 2 # number of downsampling steps
    num_bilateral = 7 # number of bilateral filtering steps
    global panelA, panelB
    path = filedialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        img_color = image
        for _ in range(num_down):
            img_color = cv2.pyrDown(img_color)
        for _ in range(num_bilateral):
            img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)
        for _ in range(num_down):
            img_color = cv2.pyrUp(img_color)
        img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.medianBlur(img_gray, 5)
        img_edge = cv2.adaptiveThreshold(img_blur, 255,
                   cv2.ADAPTIVE_THRESH_MEAN_C,
                   cv2.THRESH_BINARY,
                   blockSize=9,
                   C=2)
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
        cartoon = cv2.bitwise_and(img_color, img_edge)
        image = Image.fromarray(image)
        cartoon = Image.fromarray(cartoon)
        image = ImageTk.PhotoImage(image)
        cartoon = ImageTk.PhotoImage(cartoon)
        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.grid(row=1,column=0,columnspan=5,sticky='news')
			# while the second panel will store the edge map
            panelB = Label(image=cartoon)
            panelB.image = cartoon
            panelB.grid(row=1,column=6,columnspan=5,sticky='news')
		# otherwise, update the image panels
        else:
			# update the pannels
            panelA.configure(image=image)
            panelB.configure(image=cartoon)
            panelA.image = image
            panelB.image = cartoon
            
root = Tk()
root.geometry('1100x800')
root.configure(bg='DodgerBlue4')
root.title('Computer Vision Project')
panelA = None
panelB = None

lbl1 = Label(root, text="WELCOME TO COMPUTER VISION PROJECT!!!", bg="orange red", fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.grid(row=0,columnspan=10,sticky=N,padx=10,pady=10)
l=Label(text="For EDGE DETECTION-",font=8,fg='ghost white',bg='midnight blue',relief=SUNKEN,bd=10).grid(row=2,column=1,sticky=W,padx=10)
l1=Label(text="For CREATING PENCIL SKETCH-",font=8,fg='ghost white',bg='midnight blue',relief=SUNKEN,bd=10).grid(row=3,column=1,sticky=W,padx=10)
l2=Label(text="For CREATING CARTOON IMAGE-",font=8,fg='ghost white',bg='midnight blue',relief=SUNKEN,bd=10).grid(row=6,column=1,sticky=W,padx=10)

img1 = ImageTk. PhotoImage(Image. open("edge.jpg"))
imglabel1 = Label(root, image=img1).grid(row=2,column=7,padx=10,pady=10)
img2 = ImageTk. PhotoImage(Image. open("1.jpg"))
imglabel2 = Label(root, image=img2).grid(row=3,column=7,padx=10,pady=10)
img3 = ImageTk. PhotoImage(Image. open("cartoon.jpg"))
imglabel3 = Label(root, image=img3).grid(row=6,column=7,padx=10,pady=10)

b= Button(root, text="Edge Detection:CHOOSE THE IMAGE",width=35,height=5,relief=RAISED,bd=5,cursor='plus',bg='cyan2',fg='black',activebackground='black',activeforeground='white', command=Edge_Detection)
b.grid(row=2,column=3,sticky=E)
b1= Button(root, text="Photo Sketch:CHOOSE THE IMAGE",width=35,height=5,relief=RAISED,bd=5,cursor='plus',bg='cyan2',fg='black',activebackground='black',activeforeground='white', command=Pencil_Sketch)
b1.grid(row=3,column=3,sticky=E)
b4= Button(root, text="Cartoonifying image:CHOOSE THE IMAGE",width=35,height=5,relief=RAISED,bd=5,cursor='plus',bg='cyan2',fg='black',activebackground='black',activeforeground='white', command=Cartooning)
b4.grid(row=6,column=3,sticky=E)

root.mainloop()