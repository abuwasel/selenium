import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # create a webdriver window and open it
driver.get('https://demoqa.com/checkbox')  # open this url / site

home_checkbox = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > span > button > svg')
home_checkbox.click()

documents_checkbox = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(2) > span > button > svg')
documents_checkbox.click()

workspace_checkbox = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > button > svg')
workspace_checkbox.click()

react_checkbox = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox')
react_checkbox.click()

veu_checkbox = driver.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(3) > span')
veu_checkbox.click()

checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]') # This finds elements in all the page
#checkboxes = driver.find_elements(By.XPATH, '//li[@class="rct-node rct-node-parent rct-node-expanded"]//input[@type="checkbox"]')
# This finds elements within a class on the page

for checkbox in checkboxes:
    if checkbox.is_selected():
        print("True")
    else:
        print("False")

driver.save_screenshot('checkbox.png')

time.sleep(2)
