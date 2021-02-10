from selenium import webdriver
from modulo_02.browsing import get_chrome_path

driver = webdriver.Chrome(executable_path=get_chrome_path())
driver.get('https://www.google.com/')
print(f'Current Title: {driver.title}')
print(f'Current Cache: {driver.application_cache}')
print(f'Current Cookies: {driver.get_cookies()}')
if "SOCzOAOac8uhByk5ZGU2Zg==" in driver.page_source:
    print("Found")
driver.get('https://www.mlb.com/es')
print(f'Current Title: {driver.title}')
print(f'Current url: {driver.current_url}')
print(f'Current source: {driver.page_source}')
driver.get('https://www.nytimes.com/es/')
driver.refresh()
print(f'Current Title: {driver.title}')
print(f'Current url: {driver.current_url}')
driver.back()
driver.back()
print(f'Current Title: {driver.title}')
print(f'Current url: {driver.current_url}')
driver.quit()


