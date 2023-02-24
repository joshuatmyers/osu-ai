from threading import Thread, Lock
import numpy as np
import cv2
import ctypes
import random
import pandas as pd

user32 = ctypes.windll.user32

with open('C:/Users/joshu/Desktop/Projects/Python/osu-ai/data/coordinates.csv', 'a') as f:
    f.write("x, y")
    f.writelines('\n')

class Detection:
    # threading properties
    stopped = True

    # we are looking for the position of flashing colors
    # we need the position of the flashing window and the current color
    position = None
    color = None

    # Variable to track if position is found
    is_Found = False
    Found_pos = (0, 0, 0, 0)
    pos_list = []
    cont_list = []

    
    def __init__(self, path):

        self.cap = cv2.VideoCapture(path)

        if not self.cap.isOpened():
            print("Cannot open Video")
            exit()
            
        # Get video info
        self.scale_percent = 100 # percent of original size
        width, height = self.cap.get(3), self.cap.get(4)
        width = int(width * self.scale_percent / 100)
        height = int(height * self.scale_percent / 100)
        self.dim = (width, height)

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def check_color(self, frame):
        avg_color_per_row = np.average(frame, axis=0)
        b = int(np.average(avg_color_per_row, axis=0)[0])
        g = int(np.average(avg_color_per_row, axis=0)[1])
        r = int(np.average(avg_color_per_row, axis=0)[2])
        self.color = (r,g,b)

    def Check_contours(self, contours, frame):
        largest_area = 0
        largest_pos = None
        #self.pos_list = []
        for cnt in contours:
            # Calculate area and choose only the biggest elements
            area = cv2.contourArea(cnt)
            if area >= largest_area:
                largest_pos = cv2.boundingRect(cnt)
                largest_area = area

        if largest_pos:
            x, y, w, h = largest_pos
            #cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            return (x+w/2) * (100 / self.scale_percent), (y+h/2) * (100 / self.scale_percent)
        else:
            return 0, 0
                
        
    def run(self):
        old_cord = 0,0
        count = 0
        while not self.stopped:   
            # Read a new frame
            ret, frame = self.cap.read()

            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            
            # Resize the frame
            frame = cv2.resize(frame, self.dim, interpolation = cv2.INTER_AREA)

            #lowerHSV = np.array([0, 0, 0])
            #upperHSV  = np.array([180, 255, 250])

            img_hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # lower mask (0-10)
            lower_red = np.array([0,50,50])
            upper_red = np.array([10,255,255])
            mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

            # upper mask (170-180)
            lower_red = np.array([140,50,50])
            upper_red = np.array([150,255,255])
            mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

            # join my masks
            mask = mask0+mask1

            # set my output img to zero everywhere except my mask
            output_img = frame.copy()
            output_img[np.where(mask==0)] = 0

            # or your HSV image, which I *believe* is what you want
            output_hsv = img_hsv.copy()
            output_hsv[np.where(mask==0)] = 0


            # Find all countours and draw a rectangle 
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            x, y = self.Check_contours(contours, frame)

            # only record after the first 120 frames to avoid recording into with bg
            if count < 120:
                count += 1
            if count >= 120:
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                img = cv2.resize(img, (80,60), interpolation = cv2.INTER_AREA)
                cv2.imwrite("C:/Users/joshu/Desktop/Projects/Python/osu-ai/data/frames/frame-%d.jpg" % (count-120), img)
                count += 1

                with open('C:/Users/joshu/Desktop/Projects/Python/osu-ai/data/coordinates.csv', 'a') as f:
                    f.write("{}, {}".format((x/10),(y/10)))
                    f.writelines('\n')
            
            # display the images
            #cv.imshow('OUTPUT', frame)

            # press 'q' with the output window focused to exit.
            # waits 1 ms every loop to process key presses
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
  
    cv2.destroyAllWindows()

# load the detector
path = "C:/Users/joshu/Desktop/Projects/Python/osu-ai/data/replay-path/replay.avi"
detector = Detection(path)
# start detection
detector.start()

