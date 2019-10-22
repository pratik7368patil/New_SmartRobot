from selenium import webdriver
import time

url = "https://www.redbus.in/"
driver = webdriver.Chrome()
driver.get(url)
s_city = driver.find_element_by_id('src').send_keys('Malkapur')
time.sleep(5)
d_city = driver.find_element_by_id('dest').send_keys('Pune')
time.sleep(5)
dr = driver.find_element_by_id('onward_cal')
dr.send_keys('23112019')

