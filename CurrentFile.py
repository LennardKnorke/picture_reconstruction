from PIL import Image
import os
import numpy as np
import math
###########################################################################################################################################
####Advanced. Assign filled pictures based on R,G,B vector distance

##Create List of RGB values for all available images
#Return a list with these
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
RGB#dont lose it we will need it

##Picture recreation
Name = input("Whats the picture name?")#insert a picture name. without jpgfileformat or delete in next line!
Pic  = Image.open("Image to Image reconstruction/"+Name+".jpg")#Open Picture
Pic = Pic.resize([1000,1000])#standardize picture. Possible improvement by using locked or fixed ration.
NewPic = Image.new('RGB',(10000,10000))#create new canvas

for i in range(1,101):
    bottom = 1000-(i*10)
    top = bottom + 10
    ystart = (10000-i*100)
    for k in range(0,100):
        left = k*10
        right = left + 10
        xstart = k*100 #set parameters to paste and crop

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

        DiffValues = []#new list to save differences
        for DicPicValue in RGB:
            DiffValues.append(math.sqrt((DicPicValue[0]-PRGB[0])**2+(DicPicValue[1]-PRGB[1])**2+(DicPicValue[2]-PRGB[2])**2))#calculate vector diff between this cropped image and all the RGB values from the RGB list
        Index = DiffValues.index(min(DiffValues))#find the index of the picture which has the shortest value
        Index = PicList[Index]#Find the Filename
        PicFil = Image.open("Image to Image reconstruction/images/"+Index)
        PicFil = PicFil.resize((100,100))
        NewPic.paste(PicFil, (xstart, ystart))
NewPic.save("Image to Image reconstruction/"+Name+"2.jpg")
