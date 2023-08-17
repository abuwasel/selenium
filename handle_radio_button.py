import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # create a webdriver window and open it
driver.get('https://demoqa.com/radio-button')  # open this url / site

yes_selector = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(2) > label')
yes_selector.click()

time.sleep(3)