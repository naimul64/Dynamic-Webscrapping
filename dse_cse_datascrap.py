import bs4 as bs
import urllib.request
import time
import csv
import os
# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
driver_dir = os.path.join(os.getcwd(),'chromedriver') 
driver = webdriver.Chrome(driver_dir, chrome_options=options)

source = urllib.request.urlopen('https://alteritsolutions.com/stock').read()





driver.get("https://alteritsolutions.com/stock")
delay = 300 # seconds
try:
    #myElem = WebDriverWait(driver, delay).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
    myElem = WebDriverWait(driver, delay).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[class^='loading']")))

    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")


print ("\n\n-----------------------")
print (driver.page_source)


soup = bs.BeautifulSoup(driver.page_source,'lxml')








# FINDING DHK STOCK EXCHANGE DATA

dse = soup.find_all(id='dhk')

dse_spans = dse[0].find_all("span")
dse_data = []
for i in range(len(dse_spans)):
	list_row = []

	codes = dse_spans[i].find_all("code")
	
	string_prettified_span = dse_spans[i].prettify()

	list_row.append(string_prettified_span.splitlines()[1])
	list_row.append(codes[0].string)
	list_row.append(codes[1].string)

	dse_data.append(list_row)

print (dse_data)


# FINDING DHK STOCK EXCHANGE DATA

cse = soup.find_all(id='ctg')

cse_spans = cse[0].find_all("span")
cse_data = []
for i in range(len(cse_spans)):
	list_row = []

	codes = cse_spans[i].find("code")

	code_lines = codes.prettify().splitlines()
	del code_lines[0]
	del code_lines[-1]
	code_values = []
	for j in range(len(code_lines)):
		if (len(code_lines[j].strip()) != 0):
			code_values.append(code_lines[j].strip())

	
	string_prettified_span = cse_spans[i].prettify()

	list_row.append(string_prettified_span.splitlines()[1].strip())
	list_row.append(string_prettified_span.splitlines()[3].strip())

	list_row.append(code_values[0])
	list_row.append(code_values[1])

	cse_data.append(list_row)
print (cse_data)



#Write data to csv
with open('STOCK_EXCHANGE_DATA.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["DSE DATA"])
    for row in dse_data:
    	writer.writerow(row)

    writer.writerow(["CSE DATA"])
    for row in cse_data:
    	writer.writerow(row)