from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
import time 
from bs4 import BeautifulSoup
import pandas as pd
import schedule


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
		time.sleep(7)


        #data = pd.read_csv(('p_n.csv'), index_col=[0])

        # data.to_csv('p_n.csv')
		# print(data)
		# counter += 1


schedule.every(1).minutes.do(func)
while counter<4:
	schedule.run_pending()
	time.sleep(1)
