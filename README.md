## osu-ai
My attempt trying to use Machine Learning and Computer Vision to play osu!
Programmed in Python
Main modules used:
* TensorFlow and Keras
* openCV 
* numPy
* win32api

## How it works
First step of this program is data collection (more detail below). getData.py grabs the live gameplay and uses the method of template matching (using openCV) to find the position of the cursor. This data is stored along with the actual image, in form of a numPy array. nameImg uses this data to create the actual image so it can be fed into the convolutional neural network, as well as a csv file containing all the keypoints. Currently using fastAI, a CNN is trained and fine-tuned using this data. In the same notebook resides the trained agent that grabs screenshots of gameplay, and predicts where the cursor should be.

## Data collection
One of the big hurdles I've come across is data collection. This is because of how valuable accurate data is, with inaccurate data ruining the model. A temporary solution I have created is to grab the cursor position from direct gameplay. This however is not good in the long run, as increasing the magnitude and skill of my model would be incredibly time consuming, but it does provide some accurate data to test the model with. Two ideas I have to automate the data collection are as follows:
* Analyse raw data using circleguard - this can provide accurate data without the need to play the maps, hugely increasing the efficiency. Processing this data so it is usable with the model is a pain, but is doable
* Template matching from videos - using resources such as osr2mp4 will make creating videos simple and easy to increase the scale of the model. My template matching code will have to be improved so cursor data is more accurate and reliable. 

## Instructions
* Before using any of this code, use osr2mp4 and convert replay files of your choice. Alter the settings so it doesnt include the start or end of the replay.
* masking.py deals with the creation of all data used by the model, provide it with the path to the video file and it will create the images and a csv file containing the corresponding coordinates to the image
* Change the paths in the tensorflow notebook, as well as split for training and testing data. Run the notebook and allow the model to train
* The agent isnt included in the repository yet. In the notebook, you can test the model with a provided image of gameplay. If you want to do this with live gameplay, use getScreen.py to return an image, and predict the coordinates (multiply by 10 to get position for osu window in 800x600 res) with the model. Use win32api to actually move the cursor to said position (since the model predicts the position from just the window, an offset will have to be added depending on the location of the window)
## Additional notes
* This is by no means a finished product, I will continue to refine it when I have the motivation and/or time
* Paths will have to be altered manually for each instance it appears in the code
* Intended to be used with the relax mod, key presses will be included at a later date

## Future plans
* Increase accuracy of current TensorFlow model
* Make the program more user friendly - currently very awkward to use
* Try implementing a RCNN/LSTM and compare to CNN
* Automate most of the process for training the model, i.e. supply it with a .osr file and it does the rest of the work

Inspiration taken from:
* https://www.youtube.com/watch?v=LXA7zXVz8A4&t=405s 
* https://github.com/GuiBrandt/OsuLearn
* ClarityCoders
* Vedal

Osu replay files to video files:
* https://github.com/uyitroa/osr2mp4-app/


