# training model with the data previously created
# tensorflow and keras will be used for this project
from fastai.vision.all import *
import time
import cv2
import numpy as np
import pandas as pd
from utils.getScreen import grab_screen
import matplotlib.pyplot as plt
import PIL
import pathlib
from PIL import Image 
from PIL.ImageDraw import Draw
import tensorflow as tf
import tensorflow as keras
from keras import Model, layers
from keras.layers import *

training_csv_file = 'data.csv'
training_image_dir = 'C:/Users/Joshua/Desktop/Data/osu-ai'

training_image_records = pd.read_csv(training_csv_file)
train_image_path = os.path.join(os.getcwd(), training_image_dir)

train_images = []
train_targets = []

for index, row in training_image_records.iterrows():

    (filename, x, y) = row

    train_image_fullpath = os.path.join(train_image_path, filename)
    train_img = keras.preprocessing.image.load_img(train_image_fullpath, target_size=(600, 800))
    train_img_arr = keras.preprocessing.image.img_to_array(train_img)

    train_images.append(train_img_arr)
    train_targets.append((x, y))

train_images = np.array(train_images)
train_targets = np.array(train_targets)

validation_images = np.array(validation_images)
validation_targets = np.array(validation_targets)

width = 800
height = 600


#create the common input layer
input_shape = (height, width, 3)
input_layer = tf.keras.layers.Input(input_shape)

#create the base layers
base_layers = layers.experimental.preprocessing.Rescaling(1./255, name='bl_1')(input_layer)
base_layers = layers.Conv2D(16, 3, padding='same', activation='relu', name='bl_2')(base_layers)
base_layers = layers.MaxPooling2D(name='bl_3')(base_layers)
base_layers = layers.Conv2D(32, 3, padding='same', activation='relu', name='bl_4')(base_layers)
base_layers = layers.MaxPooling2D(name='bl_5')(base_layers)
base_layers = layers.Conv2D(64, 3, padding='same', activation='relu', name='bl_6')(base_layers)
base_layers = layers.MaxPooling2D(name='bl_7')(base_layers)
base_layers = layers.Flatten(name='bl_8')(base_layers)

#create the localiser branch
locator_branch = layers.Dense(128, activation='relu', name='bb_1')(base_layers)
locator_branch = layers.Dense(64, activation='relu', name='bb_2')(locator_branch)
locator_branch = layers.Dense(32, activation='relu', name='bb_3')(locator_branch)
locator_branch = layers.Dense(4, activation='sigmoid', name='bb_head')(locator_branch)

model = tf.keras.Model(input_layer, outputs=[locator_branch])

losses = {"bb_head":tf.keras.losses.MSE}

model.compile(loss=losses, optimizer='Adam', metrics=['accuracy'])

trainTargets = {
    "bb_head": train_targets
}
validationTargets = {
    "bb_head": validation_targets
}

history = model.fit(train_images, trainTargets,
             validation_data=(validation_images, validationTargets),
             batch_size=4,
             epochs=20,
             shuffle=True,
             verbose=1)

for layer in model.layers:
    if layer.name.startswith('bl_'):
        layer.trainable = False
        
for layer in model.layers:
    if layer.name.startswith('bb_'):
        layer.trainable = False

def label_func(x): return x.name[0:7]

def run():
    path = Path("C:/Users/Joshua/Desktop/Data/osu-ai/")
    fnames = get_image_files(path)
    print(f"Total Images:{len(fnames)}")


    dls = ImageDataLoaders.from_path_func(path, fnames, label_func,bs=20, num_workers=0)
    learn = cnn_learner(dls, resnet18, metrics=error_rate)
    print("Loaded")
    learn.remove_cb(ProgressCallback)
    learn.fine_tune(2, base_lr=1.0e-02)

    learn.export()

    # start_time = time.time()
    # test = learn.predict('g1-j5.png')
    # print("--- %s seconds ---" % (time.time() - start_time))
    # print(test)
    #start_time = time.time()
    #image = grab_screen(region=(50, 100, 799, 449))
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = cv2.Canny(image, threshold1=200, threshold2=300)
    #image = cv2.resize(image, (224, 224))
    #test = learn.predict(image)
    #print("--- %s seconds ---" % (time.time() - start_time))
    #print(test)


if __name__ == '__main__':
    run()