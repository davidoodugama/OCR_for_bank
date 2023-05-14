import os
from datetime import date
today = date.today() # CURRENT DATE
import time

"""LOG FILE PATHS"""
MAIN_LOG_PATH = "/Logs"
FORMATTER = '%(asctime)s|%(name)s|%(message)s'
USE_OWN_LOGS = True
LOG_FILE_NAME = MAIN_LOG_PATH + "/" + str(today) + "_audit.log"

"""MAIN"""
MAIN = "Main"

"""IMAGE SAVING PATH"""
IMAGE_FOLDER = "./Images/"
IMAGE_NAME = IMAGE_FOLDER + str(time.time()) + "_"

"""API URLS"""
READ_IMAGE_OCR = "/read_image"