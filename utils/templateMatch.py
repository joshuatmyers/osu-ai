import cv2
import numpy as np

# get image data from getData and pass through into this function to get coordinates
def temp_match(input_img):
    # cursor image is read converted to grayscale after reading to match with the image passed into the function
    cursor_img = cv2.imread('C:/Users/Joshua/Desktop/Projects/Python/osu-ai/osu-ai/template-matching/cursor.png', cv2.IMREAD_GRAYSCALE)
    #game_img = cv2.imread('C:/Users/joshu/Desktop/Projects/Python/osu-ai/template-matching/example.png', cv2.IMREAD_GRAYSCALE)
    game_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(game_img, cursor_img, cv2.TM_CCOEFF_NORMED)
    
    # max loc returns top left coordinate of template that is being matched
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    w = cursor_img.shape[1]
    h = cursor_img.shape[0]

    # in openCV the y coordinate goes down, i.e in a resolution of 800x600, 
    # the coordinate (300, 200), is actually (300, 400)
    
    x = max_loc[0] + 0.5 * w
    y = 600 - (max_loc[1] + 0.5 * h)

    # returns tuple containing coordinates
    return (x,y)

#print(temp_match())
