import cv2 as cv
from PIL import Image, ImageOps
from paddleocr import PPStructure, draw_structure_result, save_structure_res
from matplotlib import pyplot as plt
import numpy as np
import os
from .Const import (IMAGE_FOLDER, IMAGE_NAME)
class OCR:
    def __init__(self, image_name):
        self.image_path = IMAGE_NAME + image_name + ".jpg"
        self.table_engine = PPStructure(show_log = False)
        os.makedirs(IMAGE_FOLDER, exist_ok=True)

    def sharpen_image(self, image):
        gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(gray_img, (0, 0), 1)
        sharpened = cv.addWeighted(gray_img, 1.5, blurred, -0.5, 0)
        return sharpened

    def store_image(self, image):
        if os.path.exists(self.image_path):
            os.remove(self.image_path)
        print("Writing to file in progress......")
        cv.imwrite(self.image_path, image)
        # if os.path.exists(IMAGE_FOLDER + IMAGE_NAME + image_name):
        #     os.remove(IMAGE_FOLDER + IMAGE_NAME + image_name)
    
    def read_image(self):
        img = cv.imread(self.image_path)
        blur_image = cv.GaussianBlur(img, (3,3), 0)
        blur_image = self.sharpen_image(blur_image)
        resize_img = cv.resize(blur_image, (1200,1800))
        print("OCR working.....")
        result = self.table_engine(resize_img)
        for line in result:
            line.pop('img')
        li = []
        for i in result[0]['res']:
            li.append(i)
        
        print(li)
        