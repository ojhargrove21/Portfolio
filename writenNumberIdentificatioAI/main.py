import cv2
import os.path

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from keras.constraints import maxnorm
from keras.utils import np_utils
from keras.datasets import cifar10
#from azureml.opendatasets import MNIST

#generate machine learning model
# mnist = tf.keras.datasets.mnist
#
# (x_train,y_train),(x_test,y_test)=mnist.load_data()
# x_train =tf.keras.utils.normalize(x_train,axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)
#
# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(400,activation='relu'))
# model.add(tf.keras.layers.Dense(400,activation='relu'))
# model.add(tf.keras.layers.Dense(10,activation='softmax'))
#
# model.compile(optimizer='Nadam',loss='sparse_categorical_crossentropy',metrics='accuracy')
# model.fit(x_train,y_train,epochs=3)
# model.save('handwritten.model')

model = tf.keras.models.load_model('handwritten.model')
#
# #loss, accuracy = model.evaluate(x_test,y_test)
#
# #print(loss)
# #print(accuracy)
image_number = 1
while os.path.isfile(f"digit{image_number}.png"):
    try:
        img = cv2.imread(f"digit{image_number}.png")[:,:,0]

        # Creating the kernel with numpy

        img = np.invert(np.array([img]))

        prediction = model.predict(img)

        print(f"this digit{image_number} is probably a {np.argmax(prediction)}")

        plt.imshow(img[0],cmap=plt.cm.binary)
        plt.show()
    except:
        print("error")
    finally:
        image_number+=1
