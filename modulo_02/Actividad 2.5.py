from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select

forms_fields = ['Guillermo', 'Aranda', 'mems@hotmail.com', 'Esto es una Prueba', 'Sales Inquiry']

driver = get_driver('chrome')
driver.get('https://formsmarts.com/html-form-example')

driver.switch_to.frame(driver.find_element_by_class_name('fs_embed'))

my_name = driver.find_element_by_xpath('/html/body/div/form/input[6]')
my_name.clear()
my_name.send_keys(forms_fields[0])

my_last_name = driver.find_element_by_xpath('/html/body/div/form/input[7]')
my_last_name.clear()
my_last_name.send_keys(forms_fields[1])

my_email = driver.find_element_by_xpath('/html/body/div/form/input[8]')
my_email.clear()
my_email.send_keys(forms_fields[2])

my_comment = driver.find_element_by_xpath('/html/body/div/form/textarea')
my_comment.clear()
my_comment.send_keys(forms_fields[3])

my_inquiry = driver.find_element_by_xpath('/html/body/div/form/select')
dropdown = Select(my_inquiry)
dropdown.select_by_value(forms_fields[4])

nxt = driver.find_element_by_name('submit')
nxt.click()

out_name = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[1]/td')
out_last_name = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td')
out_email = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td')
out_inquiry = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[5]/td')
out_subject_inquiry = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[4]/td')

for fields in forms_fields:
    if fields in out_name.text:
        print(f'Name: {fields} -> {out_name.text}')
    elif fields in out_last_name.text:
        print(f'Last Name: {fields} -> {out_last_name.text}')
    elif fields in out_email.text:
        print(f'email: {fields} -> {out_email.text}')
    elif fields in out_inquiry.text:
        print(f'Inquiry: {fields} -> {out_inquiry.text}')
    elif fields in out_subject_inquiry.text:
        print(f'Subject of Your Inquiry: {fields} -> {out_subject_inquiry.text}')
    else:
        print('Form is not matching')
driver.quit()