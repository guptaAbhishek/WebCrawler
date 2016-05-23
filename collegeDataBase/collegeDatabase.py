import time
import csv
import datetime
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from bs4 import BeautifulSoup


def init_driver():
    driver = webdriver.PhantomJS()
    driver.wait = WebDriverWait(driver,5)
    return driver

def get_college(driver):
    client = MongoClient('mongodb://localhost:27017/colleges')
    db = client.colleges.collegesDoc
    college = {}
    print('[+] Careers360 College Data Scrapping[+]')
    for i in range(1,100):
        driver.get('http://www.engineering.careers360.com/colleges/list-of-engineering-colleges-in-India?page='+str(i))
        try:
            try:
                dialog_box = driver.find_element_by_class_name('bClose')
                dialog_box.click()
            except ElementNotVisibleException:
                print('Dialog Box is not on this page')
            a = driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'search-result')))
            if a:
                results = driver.find_elements_by_class_name('search-result')
                for result in results:
                    try:
                        try:
                            logo_div = result.find_element_by_class_name('image-box')
                            logo = logo_div.find_element_by_tag_name('img').get_attribute('src')
                            link_div = result.find_element_by_class_name('title')
                            link_elm = link_div.find_element_by_tag_name('a')
                            name = link_elm.text
                            careers360_link = link_elm.get_attribute('href')
                        except ElementNotVisibleException:
                            name = 'Not Available'
                            careers360_link = 'Not Available'
                            print('Logo Div Not Visible')
                        try:
                            location = result.find_elements_by_class_name('clg-state')
                            if not location:
                                location = 'Not Available'
                            else:
                                location = result.find_element_by_class_name('clg-state').text
                        except ElementNotVisibleException:
                            location = 'Not Available'
                            print('clg-state Not Visible')

                        try:
                            website = result.find_elements_by_class_name('clg-url')
                            if not website:
                                website = 'Not Available'
                            else:
                                website = result.find_element_by_class_name('clg-url').text
                        except ElementNotVisibleException:
                            website = 'Not Available'
                            print('clg-url Not Visible')

                        try:
                            estd = result.find_elements_by_class_name('clg-estd')
                            if not estd:
                                estd = 'Not Available'
                            else:
                                estd = result.find_element_by_class_name('clg-estd').text
                        except ElementNotVisibleException:
                            estd = 'Not Available'
                            print('clg-estd Not Visible')

                        try:
                            c_type = result.find_elements_by_class_name('clg-type')
                            if not c_type:
                                c_type = 'Not Available'
                            else:
                                c_type = result.find_element_by_class_name('clg-type').text
                        except ElementNotVisibleException:
                            c_type = 'Not Available'
                            print('c_type Not Visible')

                        try:
                            contact = result.find_elements_by_class_name('clg-contact')
                            if not contact:
                                contact = 'Not Available'
                            else:
                                contact = result.find_element_by_class_name('clg-contact').text
                        except ElementNotVisibleException:
                            contact = 'Not Available'
                            print('clg-contact Not Visible')

                        college["college_name"] = name
                        college["college_logo"] = logo
                        college["careers360_link"] = careers360_link
                        college["college_location"] = location
                        college["college_website_url"] = website
                        college["college_estd"] = estd
                        college["college_type"] = c_type
                        college["college_contact"] = contact
                        db.save(college)
                        college={}
                    except ElementNotVisibleException:
                        print('Element Not Found')
        except TimeoutException:
            print('Time out expception')

if __name__ == "__main__":
    driver = init_driver()
    get_college(driver)
    time.sleep(5)
    driver.quit()
