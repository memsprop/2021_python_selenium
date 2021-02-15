from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2'
           'Fmail%2F&ltmpl=default&dsh=S-754881558%3A1613063574131574&gmb=exp&biz=false&flowName='
           'GlifWebSignIn&flowEntry=SignUp')

my_name = driver.find_element_by_id('firstName')
my_name.clear()
my_name.send_keys('Guillermo')

my_last_name = driver.find_element_by_id('lastName')
my_last_name.clear()
my_last_name.send_keys('Aranda')

my_user = driver.find_element_by_id('username')
my_user.clear()
my_user.send_keys('LDORK')

my_pass = driver.find_element_by_name('Passwd')
my_pass.clear()
my_pass.send_keys('miPassword')

my_pass_conf = driver.find_element_by_name('ConfirmPasswd')
my_pass_conf.clear()
my_pass_conf.send_keys('miPassword')

nxt = driver.find_element_by_class_name('VfPpkd-RLmnJb')
nxt.click()
