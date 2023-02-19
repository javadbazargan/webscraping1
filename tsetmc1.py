from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
import time 
from bs4 import BeautifulSoup
import pandas as pd
import schedule

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import datetime
from typing import Text

counter = 0
payani_list = []
nav_list = []
data_i = pd.DataFrame({
		'nomad':[],
		'time':[],
		'payani':[],
		'nav':[]})

data_i.to_csv('p_n.csv')
#N =input("Please Enter Nomad's name :  ")
N = []
N = [item for item in input("Please Enter Nomad's name : ").split()]
print(N)

def func():
	global counter
	global N
	for n in N :
		url = 'http://tsetmc.ir/Loader.aspx?ParTree=15' 

		# options = webdriver.ChromeOptions()
		# options.headless = True 
		
		driver = webdriver.Chrome(service=ChromeService( 
			ChromeDriverManager().install())) 
		driver.get(url) 

		# driver=webdriver.Firefox()
		# driver.get(url)
		# window_before = driver.window_handles[0]
		# driver.switch_to_window(window_before)
		time.sleep(7)
		btn1 = driver.find_element('xpath','//*[@id="search"]')
		btn1.click()
		btn2 = driver.find_element('xpath','//*[@id="SearchKey"]')
		btn2.send_keys(n)
		time.sleep(10)

		
		WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".s750 > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)"))).click()
		time.sleep(14)
		
		
		soup = BeautifulSoup(driver.page_source , 'html.parser')


		data2 = pd.DataFrame({
			'nomad':[n],
			'time':[datetime.datetime.now()],
			'payani':[float((soup.find('span' , style = 'font-size:15px;font-weight:bold').text).replace(',' ,''))],
			'nav':[float((soup.find('td' , id = 'PRedTran').text).replace(',' ,''))]
			})
		data2['p/nav'] = data2['payani']/data2['nav']
		data = pd.read_csv(('p_n.csv'), index_col=[0])
		data = data.append(data2 ,ignore_index = True)
		
		
		data.to_csv('p_n.csv')
		print(data)
		counter += 1


schedule.every(1).minutes.do(func)
while counter<4:
	schedule.run_pending()
	time.sleep(1)
