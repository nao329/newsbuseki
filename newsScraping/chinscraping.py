from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import csv

options = Options()
options.add_argument('--headless')
url = 'http://j.people.com.cn/94765/index1.html'
path='C:\\Users\\naoya\\Documents\\web_driver\\chromedriver'
URL = url
csv_file_name = 'chineseNews' + '.csv'

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
    for elem_li in driver.find_elements_by_xpath('/html/body/div[5]/div[1]/div[3]/div'):
        elem_a = elem_li.find_element_by_xpath('./h3/a')
        elem_time = elem_li.find_element_by_xpath('./i')
        # elem_jan = elem_li.find_element_by_xpath('./dl/dd/span/a')
        csvlist = []
        csvlist.append(str(item))
        csvlist.append(elem_time.text)
        # csvlist.append(elem_jan.text)
        csvlist.append(elem_a.text)
        writer.writerow(csvlist)
        item = item + 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.get(f'http://j.people.com.cn/94765/index{i}.html')
    if i > 6:
        break
f.close()