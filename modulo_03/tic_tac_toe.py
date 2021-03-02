"""TicTac"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

def winner(wait):
    # XPATH //div[contains(@class, 'restart')]
    try:
        locator = (By.XPATH, "//div[contains(@class, 'restart')]")
        element = wait.until(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False

def select_empty_box(wait):
    #XPATH //div[contains(@class, 'square)]
    try:
        locator = (By.CSS_SELECTOR, ".square")
        elements = wait.until(EC.visibility_of_all_elements_located(locator))
        # Iterar los elementos
        # por cada elemento obtener su hijo div y verificar su contenido  class
        #si lass es none, esta vacio
        empty = []
        for box in elements:
            box: WebElement
            cell = box.find_element_by_tag_name('div')
            if not cell.get_attribute('class'):
                empty.append(box)
            print(f'Total empty boxes: {len(empty)}')
        target = random.choice(empty)
        target: WebElement
        target.click()
    except TimeoutException as exception:
        raise RuntimeError(f'No empty boxes {exception}')

def print_game_stats(wait):
    # player 1 XPATH //p[contains(@class, 'player1')]/span[@class='score']
    player_1_locator = (By.CSS_SELECTOR, '.player1 .score')
    player_1 = wait.until(EC.visibility_of_element_located(player_1_locator))
    # ties 1 XPATH //p[contains(@class, 'ties')]/span[@class='score']
    player_ties_locator = (By.XPATH, "//p[contains(@class, 'ties')]/span[@class='score']")
    player_ties = wait.until(EC.visibility_of_element_located(player_1_locator))
    # player 2 XPATH //p[contains(@class, 'player2')]/span[@class='score']
    player_2_locator = (By.CSS_SELECTOR, '.player2 .score')
    player_2 = wait.until(EC.visibility_of_element_located(player_2_locator))
    print(f'Player1: {player_1.text}, Ties: {player_ties.text}, Computer: {player_2.text}')

if __name__ == '__main__':
    # search users
    driver = get_driver('chrome')
    my_wait = WebDriverWait(driver, 1)
    driver.get('https://playtictactoe.org/')

    while not winner(my_wait):
        select_empty_box(my_wait)

    print_game_stats(my_wait)
    #whileNotWinner
    #Select random box
    #print game stats