from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = get_driver('chrome')
driver.implicitly_wait(10)

driver.get('https://www.amazon.com.mx/')
elements = driver.find_elements_by_xpath("//a")

print(f'Total of Elements with tag a = {len(elements)}')
for element in elements:
    print(element.text)

head_childs = driver.find_elements_by_xpath("//head/*")
print(f'Total of Head childs = {len(head_childs)}')

for child in head_childs:
    print(child.text)

driver.quit()