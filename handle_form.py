import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')

userName = driver.find_element(By.CSS_SELECTOR, '#userName')
userName.send_keys('Ibrahim')
userEmail = driver.find_element(By.CSS_SELECTOR, '#userEmail')
userEmail.send_keys('ibra@gmail.com')
currentAddress = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
currentAddress.send_keys('Kfar Qara')
permanentAddress = driver.find_element(By.CSS_SELECTOR, '#permanentAddress')
permanentAddress.send_keys('italy')

submit_button = driver.find_element(By.CSS_SELECTOR, '#submit')
submit_button.click()

time.sleep(5)



