'''
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD,RMSprop,Adam
from keras.utils import np_utils

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
#import theano
from PIL import Image
from numpy import *
# SKLEARN
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
#from Alexnet import AlexNet

# input image dimensions
img_rows, img_cols = 64, 64

# number of channels
img_channels = 3



path1 = 'D:/All Code/Project Done/Fake_Currency 100% Code/test/7'    #path of folder of images    
path2 = 'D:/All Code/Project Done/Fake_Currency 100% Code/testing'  #path of folder to save images    

listing = os.listdir(path1)
num_samples=size(listing)
print(num_samples)

for file in listing:
    im = Image.open(path1 + '\\' + file)  
    img = im.resize((img_rows,img_cols))
    gray = img.convert(mode='RGB')
                #need to do some more processing here          
    gray.save(path2 +'\\' +  file, "JPEG")

'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Convolution2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD, RMSprop, Adam
#from tensorflow.keras.utils import np_utils

import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import os

# input image dimensions
img_rows, img_cols = 64, 64

# number of channels
img_channels = 3

path1 = r'C:\Users\hp\OneDrive\Desktop\Anuj IMP\BE IT PROJEC 2023\fake currency 100% code/test/7'    # path of folder of images    
path2 = r'C:\Users\hp\OneDrive\Desktop\Anuj IMP\BE IT PROJEC 2023\fake currency 100% code/testing'  # path of folder to save images    

listing = os.listdir(path1)
num_samples = len(listing)
print(num_samples)

for file in listing:
    im = Image.open(os.path.join(path1, file))
    img = im.resize((img_rows, img_cols))
    gray = img.convert(mode='RGB')
    gray.save(os.path.join(path2, file), "JPEG")



