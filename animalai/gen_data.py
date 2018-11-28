from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
IMAGE_SIZE = 50

# 画像の読み込み

X = []
Y = []
for index, classlabel in enumerate(classes):
    photos_dir = "./" + classlabel
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        if i >= 200: break
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)
