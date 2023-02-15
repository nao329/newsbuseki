from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import csv

options = Options()
options.add_argument('--headless')
url = 'https://www.cnn.co.jp/archives/'
path='C:\\Users\\naoya\\Documents\\web_driver\\chromedriver'
URL = url
csv_file_name = 'ccnNews' + '.csv'

driver = webdriver.Chrome(path, options=options)
driver.get(URL)

f=open(csv_file_name, "w", encoding='cp932', errors='ignore')

writer = csv.writer(f, lineterminator='\n')
csv_header = ['id','日付', 'タイトル']
writer.writerow(csv_header)

i = 1
item=1
while True:
    i = i+1
    sleep(10)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.find_element_by_css_selector(".module--footer > p:nth-child(1)").click()
    for elem_li in driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/div[1]/section[1]/div[1]/ul/li'):
        elem_a = elem_li.find_element_by_xpath('./a[2]')
        elem_time = elem_li.find_element_by_class_name('txt-time')
        # elem_jan = elem_li.find_element_by_xpath('./dl/dd/span/a')
        csvlist = []
        csvlist.append(str(item))
        csvlist.append(elem_time.text)
        # csvlist.append(elem_jan.text)
        csvlist.append(elem_a.text)
        writer.writerow(csvlist)
        item = item + 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.get(f'https://www.cnn.co.jp/archives/{i}/')
    if i > 6:
        break
f.close()