import configparser
import logging
import datetime
import os
import colorama

class Config:
    ini_path = os.path.join(os.path.dirname(__file__), "settings.ini")
    log_path = os.path.join(os.path.dirname(__file__), f"{datetime.date.today()}.log")
    logging_format = "%(asctime)s | %(levelname)s | %(message)s"

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(Config.ini_path, encoding='utf-8')
        if self.config['main_config']['debug'] == "True":
            self.logging_level = logging.DEBUG
        else:
            self.logging_level = logging.WARNING

    def logger(self):
        logging.basicConfig(filename=Config.log_path,
                            level=self.logging_level,
                            filemode="a",
                            format=Config.logging_format,
                            datefmt="%m.%d.%Y %H:%M:%S"
                            )
    
    def progress_bar(self, progress, total, color=colorama.Fore.YELLOW):
        percent = 100 * (progress / float(total))
        bar = '█' * int(percent) + '-' * (100 - int(percent))
        print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
        if progress == total:
            print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")
    
    def reset_progress_color(self):
        print(colorama.Fore.RESET)