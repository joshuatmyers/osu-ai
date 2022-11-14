# Plans for getData.py

# capture osu! window
# apply grayscale and filter to reduce size

# Inside a while loop:
# take a screenshot
# take current mouse position => append to array
# take current keys pressed => append to different array
# check if button has been pressed to stop taking data

# Labelling images:
# loop through all images
# attach mouse pos (x,y) to name of image
import numpy as np
import cv2
import time
import os

from utils.getScreen import grab_screen
from utils.getInput import key_input

file_name = "C:/Users/Joshua/Desktop/Projects/Python/osu-ai/osu-ai/data/training_data.npy"
file_name2 = "C:/Users/Joshua/Desktop/Projects/Python/osu-ai/osu-ai/data/target_data.npy"


def get_data():

    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))
    else:
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets


def save_data(image_data, targets):
    np.save(file_name, image_data)
    np.save(file_name2, targets)


image_data, targets = get_data()
while True:
    keys = key_input()
    print("waiting press B to start")
    if keys == "B":
        print("Starting")
        break

count = 0
while True:
    count +=1
    last_time = time.time()
    image = grab_screen(region=(100, 100, 899, 699))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Canny filter makes the cursor invisible to the program, may work around later
    #image = cv2.Canny(image, threshold1=19, threshold2=20)

    image = cv2.resize(image, (224, 224))

    # Debug line to show image
    cv2.imshow("AI Peak", image)
    cv2.waitKey(1)

    # Convert to numpy array
    #image = np.array(image)
    #image_data.append(image)

    # Send image to template matching to get x and y coordinates
    # Alternitavely, could use win32api to get cursor position relative to the game window

    # key presses to be included in the model at another time
    #keys = key_input()
    #targets.append(keys)
    if keys == "H":
        break

    print('loop took {} seconds'.format(time.time()-last_time))

save_data(image_data, targets)