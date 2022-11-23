# training model with the data previously created
# tensorflow and keras will be used for this project
from fastai.vision.all import *
import time
import cv2
from utils.getScreen import grab_screen
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, CuDNNLSTM as LSTM, Input, GaussianNoise

path = Path("C:\Users\Joshua\Desktop\Data\osu-ai")
imgs = get_image_files(path)
lbls = get_files(path, extension='.png')
print(f"Total images: {len(imgs)}")

def img2kpts(f):
    name = os.path.basename(f)
    split = str(name).split("-")
    kpts = []
    kpts.append([int(split[1]), int(split[2][:4])])
    return tensor(kpts)

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