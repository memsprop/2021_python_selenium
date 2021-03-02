from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = get_driver('chrome')
driver.implicitly_wait(10)

driver.get('https://www.google.com/')
div_fst = driver.find_element_by_xpath("//body/div[1]")
div_lst = driver.find_element_by_xpath("//body/div[last()]")
#any_nav = driver.find_element_by_xpath("")
element_submit = driver.find_element_by_xpath("//*[@type='submit']")
print(f'Body child Div first elements {div_fst.text} \nLast element {div_lst.text} \n Type = Submit {element_submit.text}')


driver.quit()