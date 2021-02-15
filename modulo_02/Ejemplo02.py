from selenium import webdriver
from modulo_02.browsing import get_chrome_path


driver = webdriver.Chrome(executable_path=get_chrome_path())

driver.get('https://google.com')
gmail_link = driver.find_element_by_link_text('Gmail')
print(f'Gmail link is displayed: {gmail_link.is_displayed()}')
print(f'Gmail link is enabled: {gmail_link.is_enabled()}')
print(f'Gmail link is selected: {gmail_link.is_selected()}')
if gmail_link.is_enabled() and gmail_link.is_displayed():
    gmail_link.click()

driver.quit()