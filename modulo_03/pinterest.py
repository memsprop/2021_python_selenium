from selenium.webdriver.remote.webelement import WebElement
from common.webdriver_factory import get_driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def my_login(wait: WebDriverWait, user: str, password: str):
    locator = (By.XPATH, "//*[@data-test-id='simple-login-button']//button")
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()
    #email
    login_user = (By.ID, "email")
    email = wait.until(EC.element_to_be_clickable(login_user))
    email.clear()
    email.send_keys(user)
    #Password
    login_password = (By.ID, "password")
    passwd = wait.until(EC.element_to_be_clickable(login_password))
    passwd.clear()
    passwd.send_keys(password)
    #Login button
    submit_btn_locator = (By.XPATH, "//*[@data-test-id='registerFormSubmitButton']//button")
    submit_btn = wait.until(EC.element_to_be_clickable(submit_btn_locator))
    submit_btn.click()

def my_search(wait: WebDriverWait, my_search_word: str):
    search_bar_locator = (By.NAME, "searchBoxInput")
    search_bar = wait.until(EC.element_to_be_clickable(search_bar_locator))
    search_bar.clear()
    search_bar.send_keys(my_search_word)
    search_bar.send_keys(Keys.ENTER)

def get_improvements_info(wait: WebDriverWait):
    locator = (By.XPATH, "//*[@class='SearchImprovementsBar-InnerScrollContainer']//a")
    rows = wait.until(EC.visibility_of_all_elements_located(locator))
    info = []
    for element in rows:
        info.append(element.text)
    return info

def my_logout(wait: WebDriverWait):
    locator = (By.XPATH, "//*[@data-test-id='header-accounts-options-button']//button")
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()
    quit_btn_locator = (By.XPATH, "//*[@data-test-id='header-menu-options-logout']")
    quit_btn = wait.until(EC.element_to_be_clickable(quit_btn_locator))
    quit_btn.click()

def scrapper(wait: WebDriverWait):
    locator = (By.XPATH, "//*[@class='SearchImprovementsBar-InnerScrollContainer']//a")
    rows = wait.until(EC.visibility_of_all_elements_located(locator))
    #for element in rows:
    #   info.append(element.text)

my_driver = get_driver('chrome')
my_wait = WebDriverWait(my_driver, 10)

    # Got to page
my_driver.get('https://www.pinterest.com.mx/?autologin=true')

    # Select league option.

user = 'garanda@anexinet.com'
password = 'Pinterest.2021'
my_login(my_wait, user, password)
my_search(my_wait,'Selenium')
improvements = get_improvements_info(my_wait)
for improvement in improvements:
    print(f' | {improvement} |')

my_logout(my_wait)
my_driver.quit()
scrapper(my_wait)