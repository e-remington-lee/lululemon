'''
Web bot with basic inputs
'''
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
import ssl
import time


class WebBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        ssl._create_default_https_context = ssl._create_unverified_context

 
    def next_page(self, xpath):
        btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        btn.click()

    def create_browsers(self):
        return self.driver, WebDriverWait(self.driver, 10)
