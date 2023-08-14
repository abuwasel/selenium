import time

from selenium import webdriver

driver = webdriver.Chrome()  # create a webdriver window and open it
driver.get('https://www.google.com')  # open this url / site
driver.get('https://www.amazon.com')  # open this url / site

print(driver.title)
print(driver.name)
print(driver.current_url)
print(driver.get_network_conditions())
# driver.back()
# driver.forward()

#file = open('p1.png', 'b')


time.sleep(3)

