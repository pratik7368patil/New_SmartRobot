from queue import Empty
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from datetime import date

url = "https://www.redbus.in/"
driver = webdriver.Chrome()
driver.get(url)
s_city = driver.find_element_by_id('src').send_keys('Malkapur')
time.sleep(5)
d_city = driver.find_element_by_id('dest').send_keys('Pune')
time.sleep(5)
dr = driver.find_element_by_id('onward_cal').send_keys('0')


def month_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')


x = date.today()
u_mm = "November"
mm = x.strftime("%B")
_u_mm = month_to_number(u_mm)
_mm = month_to_number(mm)
dd = '23'
flag = _u_mm - _mm

while flag > 0:
    try:
        d = driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td[@class='next']").click()
        flag -= 1
    except:
        raise Empty("Please provide valid month")

driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td[text()=" + dd + "]").click()
driver.find_element_by_xpath("//button[@id='search_btn']").click()
