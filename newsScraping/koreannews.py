from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import csv

options = Options()
options.add_argument('--headless')
url = 'https://www.chosunonline.com/svc/list.html?date=20221208'
path='C:\\Users\\naoya\\Documents\\web_driver\\chromedriver'
URL = url
csv_file_name = 'koreanNews' + '.csv'

driver = webdriver.Chrome(path, options=options)
driver.get(URL)

f=open(csv_file_name, "w", encoding='cp932', errors='ignore')

writer = csv.writer(f, lineterminator='\n')
csv_header = ['id','日付', 'タイトル']
writer.writerow(csv_header)

i = 0
item=1
pn=1
while True:
    i = i+1
    sleep(10)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.find_element_by_css_selector(".module--footer > p:nth-child(1)").click()
    for elem_ul in driver.find_elements_by_xpath(f'/html/body/div/div[2]/div[1]/div/ul'):
        for elem_li in elem_ul.find_elements_by_xpath('./li'):
            elem_a = elem_li.find_element_by_xpath('./a')
            elem_time = elem_li.find_element_by_xpath('./span')
            # elem_jan = elem_li.find_element_by_xpath('./dl/dd/span/a')
            csvlist = []
            csvlist.append(str(item))
            csvlist.append(elem_time.text)
            # csvlist.append(elem_jan.text)
            csvlist.append(elem_a.text)
            writer.writerow(csvlist)
            item = item + 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if pn == 1:
        URL+=f'&pn={pn+1}'
        pn=2
        driver.get(URL)
    elif pn == 2:
        URL='https://www.chosunonline.com/svc/list.html?date=20221207'
        pn=1
        driver.get(URL)
    if i > 3:
        break
f.close()