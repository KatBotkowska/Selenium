from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
#driver = webdriver.Firefox()
#driver = webdriver.Ie()

driver.set_page_load_timeout(10)
driver.get('http://google.com')
driver.find_element_by_name('q').send_keys('Automation step by step')
driver.find_element_by_name('btnK').click()

time.sleep(4)
driver.quit()

'''from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')
driver.get('https://www.luxmed.pl')
title = driver.title
print(title)
assert 'Grupa LUX MED - prywatna opieka medyczna'  == title
driver.quit()'''

