"""Souce Lab login demo"""
from selenium.webdriver.remote.webelement import WebElement

from common.webdriver_factory import get_driver
#Importar la libreria de wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#definir script o secuencia de codigo

def login(wait: WebDriverWait, user: str, secret: str):
    """Login soucelab"""

    #user_id: user-name
    #clear()
    #send_keys()
    user_locator = (By.ID, 'user-name')
    #Hay que elegir el metodo de espera
    user_element = wait.until(EC.element_to_be_clickable(user_locator))
    #Presence - Exita en el DOM, no garantiza visibilidad
    #Visibility - Exista en DOM, n garantiza este visible
    #clickable - Visible y se pueda dar click
    user_element.clear()
    user_element.send_keys(user)

    #password_id: password
    #clear()
    #send_keys()
    password_locator = (By.ID, 'password')
    password = wait.until(EC.element_to_be_clickable(password_locator))
    password.clear()
    password.send_keys(secret)

    #login_id: login-button
    login_locator = (By.ID, 'login-button')
    login_element = wait.until(EC.element_to_be_clickable(login_locator))
    login_element.click()

def get_catalog_info(wait):
    """get catalogo information"""
    products_locator = (By.CLASS_NAME, 'inventory_item')
    products = wait.until(EC.visibility_of_all_elements_located(products_locator))
    result = []
    for product in products:
        product: WebElement
        name = product.find_element_by_class_name('inventory_item_name')
        price = product.find_element_by_class_name('inventory_item_price')
        result.append(f'Name: {name.text}, Price: {price.text}')
    return result

if __name__ == '__main__':
    # Primer paso definir el driver de selenium
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('http://saucedemo.com/index.html')

    login(wait, 'standard_user', 'secret_sauce')

    get_catalog_info(wait)

    driver.quit()