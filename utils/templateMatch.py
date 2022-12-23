import cv2
import numpy as np

# get image data from getData and pass through into this function to get coordinates
def temp_match(input_img):
    # cursor image is read converted to grayscale after reading to match with the image passed into the function
    cursor_img = cv2.imread('C:/Users/joshu/Desktop/Projects/Python/osu-ai/template-matching/cursor.png', cv2.IMREAD_UNCHANGED)
    #cursor_img = cv2.cvtColor(cursor_img, cv2.COLOR_BGR2HSV )
    cursor_img = cv2.cvtColor(cursor_img, cv2.COLOR_BGR2GRAY) # COLOR_BGRA2RGB
    cursor_img = cv2.resize(cursor_img, (40,40), interpolation = cv2.INTER_AREA)
    #input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY) # COLOR_BGR2GRAY, IMREAD_GRAYSCALE
 

    result = cv2.matchTemplate(input_img, cursor_img, cv2.TM_CCOEFF_NORMED)
    
    # max loc returns top left coordinate of template that is being matched
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # returns tuple containing coordinates
    return max_loc

#print(temp_match())
