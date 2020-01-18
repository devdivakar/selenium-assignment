from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://changegod.com/greenseed_yt_test47.html")
iframe = driver.find_elements_by_tag_name('iframe')[0]
time.sleep(5)
iframe.click()

