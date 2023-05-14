"""
# LOG CLASS
# @author David Oodugama
# @email davidoodugama1999@gmail.com
# @version v1.0 2023-May
"""

from logging import Formatter, getLogger, DEBUG, FileHandler
from os import path, mkdir
from .Const import MAIN_LOG_PATH, FORMATTER, USE_OWN_LOGS, LOG_FILE_NAME

class Logger():
    def __init__(self):
        self.formatter = Formatter(FORMATTER)
        self.logger = None
        self.file_handler_debug = None
        self.file_handler_error = None
        self.error_logger = None
        self.use_own_logs = USE_OWN_LOGS
        if self.use_own_logs == True:
            if path.exists(MAIN_LOG_PATH) == False: # MAIN LOG FOLDER
                mkdir(MAIN_LOG_PATH)
        
    def debug(self, log_name, msg):
        self.logger = getLogger(log_name)
        self.logger.setLevel(DEBUG)
        self.file_handler_debug = FileHandler(LOG_FILE_NAME) # AUDIT LOG FILE PATH
        self.file_handler_debug.setFormatter(self.formatter)
        if (self.logger.hasHandlers()):
            self.logger.handlers.clear()
        self.logger.addHandler(self.file_handler_debug)
        self.logger.debug(msg)
        