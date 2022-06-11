from PIL import Image
import os
import numpy as np
import math
###########################################################################################################################################
####Advanced. Assign filled pictures based on R,G,B vector distance

##Create List of RGB values for all available images
#Return a list with these
print("Preprocessing Pictures")
PicList = os.listdir("Image to Image reconstruction/images")
RGB = []
for Bild in PicList:
    R = []
    G = []
    B = []
    TImg = Image.open("Image to Image reconstruction/images/"+Bild)
    TImg = TImg.resize([100,100])
    TImg = list(TImg.getdata())
    for Pixel in TImg:
        R.append(Pixel[0])
        G.append(Pixel[1])
        B.append(Pixel[2])
    R = np.mean(R)
    G = np.mean(G)
    B = np.mean(B)
    RGBIM = [R, G, B, Bild]
    RGB.append(RGBIM)
#dont lose it we will need it

##Preparation. Getting Picture details
Name = input("Whats the name of the jpg file?")#insert a picture name. without jpgfileformat or delete in next line!
Pic  = Image.open("Image to Image reconstruction/"+Name+".jpg")#Open Picture
while True:
    Resizing = input("Woud you like to keep the original pixel ratio or lock. \nPress 1 for keeping the original size\nPress 2 to change to a fixed ratio!\n")
    if Resizing == "1":
        x, y = Pic.size
        while int(x)%10 != 0 and int(y)%10:
            y +=1####This.... this is kinda meh...
            x += 1
        Pic = Pic.resize([x,y])
        break
    elif Resizing == "2":
        Pic = Pic.resize([1000,1000])#standardize picture. Possible improvement by using locked or fixed ration.
        break
    else:
        print("Error. Wrong Input!")
#######
steps = input("How accurate is it supposed to be")#
###The point of this is to have a choice between degree of detail but adding more pictures or processing faster but ending up with a lower resolution. Basically in howmany segments you can seperate the picture.
###But there is an issue because it can be every number because you need a fittingdistribution within the picutre. I'm tired but maybe one of you has an idea
####
Pwidth, Pheight = Pic.size #

PwidthNew = Pwidth*10
PheightNew = Pheight*10
NewPic = Image.new('RGB',(PwidthNew,PheightNew))#create new canvas

Heighsteps = Pheight/100
Height_crop_steps = int(PheightNew/100)
Widthsteps = Pwidth/100
Widgth_crop_steps = int(PwidthNew/100)


print("Processing Picture")
for i in range(1,101):
    bottom = Pheight-(i*Heighsteps)
    top = bottom + Heighsteps
    ystart = (PheightNew-i*Height_crop_steps)
    for k in range(0,100):
        left = k*Widthsteps
        right = left + Widthsteps
        xstart = k*Widgth_crop_steps #set parameters to paste and crop
        PartImg = Pic.crop((left, bottom, right, top))#crop
        PartImg = list(PartImg.getdata())#Get RGB value for each pixel in a field
        R = []
        G = []
        B = []
        for Pixel in PartImg:
            R.append(Pixel[0])
            G.append(Pixel[1])
            B.append(Pixel[2])
        R = np.mean(R)
        G = np.mean(G)
        B = np.mean(B)
        PRGB = [R, G, B]#Save the average RGB values in this one

        DiffValues = []#new list to save differences. Calculate differences and resize appropriate picture
        for DicPicValue in RGB:
            DiffValues.append(math.sqrt((DicPicValue[0]-PRGB[0])**2+(DicPicValue[1]-PRGB[1])**2+(DicPicValue[2]-PRGB[2])**2))#calculate vector diff between this cropped image and all the RGB values from the RGB list
        Index = DiffValues.index(min(DiffValues))#find the index of the picture which has the shortest value
        Index = PicList[Index]#Find the Filename
        PicFil = Image.open("Image to Image reconstruction/images/"+Index)
        PicFil = PicFil.resize((int(Widgth_crop_steps),int(Height_crop_steps)))
        NewPic.paste(PicFil, (xstart, ystart))

NewPic.save("Image to Image reconstruction/"+Name+"2.jpg")


