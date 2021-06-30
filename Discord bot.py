from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
import random


mypath = "D:\Coding_Programs\_01 Python\PythonWork5thSemester\Images"
images = []
listdir = os.listdir(mypath)
for files in listdir:
	images.append(files)


path = "D:\Coding_Programs\_01 Python\PythonWork5thSemester\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9515')
driver = webdriver.Chrome(executable_path=path, options=chrome_options)
channel = ["743840243094126702"]

def login_discord(token):
	time.sleep(2)
	driver.execute_script('setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"' + token.strip() +'"`}, 50);setTimeout(() => {location.reload();}, 2500)')
	time.sleep(10)
	try:
		driver.find_element_by_xpath('//*[@class="qrCodeOverlay-qgtlTP"]')
		return 2
	except:
		pass
	return 1

def addAvatar(i):
	try:
		driver.find_elements_by_xpath('//*[@class="button-14-BFJ enabled-2cQ-u7 button-38aScr lookBlank-3eh9lL colorBrand-3pXr91 grow-q77ONN"]')[2].click()
		time.sleep(4)
		conf = 3
		try:
			driver.find_element_by_xpath('//*[@class="fileInput-23-d-3"]').send_keys('C:/Users/Spiros/Desktop/Discord Avatar/avatar/' + random.choice(images))
		except:
			driver.execute_script("document.getElementsByClassName('userInfoViewingButton-2GlDif button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN')[0].click()")
			time.sleep(1.5)
			driver.find_element_by_xpath('//*[@class="fileInput-23-d-3"]').send_keys('C:/Users/Spiros/Desktop/Discord Avatar/avatar/' + random.choice(images))
			conf = 2
		time.sleep(2)
		try:
			driver.execute_script('document.getElementsByClassName("button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN")[' + str(conf) + '].click()')
		except:
			time.sleep(4)
			driver.execute_script('document.getElementsByClassName("button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN")[' + str(conf) + '].click()')

		time.sleep(3)
		if conf == 2:
			driver.execute_script("document.getElementsByClassName('button-38aScr lookFilled-1Gx00P colorGreen-29iAKY sizeSmall-2cSMqn grow-q77ONN')[0].click()")
		else:
			driver.execute_script('document.getElementsByClassName("contents-18-Yxp")[15].click()')
		time.sleep(4)
	except:
		pass

def logout_discord():
	driver.execute_script('document.getElementsByClassName("sidebar-CFHs9e")[0].scrollTo(0, 500000)')
	time.sleep(4)
	buttons_logout = driver.execute_script('return document.getElementsByClassName("item-PXvHYJ")')
	driver.execute_script('document.getElementsByClassName("item-PXvHYJ")['+ str(len(buttons_logout) - 1) +'].click()')
	time.sleep(4)
	driver.find_element_by_xpath('//*[@class="button-38aScr lookFilled-1Gx00P colorRed-1TFJan sizeMedium-1AC_Sl grow-q77ONN"]').click()
	time.sleep(4)
	return 1


def clear_browser():
	driver.get('chrome://settings/clearBrowserData')
	time.sleep(3)
	btn='//*[@id="clearBrowsingDataConfirm"]'
	clear_data=driver.execute_script("return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
	ActionChains(driver).move_to_element(clear_data).click(clear_data).perform()
	time.sleep(5)
	driver.get('https://discord.com/login')
	time.sleep(3)


file_accounts = open('data/tokens.txt', 'r', encoding='UTF-8')
tokens = file_accounts.readlines()
file_accounts.close()


def solve():
	driver.get('https://discord.com/login')
	i = 0 # final tab has id 9 to tab that will popup will be 10
	for token in tokens:
		print(token.strip() + ' ID : ' + str((i+1)))
		clear_browser()
		time.sleep(1)
		if login_discord(token.strip()) == 1:
			print('[LOGIN] Success...')
			time.sleep(5)
			addAvatar(i)
			#logout_discord()
			i += 1
		else:
			print('[LOGIN] Bad....')
			i += 1



if __name__ == '__main__':
	solve()
