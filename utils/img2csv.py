# creating csv with filename and the x and y coordinates
import pandas as pd
import numpy as np
from fastai.vision.all import *

#f = pd.DataFrame(columns=['filename','x','y'])

path = Path("C:/Users/Joshua/Desktop/Data/osu-ai")
imgs = get_image_files(path)
#lbls = get_files(path, extension='.png')
print(f"Total images: {len(imgs)}")

""""
def img2kpts(f):
    name = os.path.basename(f)
    split = str(name).split("-")
    kpts = []
    kpts.append([int(split[1]), int(split[2][:4])])
    return kpts
"""
cols = ['filename', 'x', 'y']
lst = []
for i in range(len(imgs)-1):
    name = os.path.basename(imgs[i])
    split = str(name).split("-")
    lst.append([os.path.basename(imgs[i]), int(split[1]), int(split[2][:-4])])
    #df['filename'] = os.path.basename(imgs[i])
    #df['x'] = int(split[1])
    #df['y'] = int(split[2][:-4])

df1 = pd.DataFrame(lst, columns=cols)
df1.to_csv('data.csv',index=False)
