from seleniumwire import webdriver
import time

# replace 'user:pass@ip:port' with your information
options = {
	'proxy': {
		'http': 'http://CcqTJb:fskuRH@103.74.76.130:8000',
		'https': 'https://CcqTJb:fskuRH@103.74.76.130:8000',
		'no_proxy': 'localhost,127.0.0.1'
	}
}

# replace 'your_absolute_path' with your chrome binary's aboslute path
driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\PROXY\\chromedriver\\chromedriver.exe', seleniumwire_options=options)

driver.get('https://instagram.com')

time.sleep(30)

driver.quit()