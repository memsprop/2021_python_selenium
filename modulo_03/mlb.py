from selenium.webdriver.remote.webelement import WebElement
from common.webdriver_factory import get_driver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def select_dropdown(wait: WebDriverWait, option: str):
    locator = (By.XPATH, "//select[contains(@class, 'p-dropdown__standings')]")
    element = wait.until(EC.element_to_be_clickable(locator))
    dropdown = Select(element)
    dropdown.select_by_value(option)


def select_standard(wait: WebDriverWait):
    locator = (By.XPATH, "//*[@data-value='standard']")
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()


def select_advance(wait: WebDriverWait):
    locator = (By.XPATH, "//*[@data-value='advanced']")
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()


def get_teams_info(wait: WebDriverWait) -> dict:
    locator = (By.XPATH, "//*[@class='responsive-datatable__scrollable']//tbody//tr")
    rows = wait.until(EC.visibility_of_all_elements_located(locator))
    info = []
    for row in rows:
        tmp = parse_team_row(row)
        info.append(tmp)
    return info


def parse_team_row(row: WebElement):
    info = []
    for cell in row.find_elements_by_tag_name('td'):
        info.append(cell.text)
    return info


#if __name__ == '__main__':
my_driver = get_driver('chrome')
my_wait = WebDriverWait(my_driver, 10)

    # Got to page
my_driver.get('https://www.mlb.com/es/standings')

    # Select league option.
select_dropdown(my_wait, 'league')

    # Select standard
select_standard(my_wait)

    # Select advance
select_advance(my_wait)

    # Get team info
teams = get_teams_info(my_wait)
print(teams)
for team in teams:
    print(' | '.join(team))
my_driver.quit()