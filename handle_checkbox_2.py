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


time.sleep(5)
