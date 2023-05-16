"""
# MAIN API CONNECTION

# @author David Oodugama
# @email davidoodugama1999@gmail.com
# @version v1.0 2023-May
"""
try:
    from flask import Flask, request, jsonify, make_response
    from flask_restful import Api, Resource, request
    from shutil import rmtree
    from Config.Const import MAIN, READ_IMAGE_OCR
    from Config.OCR import OCR
    import cv2 as cv
    from PIL import Image
    # from Const.Logger
    import numpy as np
    from werkzeug.utils import secure_filename
    
except Exception as e:
    from Config.Logger import Logger
    logger = Logger()
    logger.debug(MAIN, e)
    
application = Flask(__name__)
api = Api(application)


class readImage(Resource):
    def post(self):
        image_file = request.files['img']
        image_name = request.form['img_name']
        ocr = OCR(image_name)
        
        # Read the image using OpenCV
        image_array = np.frombuffer(image_file.read(), np.uint8)
        image_A = cv.imdecode(image_array, cv.IMREAD_COLOR)
        # image_b = ocr.sharpen_image(image_A)
        # Display the image
        # cv.imshow('image_a', image_A)
        # cv.imshow('image_B', image_b)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        ocr.store_image(image_A)
        ocr.read_image()
        

api.add_resource(readImage, READ_IMAGE_OCR)

if __name__ == "__main__":
    application.run(debug = True)