#main() by Josh Patrick
def main():
    folder = os.path.dirname(os.path.realpath('__file__'))              #creates the local file path
    
    fileName = os.path.join(folder, '../College Kid Captions/Macros/')  #sets up path for image macro access
    fileName = os.path.abspath(os.path.realpath(fileName))
    
    title = 'College Kid Captions'                                      #allows user to pick from a list of image names (made easier by having the folder open)
    choices = ['Celebration Walrus', 'Foul Bachelor Frog', 'Jackass Joshua', 'Jaded Student James', 'Ostentatious Otter', 'Overzealous Zach', 'Seal of Approval']
    
    imageSelection = choicebox ('Select Macro', title, choices)
    imagePath = fileName + "\\" + imageSelection + ".jpg"

    image = Image.open(imagePath)  #accesses the unedited image
    image.save("copy.jpg")         #creates a copy to be edited
    image = Image.open("copy.jpg") #prepares the copy to be edited

    text()
    finalize()

#this function *should* be able to handshake with all the others if we format them correctly.    
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
    font = ImageFont.truetype("impact.ttf", fontSize)
    
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
