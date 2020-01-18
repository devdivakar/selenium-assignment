
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time


driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.facebook.com/")

email = driver.find_element_by_name('email')
password = driver.find_element_by_name('pass')
email.send_keys("username")
password.send_keys('password')
button = driver.find_element_by_id('loginbutton')
button.click()
