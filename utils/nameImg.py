import cv2
import numpy as np
import os

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

os.chdir('C:/Users/Joshua/Desktop/Data/osu-ai/')
for data in holder_list:
    #print(int(data[1][0]))
    count += 1
    #if not os.path.exists(f"{int(data[1][0])}-{int(data[1][1])}"):
    #    os.mkdir(f"{int(data[1][0])}-{int(data[1][1])}")
    #cv2.imwrite(f"C:/Users/Joshua/Desktop/Data/osu-ai/{int(data[1][0])}-{int(data[1][1])}/{count}.png", data[0]) 
    cv2.imwrite(f"C:/Users/Joshua/Desktop/Data/osu-ai/{int(data[1][0])}-{int(data[1][1])}-{count}.png", data[0]) 