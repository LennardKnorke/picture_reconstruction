#%%
from PIL import Image
import os
import numpy as np
from tqdm import tqdm
from sklearn.neighbors import NearestNeighbors

def choose_image_folder(data_base_exists):
    if data_base_exists == False:
        return "new"
    print(os.listdir("Image Database"))
    while True:
        folder_choice = input("choose an available folder create a 'new' folder")
        if folder_choice == "new" or folder_choice == "New":
            return "new"
        elif folder_choice in list(os.listdir('Image Database/')):
            return folder_choice
        else:
            print("Invalid choice")

def check_database_exists():
    if os.path.exists('Image database') == False:
        os.mkdir('Image database')
        return False
    else:
        return True
def choose_crop_size():
    while True:
        crop_size = input("Choose 1x1, 2x2, 5x5 or 10x10 crop area. Smaller choices result in higher quality but increased memory space and processing time")
        if crop_size == "1x1" or crop_size == "1" or crop_size == "11":
            return 1
        elif crop_size == "2x2" or crop_size == "2" or crop_size =="22":
            return 2
        elif crop_size == "5x5" or crop_size == "5" or crop_size =="55":
            return 5
        elif crop_size == "10x10" or crop_size == "10":
            return 10

def pre_process_smaller_pictures(folder, sub_pic_size):
    print("Preprocessing Pictures")
    picture_list = os.listdir(f"Image database/{folder}")
    fill_RGB = []
    for pic in tqdm(picture_list):
        Temp_Img = Image.open(f"Image database/{folder}/" + pic)
        Temp_Img = Temp_Img.resize([sub_pic_size, sub_pic_size])
        # get the 
        Temp_Img = np.array(Temp_Img.getdata())
        RGBIM = Temp_Img.mean(axis=0)
        fill_RGB.append(RGBIM)
    fill_RGB = np.array(fill_RGB, dtype=float)
    return fill_RGB

def fit_model(rgb_list):
    fill_knn = NearestNeighbors(n_neighbors=1)
    fill_knn.fit(rgb_list)
    return fill_knn

def fetch_google_pics(keyword):
    pass

def find_og():
    while True:
        name = input("Enter a valid name of a picture ending on jpg or jpeg")
        if name in os.listdir():
            return name
        elif name+'.jpg' in os.listdir():
            return name+'.jpg'

def open_and_adjust_picture(file_name):
    picture = Image.open(file_name)
    while True:
        #possibility to standardize picture
        Resizing = input("Woud you like to keep the original pixel ratio or lock. \nPress 1 for keeping the original size\nPress 2 to change to a fixed ratio!\n")
        if Resizing == "1":
            #if not standardizing, adjust height, width just minimally to allow clean segmentations
            x, y = picture.size
            if x % 10 != 0 and y % 10 != 0:
                print("Width or Heigth might not be fitting. Making small adjustments:")
                print("Original width: ", x)
                print("Original heigth: ", y)
                x += 10 - (x % 10)
                y += 10 - (y % 10)
            picture = picture.resize([x, y])
            print("Width: ", x)
            print("Heigth: ", y)
            break
        ##standardize
        elif Resizing == "2":
            picture = picture.resize([1000, 1000])#standardize picture. Possible improvement by using locked or fixed ration.
            break
        else:
            print("Error. Wrong Input!")
    return picture

def create_new_picture(og_picture, subpicSize, segSize, knn_model, small_picture_list, selected_folder):
    Pwidth, Pheight = og_picture.size
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
            PartImg = og_picture.crop((left, bottom, right, top))

            ##algorithm thing!
            PartImg = np.array(PartImg.getdata())#Get RGB value for each pixel in a field

            meanRGB = PartImg.mean(axis=0)
            idx = knn_model.kneighbors(meanRGB.reshape(1, -1))[1]
            idx = os.listdir(f"Image database/{selected_folder}/")[idx[0][0]]

            ##Fill in new picture
            PicFil = Image.open(f"Image database/{selected_folder}/" + idx)
            PicFil = PicFil.resize((int(Widgth_crop_steps), int(Height_crop_steps)))
            NewPic.paste(PicFil, (xstart, ystart))
    NewPic.save("new_picture.jpg")



###Main Loop
if __name__ == "__main__":
    RUNNING = True
    data_exists = check_database_exists()
    while RUNNING:
        small_folder = choose_image_folder(data_base_exists= data_exists)

        #Create a new image database to use
        if small_folder == "new":
            fetch_google_pics("lol")
            print("WORK IN PROGRESS")
            break
        #Internal loop. Gets user input for the cropping resolution
        og_crop_size = choose_crop_size()

        #Choose size of the filling pictures replacing a croped area
        small_pictures_size = input("Choose the size of the filling pictures")
        small_pictures_size = int(small_pictures_size)

        all_pics_rgbvals = pre_process_smaller_pictures(small_folder, small_pictures_size)
        model = fit_model(all_pics_rgbvals)

        og_picture = find_og()
        og_picture = open_and_adjust_picture(og_picture)

        create_new_picture(og_picture=og_picture, subpicSize = small_pictures_size, segSize = og_crop_size, knn_model = model, small_picture_list = all_pics_rgbvals, selected_folder = small_folder)

        doagain = input("enter 'exit' to exit the programm or any input to try again")
        if  doagain == "exit" or doagain == "Exit":
            RUNNING = False