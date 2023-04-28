"""import os
import logging
from logging.handlers import TimedRotatingFileHandler

from datetime import datetime


class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    
    def get_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        log_file_name = datetime.now().strftime("log_%Y%m%d_%H%M%S.log")
        file_handler = logging.FileHandler(os.path.join(os.getcwd(), "Logs", log_file_name))
        file_handler.setFormatter(self.formatter)
        logger.addHandler(file_handler)
        return logger

    def check_log_directory(self):
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        if not os.path.exists(self.archive_directory):
            os.makedirs(self.archive_directory)

    def get_handler(self, level):
        file_name = f"{os.path.join(self.log_directory, level)}.log"
        handler = TimedRotatingFileHandler(file_name, when='midnight', backupCount=10)
        handler.setLevel(self.log_level)
        handler.setFormatter(self.formatter)
        return handler

    def add_handlers(self):
        self.logger.addHandler(self.get_handler('info'))
        self.logger.addHandler(self.get_handler('warn'))
        self.logger.addHandler(self.get_handler('error'))

    def move_logs_to_archive(self):
        logs = [f for f in os.listdir(self.log_directory) if f.endswith('.log')]
        logs.sort(reverse=True)
        for i in range(10, len(logs)):
            old_file = os.path.join(self.log_directory, logs[i])
            new_file = os.path.join(self.archive_directory, logs[i])
            os.rename(old_file, new_file)

    def log_info(self, message):
        self.logger.info(message)

    def log_warn(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        self.log_directory = os.path.join(os.getcwd(), "Logs")
        self.archive_directory = os.path.join(os.getcwd(), "Archive")

        # check if Logs and Archive directory exists, if not create them
        self.check_log_directory()

        # add file handlers for different log levels
        self.add_handlers()

    def get_logger(self):
        logger = logging.getLogger('SpotifyTestAutomation')
        logger.setLevel(logging.DEBUG)
        file_name = datetime.now().strftime("SpotifyTestAutomation.log")
        file_handler = logging.FileHandler(os.path.join(self.log_directory, file_name))
        file_handler.setFormatter(self.formatter)
        logger.addHandler(file_handler)
        return logger

    def check_log_directory(self):
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        if not os.path.exists(self.archive_directory):
            os.makedirs(self.archive_directory)

    def get_handler(self, level):
        file_name = f"{os.path.join(self.log_directory, 'SpotifyTestAutomation.log')}"
        handler = TimedRotatingFileHandler(file_name, when='midnight', backupCount=10)
        handler.setLevel(level)
        handler.setFormatter(self.formatter)
        return handler

    def add_handlers(self):
        self.logger.addHandler(self.get_handler(logging.INFO))
        self.logger.addHandler(self.get_handler(logging.WARNING))
        self.logger.addHandler(self.get_handler(logging.ERROR))

    def move_logs_to_archive(self):
        logs = [f for f in os.listdir(self.log_directory) if f.endswith('.log')]
        logs.sort(reverse=True)
        for i in range(10, len(logs)):
            old_file = os.path.join(self.log_directory, logs[i])
            new_file = os.path.join(self.archive_directory, logs[i])
            os.rename(old_file, new_file)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
