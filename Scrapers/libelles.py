from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:\Users\OTHMANE\Downloads\geckodriver-v0.29.0-win64\geckodriver.exe')


instruments=[]
def fetch():
    driver.get("http://www.casablanca-bourse.com/bourseweb/Liste-Societe.aspx?IdLink=20&Cat=7")
    for i in range(1,10):
        libels = driver.find_elements_by_xpath('//span[id="ListSocieteControl1_ListSociete1_RptrScCote_ctl0'+str(i)+'_Label2"]')
        for k in libels:
            instruments.append(k.text)
    for i in range(10,77):
        libels = driver.find_elements_by_xpath('//span[@id="ListSocieteControl1_ListSociete1_RptrScCote_ctl'+str(i)+'_Label2"]')
        for k in libels:
            instruments.append(k.text)
        libel2 = driver.find_elements_by_xpath('//span[@id="ListSocieteControl1_ListSociete1_RptrScCote_ctl'+str(i)+'_Label21"]')
        for k in libel2:
            instruments.append(k.text)
    instruments.sort()

fetch()