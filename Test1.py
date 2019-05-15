from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')


driver.set_page_load_timeout(10)
driver.get('http://google.com')
driver.find_element_by_name('q').send_keys('Selenium')

    
time.sleep(4)
driver.quit()

