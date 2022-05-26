###Picture Reconstruction Program
##PACKAGES
from PIL import Image
import numpy as np
import os
import random
import glob
import cv2


##ALPHA VERSION. The very first one which started it all.

#First a function to determin whether a picture is bright or dark
def isbright(image, dim=10, thresh=0.5):
    image = cv2.resize(image, (dim, dim))
    L, A, B = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
    L = L/np.max(L)
    return np.mean(L) > thresh

#Creates folder for the sorted pictures
os.makedirs("Image to Image reconstruction/output/bright", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/dark", exist_ok= True)

#loops through the images and sorts them
for i, path in enumerate(glob.glob("images/*")):#goes through images and sorts them into bright and dark folder
    image = cv2.imread(path)
    path = os.path.basename(path)
    text = "bright" if isbright(image) else "dark"
    cv2.imwrite("output/{}/{}".format(text, path), image)

#the function which reconstructs the picture
def PEEENIS (Im):#Function. Calls a picture which gets translated and saved as a penic pic
    img = Image.open(Im)
    img = img.resize([1000,1000])
    newimg = Image.new('RGB',(10000,10000))
    for i in range(1,101):
        bottom = 1000-(10*i)
        top = bottom+10
        for j in range(0,100):
            left = 10*j
            right = left+10
            newpic = []
            crap = img.crop((left,bottom,right,top))
            crapp = list(crap.getdata())
            xstart = j*100
            ystart = (10000-i*100)            
            for pixel in crapp:
                newpic.append((pixel[0]+pixel[1]+pixel[2])/3)
            if np.mean(newpic) <= 128:
                file_path_type =["./output/dark/*.jpg"]
                allImg = glob.glob(random.choice(file_path_type))
                rImg = random.choice(allImg)
                rImg = Image.open(rImg)
                rImg = rImg.resize((100,100))
                newimg.paste(rImg,(xstart,ystart))
            else:
                file_path_type =["./output/bright/*.jpg"]
                allImg = glob.glob(random.choice(file_path_type))
                rImg = random.choice(allImg)
                rImg = Image.open(rImg)
                rImg = rImg.resize((100,100))
                newimg.paste(rImg,(xstart,ystart))
    newimg.save("NewPic.jpg")

PEEENIS("UnknownPerson.jpg")#Call a picture# Call function: PEEENIS()

#################################################################
##Alpha2.0 using 8 Colors
##PreComments
#One issue I am having is with my workspace. As you can see I have specific name still for the folders in which stuff is supposed to be. Is there an easy fix?
#
#Feed a list or tuple with 3 values(R,G,B) and it tells you which of the 8 colors it belongs to
def DefCol (PicValue):
    if PicValue[0] <= 128:
        if PicValue[1]<=128:
            if PicValue[2] <= 128:
                return "Black"
            else:
                return "Blue"
        else:
            if PicValue[2] <= 128:
                return "Green"
            else:
                return "Türkis"
    else:
        if PicValue[1] <= 128:
            if PicValue[2] <= 128:
                return "Red"
            else:
                return "Pink"
        else:
            if PicValue[2] <= 128:
                return "Yellow"
            else:
                return "White"

#Feed a jpeg image object
def DfRGB (Img):
    PrePic = list(Img.getdata())
    R = []
    G = []
    B = []
    for entry in PrePic:
        R.append(entry[0])
        G.append(entry[1])
        B.append(entry[2])
    R = np.mean(R)
    G = np.mean(G)
    B = np.mean(B)
    PicRGB = [R, G, B]
    return PicRGB

#Create Folders for 8 colors
os.makedirs("Image to Image reconstruction/output/Black", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/White", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Blue", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Green", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Türkis", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Red", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Pink", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Yellow", exist_ok= True)

#Loop Pictures into folders
for Picture in os.listdir("Image to Image reconstruction/images"):
    Pic = Image.open("Image to Image reconstruction/images/"+Picture)
    PicColour = DefCol(DfRGB(Pic))
    Pic.save("Image to Image reconstruction/output/"+PicColour+"/"+Picture)


#Final loop which recreates the pictue
Pic = "Richi" # Enter the title of a jpg picture. I tried a familiar face :))
#run script
Pic = Image.open("Image to Image reconstruction/"+Pic+".jpg")
Pic = Pic.resize((1000,1000))
NewPic = Image.new('RGB',(10000,10000))
for i in range(1,101):
    bottom = 1000-(10*i)
    top = bottom+10
    for j in range(0,100):
        left = 10*j
        right = left+10
        crap = Pic.crop((left,bottom,right,top))
        CuCol = DefCol(DfRGB(crap))
        xstart = j*100
        ystart = (10000-i*100)
        if CuCol == "Black":
            file_path_type =["./Image to Image reconstruction/output/Black/*.jpg"]
            allImg = glob.glob(random.choice(file_path_type))
            rImg = random.choice(allImg)
            rImg = Image.open(rImg)
            rImg = rImg.resize((100,100))
            NewPic.paste(rImg,(xstart,ystart))
        elif CuCol == "White":
            file_path_type =["./Image to Image reconstruction/output/White/*.jpg"]
            allImg = glob.glob(random.choice(file_path_type))
            rImg = random.choice(allImg)
            rImg = Image.open(rImg)
            rImg = rImg.resize((100,100))
            NewPic.paste(rImg,(xstart,ystart))
        elif CuCol == "Pink":
            file_path_type =["./Image to Image reconstruction/output/Pink/*.jpg"]
            allImg = glob.glob(random.choice(file_path_type))
            rImg = random.choice(allImg)
            rImg = Image.open(rImg)
            rImg = rImg.resize((100,100))
            NewPic.paste(rImg,(xstart,ystart))
        elif CuCol == "Blue":
            file_path_type =["./Image to Image reconstruction/output/Blue/*.jpg"]
            allImg = glob.glob(random.choice(file_path_type))
            rImg = random.choice(allImg)
            rImg = Image.open(rImg)
            rImg = rImg.resize((100,100))
            NewPic.paste(rImg,(xstart,ystart))
        elif CuCol == "Green":
            file_path_type =["./Image to Image reconstruction/output/Green/*.jpg"]
            allImg = glob.glob(random.choice(file_path_type))
            rImg = random.choice(allImg)
            rImg = Image.open(rImg)
            rImg = rImg.resize((100,100))
            NewPic.paste(rImg,(xstart,ystart))
        elif CuCol == "Türkis":
            file_path_type =["./Image to Image reconstruction/output/Türkis/*.jpg"]
            allImg = glob.glob(random.choice(file_path_type))
            rImg = random.choice(allImg)
            rImg = Image.open(rImg)
            rImg = rImg.resize((100,100))
            NewPic.paste(rImg,(xstart,ystart))
        elif CuCol == "Yellow":
            file_path_type =["./Image to Image reconstruction/output/Yellow/*.jpg"]
            allImg = glob.glob(random.choice(file_path_type))
            rImg = random.choice(allImg)
            rImg = Image.open(rImg)
            rImg = rImg.resize((100,100))
            NewPic.paste(rImg,(xstart,ystart))
        elif CuCol == "Red":
            file_path_type =["./Image to Image reconstruction/output/Red/*.jpg"]
            allImg = glob.glob(random.choice(file_path_type))
            rImg = random.choice(allImg)
            rImg = Image.open(rImg)
            rImg = rImg.resize((100,100))
            NewPic.paste(rImg,(xstart,ystart))
        else:
            print("Fail")
NewPic.save("Image to Image reconstruction/NewPic.jpg")
