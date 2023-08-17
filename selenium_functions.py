import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # create a webdriver window and open it
driver.get('https://demo.applitools.com/')  # open this url / site

selectors = {'username':'#username', 'password':'#password', 'login':'#log-in'}
def handle_element(driver, selector, value=0):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    if value:
        element.send_keys(value)
    else:
        element.click()

handle_element(driver, selectors['username'], 'ibrahim')
handle_element(driver, selectors['password'], '123456')
handle_element(driver, selectors['login'])

time.sleep(2)


total_balance = driver.find_element(By.CSS_SELECTOR, 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)').text
due_today = driver.find_element(By.CSS_SELECTOR, 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(3) > div.balance-value.danger').text

#Remove the $ symbol and convert the value from str to int
new_total_balance = int(total_balance.replace("$", "")) - int(due_today.replace("$", ""))




# Check if the balance is plus or minus
if new_total_balance >= 0:
    print(f'Your Current Balance is in plus: {new_total_balance}')
else:
    print(f'Your Current Balance is in minus: {new_total_balance}')


time.sleep(2)
