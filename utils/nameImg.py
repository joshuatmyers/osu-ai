# this now functions to create the images as well as creating a
# csv file with the equivalent coordinates for the 80x60 image
import cv2
import numpy as np
import os
import pandas as pd

data = np.load("./data/training_data.npy", allow_pickle=True)
targets = np.load("./data/target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Store both data and targets in a list.
# We may want to shuffle down the road.
holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count = 0

# Below code creates the dataframe and following that, the csv file
cols = ['x', 'y', 'image']
lst = []
for data in holder_list:
    lst.append([int(data[1][0]/10), int(data[1][1]/10), data[0]])

df = pd.DataFrame(lst, columns=cols)
df.to_csv('resizedData.csv',index=False)

# Code to create and name the images from the numpy arrays
os.chdir('C:/Users/joshu/Desktop/osu-ai-data/')
for data in holder_list:
    count += 1
    cv2.imwrite(f"C:/Users/joshu/Desktop/osu-ai-data/{count}-{int(data[1][0])}-{int(data[1][1])}.png", data[0]) 
