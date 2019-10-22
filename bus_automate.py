from selenium import webdriver
import time

url = "https://www.redbus.in/"
driver = webdriver.Chrome()
driver.get(url)
des_city = driver.find_element_by_id('src').send_keys('Malkapur')
time.sleep(5)

