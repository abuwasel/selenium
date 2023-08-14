import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # create a webdriver window and open it
driver.get('https://www.google.com')  # open this url / site

search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb')

search_box.send_keys('italy', Keys.ENTER)
#search_box.send_keys(Keys.ENTER)


time.sleep(3)
