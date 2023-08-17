import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def init_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def handle_element(driver, selector, value=0):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    if value:
        element.send_keys(value)
    else:
        element.click()

def get_items_as_number(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector).text
    return float(element.replace("$", ""))

def check_balance(total_balance, due_today=0):
    # Check if the balance is plus or minus
    new_total_balance = total_balance - due_today
    if new_total_balance >= 0:
        print(f'Your Current Balance is in plus: {new_total_balance}')
    else:
        print(f'Your Current Balance is in minus: {new_total_balance}')
