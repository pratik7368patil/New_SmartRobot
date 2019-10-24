from queue import Empty
from selenium import webdriver
import time
from datetime import date
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.redbus.in/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(1)
s_city = driver.find_element_by_id('src').send_keys('Aurangabad')
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
u_mm = "October"
mm = x.strftime("%B")
_u_mm = month_to_number(u_mm)
_mm = month_to_number(mm)
dd = '30'
flag = _u_mm - _mm

while flag > 0:
    try:
        d = driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td[@class='next']").click()
        flag -= 1
    except:
        raise Empty("Please provide valid month")

driver.find_element_by_xpath("//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td[text()=" + dd + "]").click()
driver.find_element_by_xpath("//button[@id='search_btn']").click()
time.sleep(10)
p = driver.find_element_by_xpath("//div[text()='View Buses']")
if p:
    p.click()

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
info = soup.find_all('div', attrs={'class': 'clearfix row-one'})
print(len(info))
name_ = []
tpe_ = []
price_ = []
for a in info:
    name = a.find('div', attrs={'class': 'travels lh-24 f-bold d-color'})
    name_.append(name.text)
    tpe = a.find('div', attrs={'class': 'bus-type f-12 m-top-16 l-color'})
    tpe_.append(tpe.text)
    price = a.find('div', attrs={'class': 'seat-fare'})
    price_with_text = price.text
    price_without_text = res = [int(i) for i in price_with_text.split() if i.isdigit()]
    price_.append(price_without_text[0])

df = pd.DataFrame({'Travels Name': name_, 'Bus Type': tpe_, 'Price': price_})
df.to_csv('products.csv', index=False, encoding='utf-8')

driver.close()

csv_data = pd.read_csv('products.csv')
all_ele = []
for row in csv_data.index:
    all_ele.append(csv_data['Price'][row])

all_ele_len = len(all_ele)
average_price = sum(all_ele)/all_ele_len
print(average_price)