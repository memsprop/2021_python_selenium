
"""Login to facebook"""
from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://www.facebook.com/')

email = driver.find_element_by_id('email')
email.clear()
email.send_keys('my_user@email.com')

password = driver.find_element_by_id('pass')
password.clear()
password.send_keys('my_password')

login = driver.find_element_by_name('login')
login.click()

driver.quit()