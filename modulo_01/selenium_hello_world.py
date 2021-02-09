from selenium import webdriver

driver_path = '/drivers/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('QA Minds')
driver.quit()


