
#2001-03-28
#2000-12-31
#y45625kex13.txt


#This piece of codes extract Annual Report to Stockholders section of failed MDA documents 
#https://www.toolsqa.com/selenium-webdriver/find-element-selenium/

import csv
import random
import time
import os
print(os.environ['PATH'])
from selenium import webdriver

#os.chdir("/Users/lucy/Desktop/summer/datacollection")

os.chdir("/Users/lucy/Desktop/assortedcodes")

debug=True
 
from selenium import webdriver
 
with open('outfail2.csv', 'w', newline='') as log:
    logwriter = csv.writer(log)
 
    with open('fail2.csv', newline='') as infile:
        records = csv.reader(infile)
 
        for r in records:
            log_row = r.copy()
            print('Start fetching URL to', r[0], r[1], 'filed on', r[3], '...')
            start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
 
            driver = webdriver.Chrome('/Users/lucy/Downloads/chromedriver')
 
            try:
                driver.get(r[4])
                time.sleep(3 + random.random() * 3)
                filing_date = driver.find_element_by_xpath('//*[@id="formDiv"]/div[2]/div[1]/div[2]').text
                if debug:
                    print(filing_date)
                period_of_report = driver.find_element_by_xpath('//*[@id="formDiv"]/div[2]/div[2]/div[2]').text
                if debug:
                    print(period_of_report)
                
                #Tried out driver.find_element_by_path method but did not work  
                #if debug: 
                    #print(driver.find_element_by_xpath('//*[@id="formDiv"]/div/table/tr/td[4]'))
                #if 'EX-13'== driver.find_element_by_xpath('//*[@id="formDiv"]/div/table/td[4]'):
                    #form_text = driver.find_element_by_xpath('//*[@id="formDiv"]/div/table/tbody/td[3]/a').text

                html=[]
                form_text = driver.find_element_by_partial_link_text('ex13').text
                if form_text:
                    form_text.append(html)
                    if debug:
                        print(form_text)
                    form_link = driver.find_element_by_link_text(form_text).get_attribute('href')
                else: 
                    form_text=driver.find_element_by_partial_link_text('exv13').text
                    if form_text:
                        print(form_text)
                        form_link = driver.find_element_by_link_text(form_text).get_attribute('href')
                    else: 
                     form_text = driver.find_element_by_partial_link_text(".txt").text
                     form_link = driver.find_element_by_link_text(form_text).get_attribute('href')
            
            ########

                    #form_text.append(html)
                    #if debug:
                        #print(form_text)
                    #form_link = driver.find_element_by_link_text(form_text).get_attribute('href')
                    #if not html:
                        #print("nofound")
                        #form_text = driver.find_element_by_partial_link_text(".txt").text
                        #print(form_text)
                        #form_link = driver.find_element_by_link_text(form_text).get_attribute('innerText')
            ########

                if debug:
                    print(form_link)
                end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                print('Success!', start_time, ' --> ', end_time, '\n')
                log_row = log_row + [start_time, end_time, filing_date, period_of_report, form_link]
 
            except:
                end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                print('Error!', start_time, ' --> ', end_time, '\n')
                log_row = log_row + [start_time, end_time, 'ERROR!']
 
            driver.quit()
 
            logwriter.writerow(log_row)