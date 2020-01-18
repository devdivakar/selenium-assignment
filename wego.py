
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time


driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.wego.co.in")


# function for getting the shadowelement
def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root


root1 = driver.find_element_by_id('app')
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element_by_tag_name('wego-search-form')
shadow_root2 = expand_shadow_element(root2)

root3 = shadow_root2.find_element_by_tag_name('wego-flight-search-form')
shadow_root3 = expand_shadow_element(root3)

root4 = shadow_root3.find_element_by_id('dep')
shadow_root4 = expand_shadow_element(root4)


dep = shadow_root4.find_element_by_id('searchKeywordInput')
dep.click()
time.sleep(2)
root5 = shadow_root4.find_element_by_tag_name('result-box')
shadow_root5 = expand_shadow_element(root5)
content_div = shadow_root5.find_element_by_class_name('content')
array_destinations = content_div.find_elements_by_xpath(".//*")
array_destinations[random.randint(0,len(array_destinations)-1)].click()

root4 = shadow_root3.find_element_by_id('arr')
shadow_root4 = expand_shadow_element(root4)
arr = shadow_root4.find_element_by_id('searchKeywordInput')
arr.click()
time.sleep(2)
root5 = shadow_root4.find_element_by_tag_name('result-box')
shadow_root5 = expand_shadow_element(root5)
content_div = shadow_root5.find_element_by_class_name('content')
array_arrivals = content_div.find_elements_by_xpath(".//*")
array_arrivals[random.randint(0,len(array_arrivals)-1)].click()

root4 = shadow_root3.find_element_by_id('dates')
shadow_root4 = expand_shadow_element(root4)
date_button = shadow_root4.find_element_by_tag_name('date-field')
date_button.click()
calendar_popup = shadow_root4.find_element_by_tag_name('calendar-popup')
calendar_popup = expand_shadow_element(calendar_popup).find_element_by_class_name('days')
dates =  calendar_popup.find_elements_by_xpath(".//*")
dates[random.randint(17,26)].click()
time.sleep(3)
root3 = shadow_root2.find_element_by_tag_name('wego-flight-search-form')
shadow_root3 = expand_shadow_element(root3)
search_button = shadow_root3.find_element_by_id('search').click()
time.sleep(5)




# <---Search Result Appears-->
root1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'app')))
shadow_root1 = expand_shadow_element(root1)

time.sleep(10)
root2 = shadow_root1.find_element_by_tag_name('wego-flight-results')
shadow_root2 = expand_shadow_element(root2)

time.sleep(10)
root3 = shadow_root2.find_element_by_tag_name('flight-result-list')
shadow_root3 = expand_shadow_element(root3)


#my internet is slow thats why I have used time.sleep() too much 
#I have not used Try blocks considering the time constraint