#libraries
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras.preprocessing import image as img
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im
import cv2
import os

#load voltage model
def load_voltage_model():
    json_file = open('voltage_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
     # load weights into new model
    loaded_model.load_weights("voltage_model.h5")
    return loaded_model

#load current model
def load_current_model():
        json_file = open('current_model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
     # load weights into new model
        loaded_model.load_weights("current_model.h5")
        return loaded_model

#extract voltage feature
def extract_voltage(image,file_name):
    imge = image[int((image.shape[0]*0.35)):int((image.shape[0]*0.587)),int(((image.shape[1])*0.52)):int(((image.shape[1])*0.99)),:]
    # Output img with window name as 'image'
    imge = cv2.resize(imge, (300, 200))
    if (file_name.endswith(".jpg") or file_name.endswith(".JPG")):
         imge = cv2.cvtColor(imge, cv2.COLOR_BGR2RGB)
    else:
        imge = imge*255
    cv2.imwrite('voltage.png', imge)

#extract current feature
def extract_current(image,file_name):
    imge = image[int((image.shape[0]*0.635)):int((image.shape[0]*0.932)),int(((image.shape[1])*0.05)):int(((image.shape[1])*0.464)),:]
    # Output img with window name as 'image'
    imge = cv2.resize(imge, (300, 200))
    if (file_name.endswith(".jpg") or file_name.endswith(".JPG")):
         imge = cv2.cvtColor(imge, cv2.COLOR_BGR2RGB)
    else:
        imge = imge*255
    cv2.imwrite('current.png', imge)

#testing the health state of voltage brush
def test_voltage(loaded_model):
    image = img.load_img('voltage.png',target_size=(300,200))
    x = img.img_to_array(image)
    x = np.expand_dims(x,axis=0)
    images = np.vstack([x])
    val = loaded_model.predict(images)
    return val[0][0]

#test the health state of current brush
def test_current(loaded_model):
    image = img.load_img('current.png',target_size=(300,200))
    x = img.img_to_array(image)
    x = np.expand_dims(x,axis=0)
    images = np.vstack([x])
    val = loaded_model.predict(images)
    return val[0][0]