import time
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')

def open():
    driver.get('http://www.sgg.gov.ma/Legislation/BulletinsOfficielsAns.aspx')

latest_summary=[]
edition=[]
def latest():
    open()
    time.sleep(5)
    elem = driver.find_element_by_xpath('//tr[@class="dnnGridItem"]/td/p')
    edition.append(elem.text)
    link = driver.find_element_by_xpath('//tr[@class="dnnGridItem"]/td/p/a')
    driver.get(link.get_attribute('href'))
    time.sleep(5)
    heads = driver.find_elements_by_xpath('//span[contains(@style, "20px")]')
    for h in heads:
        latest_summary.append(h.text)

latest()