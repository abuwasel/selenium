import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # create a webdriver window and open it
driver.get('https://www.walla.co.il/')  # open this url / site

heading_1 = driver.find_element(By.CSS_SELECTOR, '#root > div > div > section.css-k7u0n.css-xqg1a5.drama-wide-wrapper.no-moible-padding > section > article > a > h2').text
summary = driver.find_element(By.CSS_SELECTOR, '#root > div > div > section.css-k7u0n.css-xqg1a5.drama-wide-wrapper.no-moible-padding > section > article > a > p').text

print(heading_1)
print(summary)

if 'ביטול' in heading_1:
    print('Yes')
else:
    print('No')

time.sleep(2)

