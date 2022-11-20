from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from auth_data import username, password
import time
#from selenium import webdriver

# replace 'user:pass@ip:port' with your information
options = {
	'proxy': {
		'http': 'http://FJ0mfH:7UDSfj@194.62.66.183:8000',
		'https': 'https://FJ0mfH:7UDSfj@194.62.66.183:8000',
		'no_proxy': 'localhost,127.0.0.1'
	}
}

driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\PROXY\\chromedriver\\chromedriver.exe', seleniumwire_options=options)
#driver.get('https://instagram.com')

#service = Service(executable_path="C:\\Users\\user\\Desktop\\InstaBot\\chromedriver\\chromedriver.exe")
#driver = webdriver.Chrome(service=service)

try:
	driver.get("https://instagram.com")
	time.sleep(40)
	text_box = driver.find_element(by=By.NAME, value ="username")
	text_box.clear()
	text_box.send_keys(username)
	time.sleep(2)

	text_box = driver.find_element(by=By.NAME, value ="password")
	text_box.clear()
	text_box.send_keys(password + Keys.ENTER)
	time.sleep(40)


except Exception as ex:
	print(ex)


# replace 'your_absolute_path' with your chrome binary's aboslute path
#driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\PROXY\\chromedriver\\chromedriver.exe', seleniumwire_options=options)
#driver.get('https://instagram.com')
#time.sleep(60)
#driver.quit()