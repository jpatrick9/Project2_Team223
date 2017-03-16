#(Course) CST 205-02: Multimedia Design & Programming
#(Title) College Life Captions
#(Abstract) In remembrance of the early 2000s, this program allows the user to
#           create an image macro of some of the most popular "Advice Animals,"
#           which were virulent memes during their time. Additionally, a user can
#           create an image macro of one of the programmers if choose to do so.
#(Authors) James Barquera, Zachary Strader, and Joshua Patrick
#(GitHub) https://github.com/jpatrick9/Project2_Team223
#(Date) Last Edited on 3/15/2017


from easygui import *            #VERY IMPORTANT! Allows us to create a basic UI

from PIL import Image            #Allows us to use Pillow libraries for editing images
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
import PIL.ImageOps

import os                        #Miscellaneous operating system interfaces

#main() by Josh Patrick
def main():
    folder = os.path.dirname(os.path.realpath('__file__'))              #creates the local file path
    
    fileName = os.path.join(folder, '../College-Kid-Captions/Macros/')  #sets up path for image macro access
    fileName = os.path.abspath(os.path.realpath(fileName))
    
    title = 'College Kid Captions'                                      #allows user to pick from a list of image names (made easier by having the folder open)
    choices = ['Celebration Walrus', 'Foul Bachelor Frog', 'Jackass Joshua', 'Jaded Student James', 'Ostentatious Otter', 'Overzealous Zach', 'Seal of Approval']
    
    imageSelection = choicebox ('Select Macro', title, choices)
    imagePath = fileName + "/" + imageSelection + ".jpg"
    
    image = Image.open(imagePath)  #accesses the unedited image
    image.save("copy.jpg")         #creates a copy to be edited
    image = Image.open("copy.jpg") #prepares the copy to be edited
    
    text()
    finalize()

#text() by James Barquera
def text():
    
    #This section instructs the user to caption the image they chose in main(),
    #and allows them to choose what shade their color will have
    msg = "Caption your macro!"
    title = "CollegeKidCaptions"
    colorChoice = buttonbox("Choose the color of your captions!", title, ("Black", "Black-gray", "Gray", "White-gray", "White"))
    
    if (colorChoice == "Black"):
        color = 0
    if (colorChoice == "Black-gray"):
        color = 63
    if (colorChoice == "Gray"):
        color = 127
    if (colorChoice == "White-gray"):
        color = 194
    if (colorChoice == "White"):
        color = 255

    #Creates the prompts for inputting text on the image
    entries = ["Upper Text", "Lower Text"]
    textBoxes = []
    textBoxes = multenterbox(msg, title, entries)

textBoxes[0] = textBoxes[0].upper()
    textBoxes[1] = textBoxes[1].upper()
    
    #Historically, image macros use centered text with
    #Impact font, so our code will do the same
    image = Image.open("copy.jpg")
    imageSize = image.size
    fontSize = int(imageSize[1]/5)
    font = ImageFont.truetype("/Library/Fonts/Arial.ttf", fontSize)
    
    topTextSize = font.getsize(textBoxes[0])
    bottomTextSize = font.getsize(textBoxes[1])
    
    #In the common case that the text is too big for the
    #image, we will resize it to fit
    while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
        fontSize = fontSize - 1
        font = ImageFont.truetype("impact.ttf", fontSize)
        topTextSize = font.getsize(textBoxes[0])
        bottomTextSize = font.getsize(textBoxes[1])

    #centers text in the x and y directions
    topTextPosX = (imageSize[0]/2) - (topTextSize[0]/2)
    bottomTextPosX = (imageSize[0]/2) - (bottomTextSize[0]/2)
    bottomTextPosY = (imageSize[1] - bottomTextSize[1]- 10)

drawTop = ImageDraw.Draw(image)
    drawBottom = ImageDraw.Draw(image)
    
    #drawTop and drawBottom each take four arguments(position, String, RGB, font)
    drawTop.text((topTextPosX,0), textBoxes[0],(color,color,color), font=font)
    drawBottom.text((bottomTextPosX, bottomTextPosY), textBoxes[1],(color,color,color), font=font)
    image.save("newCaption.jpg")

#finalize() by Zachary Strader
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

#editColors() by Zachary Strader
def editColors():
    title = "College Kid Captions"
    #if the user chose to change the image
    #in finalize(), it happens here
    choice = buttonbox('How will you edit your colors?', title, ('Color Invert', 'Monochromatize'))
    if (choice == 'Color Invert'):
        colorInversion()
    elif (choice == 'Monochromatize'):
        textColorChoice()

#colorInversion() by Zachary Strader
def colorInversion():
    image = Image.open("newCaption.jpg")        #Accesses the fresh macro
    inverted_image = PIL.ImageOps.invert(image) #Inverts its RGB values
    inverted_image.save("newCaption.jpg")       #Saves the new macro

#textColorChoice() by Zachary Strader
def textColorChoice():
    image_file = Image.open("newCaption.jpg") #Accesses the macro
    image_file = image_file.convert('1')      #Changes black to white and vice versa
    image_file.save('newCaption.jpg')         #Saves the new macro

#this part was pretty much courtesy of Avner since
#we couldn't find a good way to end the program
while True:
    main()
    loop = buttonbox("Do you want to caption another macro?", "College Kid Captions", ["Yes", "No"])
    if ( loop == 'No' ):
    break