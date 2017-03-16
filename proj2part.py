from easygui import *

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
import PIL.ImageOps

import os

def finalize():
    
    #preps the captioned/altered macro to be named and saved by the user
    while True:
        image = Image.open("newCaption.jpg")
        msgConfirm = "Save this image macro?"
        actions = ["Yes", "Edit Captions", "Edit Colors", "No"]
        reply = buttonbox(msgConfirm, image="newCaption.jpg", choices=actions)
        if reply == ("Yes"):
            saveName = enterbox("What will you call your new image?", "College Kid Captions", "newMacro")
            image.save(saveName + ".jpg")
            break
        elif reply == ("Edit Captions"):
            text()
        elif reply == ("Edit Colors"):
            editColors()
        else:
            break


def editColors():
    title = "College Kid Captions"
    #if the user chose to change the image
    #in finalize(), it happens here
    choice = buttonbox('How will you edit your colors?', title, ('Color Invert', 'Monochromatize'))
    if (choice == 'Color Invert'):
        colorInversion()
    elif (choice == 'Monochromatize'):
        textColorChoice()


def colorInversion():
    image = Image.open("newCaption.jpg")        #Accesses the fresh macro
    inverted_image = PIL.ImageOps.invert(image) #Inverts its RGB values
    inverted_image.save("newCaption.jpg")       #Saves the new macro


def textColorChoice():
    image_file = Image.open("newCaption.jpg") #Accesses the macro
    image_file = image_file.convert('1')      #Changes black to white and vice versa
    image_file.save('newCaption.jpg')         #Saves the new macro

