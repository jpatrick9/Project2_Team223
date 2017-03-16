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
