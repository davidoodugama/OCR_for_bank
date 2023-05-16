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
        blurred = cv.GaussianBlur(image, (3, 3), 1)
        sharpened = cv.addWeighted(image, 1.5, blurred, -0.5, 0)
        return sharpened

    def store_image(self, image):
        if os.path.exists(self.image_path):
            os.remove(self.image_path)
        print("Writing to file in progress......")
        cv.imwrite(self.image_path, image)
        # if os.path.exists(IMAGE_FOLDER + IMAGE_NAME + image_name):
        #     os.remove(IMAGE_FOLDER + IMAGE_NAME + image_name)
    
    def read_image(self):
        # img = cv.imread(self.image_path)
        # # blur_image = cv.GaussianBlur(img, (3,3), 0)
        # blur_image = self.sharpen_image(img)
        # resize_img = cv.resize(blur_image, (1200,1800))
        # gray = cv.cvtColor(resize_img, cv.COLOR_BGR2GRAY)

        # # Apply the Laplacian filter
        # laplacian = cv.Laplacian(gray, cv.CV_64F)

        # # Normalize the result to make it a valid image format
        # laplacian = np.uint8(np.absolute(laplacian))

        # # Combine the original image with the sharpened result
        # sharpened = cv.bitwise_or(resize_img, cv.cvtColor(laplacian, cv.COLOR_GRAY2BGR))
        img = cv.imread(self.image_path)
        
        # Resize the image for better processing speed (optional)
        resized_image = cv.resize(img, None, fx=0.5, fy=0.5)

        # Convert the image to grayscale
        gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise (optional)
        # blur_image = cv.GaussianBlur(img, (3, 3), 0)

        # Convert the image to grayscale
        # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # # Apply the Laplacian filter
        # laplacian = cv.Laplacian(gray, cv.CV_64F)

        # # Normalize the result to make it a valid image format
        # laplacian = np.uint8(np.absolute(laplacian))

        # # Convert the grayscale image to BGR
        # gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

        # # Combine the original image with the sharpened result
        # sharpened = cv.bitwise_or(img, gray_bgr)

        # # Resize the final sharpened image
        # resize_img = cv.resize(sharpened, (1200, 1800))
        
        
        ## Good ##
        # Convert the image to grayscale
        # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the grayscale image
        # blurred = cv.GaussianBlur(gray, (0, 0), 3)

        # Combine the masked image and the paper texture overlay
        # scanned_copy = cv.add(masked_image, papered_resized)
        
        # Merge the sharpened image with the original image
        # result = cv.addWeighted(img, 1.2, cv.cvtColor(sharpened, cv.COLOR_GRAY2BGR), -1.2, 2)
    
        res = self.sharpen_image(gray)
        # cv.imshow('result1', res)
        # cv.imshow('img', img)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        
        
        
        print("OCR working.....")
        result = self.ocr.ocr(res)
        print(result)
        for line in result[0]:
        
            text = line[1][0]
            bbox = line[0]
            print(line[1])
        # result = self.table_engine(img)
        # for line in result:
        #     line.pop('img')
        # li = []
        # for i in result[0]['res']:
        #     li.append(i)
        
        # for i in li:
        #     print(i['text'])
        