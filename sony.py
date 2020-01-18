from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.sonyliv.com/l")

#I am leaving this. this streaming portal is quite slow.