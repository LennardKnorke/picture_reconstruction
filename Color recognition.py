from PIL import Image
import numpy as np
import os
import random
import glob
##################  Pre functions and Prepwork
#Recognize Colour in jpg pixel list
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

#get jpg pixel list!
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

os.makedirs("Image to Image reconstruction/output/Black", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/White", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Blue", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Green", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Türkis", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Red", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Pink", exist_ok= True)
os.makedirs("Image to Image reconstruction/output/Yellow", exist_ok= True)

##################      Assigning Pictures into folders

for Picture in os.listdir("Image to Image reconstruction/images"):
    Pic = Image.open("Image to Image reconstruction/images/"+Picture)
    PicColour = DefCol(DfRGB(Pic))
    Pic.save("Image to Image reconstruction/output/"+PicColour+"/"+Picture)


###################     Dick Pic Generator 1.1
Pic = "Miha" # Enter the title of a jpg picture
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
        elif CuCol == "white":
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
NewPic.save("Image to Image reconstruction/Mihatry.jpg")


##################################### 2.0


