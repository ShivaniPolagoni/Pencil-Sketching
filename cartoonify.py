import cv2
from tkinter import * 
import tkinter.font as TkFont
from functools import partial
from tkinter import filedialog

def name_of_file():
    filename = filedialog.askopenfilename(initialdir = "C:",title = "Select a File to Cartoonify",filetypes = (('jpg files','*.jpg'),('Png files','*.png'),('Jpeg files','*.jpeg')))
    img = cv2.imread(filename)
    return img


def resize_image(pic):
    resized = cv2.resize(pic, (500, 500))
    return resized
     

def display_image(resized,text):
    cv2.imshow(text,resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_image(resized):
    path = filedialog.asksaveasfilename(initialdir="C:/",filetypes = (('jpg files','*.jpg'),('Png files','*.png'),('Jpeg files','*.jpeg')))
    path1 = path + '.jpg'
    cv2.imwrite(path1,resized)



def cartoonize():
    img = name_of_file()

    #converting into grey
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    grey_blurred = cv2.medianBlur(grey_img,5)

    edges=cv2.adaptiveThreshold(grey_blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

    #CARTOON PROCESS
    color=cv2.bilateralFilter(img,9,300,300)
    cartoon=cv2.bitwise_and(color,color,mask=edges)

    #RESIZING
    resized = resize_image(cartoon)

    #DISPLAYING
    display_image(resized, 'Cartoon Image')

    #Save button
    btn3 = Button(root, text ='SAVE', command = partial(save_image,resized), bg = 'Indianred3',font =button_font)
    btn3.pack()
    btn3.place( relx = 0.42, rely = 0.7 , relheight=0.08,relwidth=0.1)



def sketch():
    img = name_of_file()

    #converting into grey
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Inverting image
    inverted_gray_img = 255-grey_img

    #Blur the image by guassian func
    blurred_img = cv2.GaussianBlur(inverted_gray_img,(21,21),15)

    #invert the blur image
    inverted_blur_img = 255 - blurred_img

    #Pencil sketch
    pencil_sketch = cv2.divide(grey_img,inverted_blur_img,scale = 256.0)

    #Resizing
    resized = resize_image(pencil_sketch)

    #Displaying on screen
    display_image(resized, 'Sketch Image')

    #Defining the save button
    btn3 = Button(root, text ='SAVE', command = partial(save_image,resized),bg = 'Indianred3',font =button_font)
    btn3.pack()
    btn3.place(  relx = 0.42, rely = 0.7 , relheight=0.08,relwidth=0.1)


#Defining the root window
root=Tk()
root.title('PIC_EDIT')
root.geometry("620x350")
root.resizable(width = True, height = True)


#Setting the background
background = PhotoImage(file = 'bg1.png')
background_label = Label(root, image = background )
background_label.place(relwidth=1,relheight=1)

#Defining the font
button_font = TkFont.Font(family='Comic Sans MS', size=13, weight=TkFont.BOLD)


#Creating buttons- cartoonify and pencil sketch
btn1 = Button(root, text ='PENCIL SKETCH', command = sketch, bg = 'salmon3',font=button_font)
btn1.pack()
btn1.place( relx = 0.35, rely = 0.5, relheight= 0.1, relwidth= 0.25)

btn2 = Button(root, text ='CARTOONIFY', command = cartoonize, bg = 'sienna3',font=button_font)
btn2.pack()
btn2.place(relx = 0.35, rely = 0.3 , relheight=0.1,relwidth=0.25)

root.mainloop()

