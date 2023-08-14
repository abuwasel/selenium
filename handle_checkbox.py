import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # create a webdriver window and open it
driver.get('https://demoqa.com/checkbox')  # open this url / site

home_checkbox = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > span')
driver.save_screenshot('before_click.png')
home_checkbox.click()
driver.save_screenshot('after_click.png')


time.sleep(5)
