import cv2
import numpy as np

def temp_match():
    cursor_img = cv2.imread('C:/Users/Joshua/Desktop/Projects/Python/osu-ai/osu-ai/template-matching/cursor.png', cv2.IMREAD_UNCHANGED)
    game_img = cv2.imread('C:/Users/Joshua/Desktop/Projects/Python/osu-ai/osu-ai/template-matching/example.png', cv2.IMREAD_UNCHANGED)

    #cv2.imshow('Game', game_img)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    result = cv2.matchTemplate(game_img, cursor_img, cv2.TM_CCOEFF_NORMED)
    #cv2.imshow('Result', result)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    w = cursor_img.shape[1]
    h = cursor_img.shape[0]

    cv2.rectangle(game_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)

    threshold = .355

    yloc, xloc = np.where(result >= threshold)

    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(game_img, (x, y), (x + w, y + h), (0,255,255), 2)

    #cv2.imshow('Game', game_img)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    # in openCV the y coordinate goes down, i.e in a resolution of 800x600, 
    # the coordinate (300, 200), is actually (300, 400)
    x = rectangles[0][0] + 0.5 * rectangles[0][2]
    y = 600 - (rectangles[0][1] + 0.5 * rectangles[0][3])
    return (x,y)

print(temp_match())
