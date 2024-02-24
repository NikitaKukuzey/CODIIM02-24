import torch
import cv2
from torch import nn
from torchvision.transforms import Resize
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import requests
import timm
import json
from joblib import load

class MyModel:

    def __init__(self, path=None):
        self.transform = timm.data.create_transform((3, 224, 224))
        self.m = timm.create_model('resnet18', pretrained=True, num_classes=0)
        self.m.eval()
        self.model = load(path)


    def __call__(self, img_path):
        labels = ['apple_pie', 'caesar_salad', 'caprese_salad', 'carrot_cake', 'cheesecake', 'chicken_curry',
                  'chocolate_cake', 'chocolate_mousse', 'donuts', 'dumplings', 'eggs_benedict', 'greek_salad',
                  'lasagna', 'pancakes', 'panna_cotta', 'peking_duck', 'pizza', 'ramen', 'risotto', 'waffles']
        # Открываем и преобразуем изображение в тензор
        img = Image.open(img_path)
        img_tensor = self.transform(img).unsqueeze(0)
        # Получаем предсказание класса
        with torch.no_grad():
            vector = self.m(img_tensor).cpu().numpy()

        # Отображение изображения
        # plt.imshow(img)
        # plt.axis('off')
        # plt.show()

        class_idx = self.model.predict(vector)
        # print(class_probs, vector.shape)
        # # Преобразуем выходной тензор в вероятности и получаем индекс класса с наибольшей вероятностью
        # probabilities = softmax(class_probs)
        # predicted_class_idx = np.argmax(probabilities)
        predicted_class_name = labels[int(class_idx)]
        return predicted_class_name

