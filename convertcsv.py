import csv
import random
import time
import os
print(os.environ['PATH'])
from selenium import webdriver

 
from selenium import webdriver
 
with open('out80-100(0).csv', 'w', newline='') as log:
    logwriter = csv.writer(log)
 
    with open('80-100(0).csv', newline='') as infile:
        records = csv.reader(infile)
 
        for r in records:
            log_row = r.copy()
            print('Start fetching URL to', r[2], r[3], 'filed on', r[4], '...')
            start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
 
            driver = webdriver.Chrome('/Users/lucy/Downloads/chromedriver')
 
            try:
                driver.get(r[5])
                time.sleep(3 + random.random() * 3)
                filing_date = driver.find_element_by_xpath('//*[@id="formDiv"]/div[2]/div[1]/div[2]').text
                period_of_report = driver.find_element_by_xpath('//*[@id="formDiv"]/div[2]/div[2]/div[2]').text
                form_text = driver.find_element_by_xpath('//*[@id="formDiv"]/div/table/tbody/tr[2]/td[3]/a').text
                form_link = driver.find_element_by_link_text(form_text).get_attribute('href')
                end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                print('Success!', start_time, ' --> ', end_time, '\n')
                log_row = log_row + [start_time, end_time, filing_date, period_of_report, form_link]
 
            except:
                end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                print('Error!', start_time, ' --> ', end_time, '\n')
                log_row = log_row + [start_time, end_time, 'ERROR!']
 
            driver.quit()
 
            logwriter.writerow(log_row)