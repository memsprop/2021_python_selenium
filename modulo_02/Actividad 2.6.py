from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select
import datetime

forms_fields = ['Guillermo', 'Aranda', 'mems@hotmail.com', '133 Main St.', 'MX', '05/03/2021', 'Double Room ($160 USD)', '5']

driver = get_driver('chrome')
driver.get('https://formsmarts.com/form/axi?mode=h5')



my_name = driver.find_element_by_xpath('/html/body/div/form/input[6]')
my_name.clear()
my_name.send_keys(forms_fields[0])

my_last_name = driver.find_element_by_xpath('/html/body/div/form/input[7]')
my_last_name.clear()
my_last_name.send_keys(forms_fields[1])

my_email = driver.find_element_by_xpath('/html/body/div/form/input[8]')
my_email.clear()
my_email.send_keys(forms_fields[2])

my_address = driver.find_element_by_xpath('/html/body/div/form/textarea')
my_address.clear()
my_address.send_keys(forms_fields[3])

my_country = driver.find_element_by_xpath('/html/body/div/form/select')
dropdown = Select(my_country)
dropdown.select_by_value(forms_fields[4])

my_date = driver.find_element_by_xpath('/html/body/div/form/div[1]/input')
my_date.clear()
my_date.send_keys(forms_fields[5])

my_room = driver.find_element_by_xpath('/html/body/div/form/fieldset/label[2]/input')
my_room.click()

my_nights = driver.find_element_by_xpath('/html/body/div/form/input[9]')
my_nights.clear()
my_nights.send_keys(forms_fields[7])

nxt = driver.find_element_by_name('submit')
nxt.click()

out_name = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[1]/td')
out_last_name = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td')
out_email = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td')
out_address = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[4]/td')
out_country = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[5]/td')
out_date = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[6]/td')
out_room = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[7]/td')
out_nights = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[8]/td')

if out_country.text == 'Mexico':
    country = 'MX'

date_time_str = out_date.text
date_time_obj = datetime.datetime.strptime(date_time_str, '%A %B %d, %Y')
date_final = date_time_obj.strftime('%m/%d/%Y')


for fields in forms_fields:
    if fields in out_name.text:
        print(f'Name: {fields} -> {out_name.text}')
    elif fields in out_last_name.text:
        print(f'Last Name: {fields} -> {out_last_name.text}')
    elif fields in out_email.text:
        print(f'email: {fields} -> {out_email.text}')
    elif fields in out_address.text:
        print(f'Address: {fields} -> {out_address.text}')
    elif fields == country:
        print(f'Country: {fields} -> {country}')
    elif fields == date_final:
        print(f'Date: {fields} -> {date_final}')
    elif fields in out_room.text:
        print(f'Room Type: {fields} -> {out_room.text}')
    elif fields in out_nights.text:
        print(f'Number of Nights: {fields} -> {out_nights.text}')
    else:
        print('Form is not matching')

#driver.quit()