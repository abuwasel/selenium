from selenium_functions import *

url = 'https://demo.applitools.com/'
selectors = {'username':'#username',
             'password':'#password',
             'login':'#log-in',
             'total_balance':'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)',
             'due_today':'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(3) > div.balance-value.danger',
             }

driver = init_driver(url)

handle_element(driver, selectors['username'], 'ibrahim')
handle_element(driver, selectors['password'], '123456')
handle_element(driver, selectors['login'])

time.sleep(2)

total_balance = get_items_as_number(driver, selectors['total_balance'])
due_today = get_items_as_number(driver, selectors['due_today'])

check_balance(total_balance, due_today)

time.sleep(2)
