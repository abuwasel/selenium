import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # create a webdriver window and open it
driver.get('  https://demo.applitools.com/')  # open this url / site

username = driver.find_element(By.CSS_SELECTOR, '#username')
username.send_keys('ibrahim')

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('123456')

time.sleep(2)
log_in_button = driver.find_element(By.CSS_SELECTOR, '#log-in')
log_in_button.click()

total_balance = driver.find_element(By.CSS_SELECTOR, 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)').text
due_today = driver.find_element(By.CSS_SELECTOR, 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(3) > div.balance-value.danger').text

#Remove the $ symbol
new_total_balance = int(total_balance.replace("$", "")) - int(due_today.replace("$", ""))

if new_total_balance >= 0:
    print(f'Your Current Balance is in plus: {new_total_balance}')
else:
    print(f'Your Current Balance is in minus: {new_total_balance}')


time.sleep(2)
