# loads model created
# capture window using opencv2
# make predictions from screenshot
# carry out prediction
# repeat
import random
import time

from utils.getInput import key_input
import pydirectinput
import keyboard
import time
import cv2
from utils.getScreen import grab_screen
from fastai.vision.all import *

def label_func(x): return x.parent.name
learn_inf = load_learner()
print("loaded learner")



while True:

    image = grab_screen(region=(100, 100, 899, 699))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image,(224,224))
    
    # cv2.waitKey(1)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]
    