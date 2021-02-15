
"""Navigate selenium page."""
from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.get('https://www.selenium.dev/')

for link in ['Downloads', 'Projects', 'Support', 'Blog']:
    element = driver.find_element_by_link_text(link)
    print('-' * 80)
    print(f'Hyperlink text: {element.text}')
    print(f'Hyperlink displayed: {element.is_displayed()}')
    print(f'Hyperlink enabled: {element.is_enabled()}')
    print(f'Hyperlink selected: {element.is_selected()}')
    element.click()
    print(f"Selenium Count: {driver.page_source.count('Selenium')}")
driver.quit()
