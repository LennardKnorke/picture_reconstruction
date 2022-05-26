from PIL import Image
import os
import random
import glob
import numpy as np
import cv2

###########################################################################################################################################
#Assign pictures based on difference in R,G,B vector space.. WORK IN PROGRESS!!!
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
