#%%
from PIL import Image
import os
import numpy as np
import math
from tqdm import tqdm
from sklearn.neighbors import NearestNeighbors
###########################################################################################################################################
####Advanced
##Create necessary folders
#%%
if os.path.exists('Image database') == False:
    os.mkdir('Image database')


print(list(os.listdir("Image database")))
small_image_folder_name = input("Choose an available image folder or create a 'new' one")
while True:
    if small_image_folder_name == "new":
        break
    elif small_image_folder_name in list(os.listdir("Image database")):
        break
    else:
        small_image_folder_name = input("Pick a valid image folder pick 'new'")
#%%
##Preprocessing small filler pictures
print("Preprocessing Pictures")
subpicSize = int(input("PixelSize of smaller images"))#wie waers die bilder die reingefuegt werden dann eh mit deren groesse auch zupreprocessen!!
PicList = os.listdir("images")
fill_RGB = []
for Bild in PicList:
    TImg = Image.open("images/" + Bild)
    TImg = TImg.resize([subpicSize, subpicSize])
    # get the 
    TImg = np.array(TImg.getdata())
    RGBIM = TImg.mean(axis=0)
    fill_RGB.append(RGBIM)

fill_RGB = np.array(fill_RGB, dtype=float)

#%%
fill_knn = NearestNeighbors(n_neighbors=1)

fill_knn.fit(fill_RGB)
#dont lose it we will need it
#%%
##Preparation. Getting OgPicture details
Name = input("OG image?")#insert a picture name. TO DO- FILEFORMAT!! .jpg, jpeg, png?!?!
Pic  = Image.open(Name + ".jpg")
while True:
    #possibility to standardize picture
    Resizing = input("Woud you like to keep the original pixel ratio or lock. \nPress 1 for keeping the original size\nPress 2 to change to a fixed ratio!\n")
    if Resizing == "1":
        #if not standardizing, adjust height, width just minimally to allow clean segmentations
        x, y = Pic.size
        if x % 10 != 0 and y % 10 != 0:
            print("Width or Heigth might not be fitting. Making small adjustments:")
            print("Original width: ", x)
            print("Original heigth: ", y)
            x += 10 - (x % 10)
            y += 10 - (y % 10)
        Pic = Pic.resize([x, y])
        print("Width: ", x)
        print("Heigth: ", y)
        break
    ##standardize
    elif Resizing == "2":
        Pic = Pic.resize([1000, 1000])#standardize picture. Possible improvement by using locked or fixed ration.
        break
    else:
        print("Error. Wrong Input!")

#######2x2, 5x5 or 10x10 or 1 pixel segmenmtation for the original image!
# How big the bounding boxes 
segSize = int(input("1, 2, 5 or 10x10 pixel areas?"))

######settings for the bigger filled picture. To-Do: adjust for above settings
#Size and how often do we need to get segments on each axis!
Pwidth, Pheight = Pic.size
max_i = int(Pheight / segSize)
max_k = int(Pwidth / segSize)

##create clean canvas with necessary size
PwidthNew = int(max_i * subpicSize)
PheightNew = int(max_k * subpicSize)
NewPic = Image.new('RGB', (PwidthNew, PheightNew))

#Ouch
Heighsteps = segSize
Height_crop_steps = int(PheightNew / max_i)
Widthsteps = segSize
Widgth_crop_steps = int(PwidthNew / max_k)

#%%
#FIX
print("Processing Picture")
for i in tqdm(range(1, max_i + 1)):
    # print("Processing: ",int((i / (max_i)) * 100),"%")
    ##settings cropping Og picture, yaxis
    bottom = Pheight - (i * Heighsteps)
    top = bottom + Heighsteps

    ##settings filling newpicture, yaxis
    ystart = (PheightNew - i * Height_crop_steps)
    for k in range(0, max_k):
        ##settings cropping Og picture, xaxis
        left = k * Widthsteps
        right = left + Widthsteps

        ##settings cropping Og picture, xaxis
        xstart = k * Widgth_crop_steps

        ##crop og image!
        PartImg = Pic.crop((left, bottom, right, top))

        ##algorithm thing!
        PartImg = np.array(PartImg.getdata())#Get RGB value for each pixel in a field

        meanRGB = PartImg.mean(axis=0)
        idx = fill_knn.kneighbors(meanRGB.reshape(1, -1))[1]
        idx = PicList[idx[0][0]]

        ##Fill in new picture
        PicFil = Image.open("images/" + idx)
        PicFil = PicFil.resize((int(Widgth_crop_steps), int(Height_crop_steps)))
        NewPic.paste(PicFil, (xstart, ystart))

#End
NewPic.save(Name + "2.jpg")
# %%
