"""Tiktok Get users"""
from selenium.webdriver.remote.webelement import WebElement
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def search_users(wait: WebDriverWait, search: str):
    search_locator = (By.NAME, 'q')
    search_element = wait.until(EC.element_to_be_clickable(search_locator))
    search_element: WebElement
    search_element.clear()
    search_element.send_keys(search)
    search_element.send_keys(Keys.ENTER)


def get_users(wait: WebDriverWait):
    user_locator = (By.XPATH, "//div[contains(@class, 'search')]/a")
    user_element = wait.until(EC.visibility_of_all_elements_located(user_locator))
    users_found = []
    for user in user_element:
        users_found.append(user.text.split('\n'))
    return users_found


if __name__ == '__main__':
    # search users
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.tiktok.com/?lang=es')
    #######################################
    search_word = 'python'
    search_users(wait, search_word)
    #print(get_users(wait))
    results = get_users(wait)
    #print(results)
    for result in results:
        print(' | '.join(result))
    driver.quit()
