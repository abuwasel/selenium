import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # create a webdriver window and open it
driver.get('https://demoqa.com/webtables')  # open this url / site

add_selector = driver.find_element(By.CSS_SELECTOR, '#addNewRecordButton')
add_selector.click()

firstName = driver.find_element(By.CSS_SELECTOR, '#firstName')
firstName.send_keys('Ibrahim')

lastName = driver.find_element(By.CSS_SELECTOR, '#lastName')
lastName.send_keys('Abu wasel')

userEmail = driver.find_element(By.CSS_SELECTOR, '#userEmail')
userEmail.send_keys('ibrahim@gmail.com')

age = driver.find_element(By.CSS_SELECTOR, '#age')
age.send_keys('40')

salary = driver.find_element(By.CSS_SELECTOR, '#salary')
salary.send_keys('8000')

department = driver.find_element(By.CSS_SELECTOR, '#department')
department.send_keys('Legal')

time.sleep(2)
add_selector_submit = driver.find_element(By.CSS_SELECTOR, '#submit')
add_selector_submit.click()

#--------Remove Item---------
# kierra_selector = driver.find_element(By.CSS_SELECTOR, '#delete-record-3 > svg > path')
# kierra_selector.click()

time.sleep(5)