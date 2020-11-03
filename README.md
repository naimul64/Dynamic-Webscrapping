# Dynamic-Webscrapping
Scrap a webpage using selenium and beautiful soup python

This scraps the site https://alteritsolutions.com/stock which contains two strips of data from DSE and CSE. 
This script search for 'loading' class to be disappeared. Then it strats scrapping from webpage. 

---
#myElem = WebDriverWait(driver, delay).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading")))
myElem = WebDriverWait(driver, delay).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[class^='loading']")))
Two lines of code. First line is not used and commented because it only waits for first 'loading' class to be disappeared. 
Later line waits for all 'loading' class to disappear.
