##Christians PenisPic
from PIL import Image
import os
import random
import glob
import numpy as np
import cv2
import math



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
    newimg.save("test.jpg")

PEEENIS("DSC08495.jpg")#Call a picture
#######################################################################################################################################

def isbright(image, dim=10, thresh=0.5):#function to determine the colour of a picture and sort into dark+bright
    image = cv2.resize(image, (dim, dim))
    L, A, B = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
    L = L/np.max(L)
    return np.mean(L) > thresh

for i, path in enumerate(glob.glob("images/*")):#goes through images and sorts them into bright and dark folder
    image = cv2.imread(path)
    path = os.path.basename(path)
    text = "bright" if isbright(image) else "dark"
    cv2.imwrite("output/{}/{}".format(text, path), image)


###########################################################################################################################################
#Assign pictures based on difference in R,G,B vector space
a = os.listdir("images")
areC = []
directory= "images/"+a[0]
for fname in range(0,(len(a))):
    R = []
    G = []
    B=[]
    CL = []
    directory = "images/"+a[fname]
    c = Image.open(directory)
    c = c.resize([500,500])
    c = list(c.getdata())
    for pixel in c:
        R.append(pixel[0])
        G.append(pixel[1])
        B.append(pixel[2])
    R = np.mean(R)
    G = np.mean(G)
    B = np.mean(B)
    CL = [R, G, B]
    print(CL)
    areC.append(CL)
#k. a enhtält alle bilders namen
#und areC enthält das RGB pendant


def PEEENISNR2 (Im):
    img = Image.open(Im)
    img = img.resize([1000,1000])
    newimg = Image.new('RGB',(10000,10000))
    for i in range(1,101):
        bottom = 1000-(10*i)
        top = bottom+10
        for j in range(0,100):
            R = []
            G = []
            B = []
            PCrap = []
            left = 10*j
            right = left+10
            crap = img.crop((left,bottom,right,top))
            crapp = list(crap.getdata())
            for pixel in crapp:
                R.append(pixel[0])
                G.append(pixel[1])
                B.append(pixel[2])
            R = np.mean(R)
            G = np.mean(G)
            B = np.mean(B)
            m = [R, G, B]
            diffcrap = []
            for Im in areC:
                diffcrap.append(math.sqrt((m[0]-Im[0])**2+(m[1]-Im[1])**2+(m[2]-Im[2])**2))
            PCrap.append(diffcrap)
    print(len(PCrap))

PEEENISNR2("Daniel.jpg")



