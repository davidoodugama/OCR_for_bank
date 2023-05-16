import cv2 as cv
from PIL import Image, ImageOps
from paddleocr import PPStructure, draw_structure_result, save_structure_res, PaddleOCR
from matplotlib import pyplot as plt
import numpy as np
import os
from .Const import (IMAGE_FOLDER, IMAGE_NAME)

class OCR:
    def __init__(self, image_name):
        self.image_path = IMAGE_NAME + image_name + ".jpg"
        self.ocr = PaddleOCR(use_gpu=True, show_log = False)
        # self.table_engine = PPStructure(show_log = False)
        os.makedirs(IMAGE_FOLDER, exist_ok=True)

    def sharpen_image(self, image):
        # gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # blurred = cv.GaussianBlur(gray_img, (3, 3), 1)
        blurred_1 = cv.GaussianBlur(image, (0, 0), 3)
        sharpened_1 = cv.addWeighted(image, 1.1, blurred_1, -0.6, 40)
        # sharpened = cv.subtract(gray_img, blurred)
        # result = cv.addWeighted(image, 1.5, cv.cvtColor(sharpened, cv.COLOR_GRAY2BGR), -0.5, 0)
        # gray_img = cv.cvtColor(sharpened, cv.COLOR_BGR2GRAY)
        return sharpened_1

    def store_image(self, image):
        if os.path.exists(self.image_path):
            os.remove(self.image_path)
        print("Writing to file in progress......")
        cv.imwrite(self.image_path, image)
    
    def read_image(self):
        # Load the image
        img = cv.imread(self.image_path)
        # img = self.sharpen_image(img)

        # Apply Gaussian blur to reduce noise (optional)
        blur_image = cv.GaussianBlur(img, (3, 3), 3)

        # Convert the image to grayscale
        gray = cv.cvtColor(blur_image, cv.COLOR_BGR2GRAY)
        
        binary = cv.adaptiveThreshold(gray, 0, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 15, 5)

        # Apply image sharpening to the binary image
        kernel = np.array([[1, -1, 0], [-1, 5, -1], [0, -1, 5]], dtype=np.float32)
        sharpened = cv.filter2D(binary, -1, kernel)

        # Merge the sharpened image with the original image
        result = cv.bitwise_or(img, cv.cvtColor(sharpened, cv.COLOR_GRAY2BGR))
        # kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    
        # # Apply the sharpening filter
        # sharpened_image = cv.filter2D(resize_img, -1, kernel)
        res = self.sharpen_image(result)
        cv.imshow('resize_img', result)
        cv.imshow('res', res)
        cv.waitKey(0)
        cv.destroyAllWindows()
        
        # print("OCR working.....")
        # li = []
        # result = self.ocr.ocr(res)
        # for line in result[0]:
        #     text = line[1][0]
        #     bbox = line[0]
        #     li.append(text)
        
        # registration_no = li[8]
        # chassis_No = li[9]
        # current_owner_address = li[12] + " " + li[13]
        # condition_special_notes = li[15]
        # print(li)
        # absolute_owner = li[]
        