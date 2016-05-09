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
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    return driver

def get_college(driver):
    client = MongoClient('mongodb://localhost:27017/colleges')
    db = client.collegesDoc
    college = {}
    for i in range(1,100):
        driver.get('http://www.engineering.careers360.com/colleges/list-of-engineering-colleges-in-India?page='+str(i))
        try:
            results = driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'search-result')))
            for result in results:
                logo = result.find_element_by_xpath('//*[@id="content"]/div/ol/li[1]/div[2]/img').get_attribute('src')
                link = result.find_element_by_xpath('//*[@id="content"]/div/ol/li[2]/div[3]/div[1]/a')
                careers360_link = link.get_attribute('href')
                name = link.text
                location = result.find_element_by_class_name('clg-state').text
                website = result.find_element_by_class_name('clg-url').text
                estd = result.find_element_by_class_name('clg-estd').text
                c_type = result.find_element_by_class_name('clg-type').text
                contact = result.find_element_by_class_name('clg-contact').text

                college["college_name"] = name
                college["college_logo"] = logo
                college["careers360_link"] = link
                college["college_location"] = location
                college["college_website_url"] = website
                college["college_estd"] = estd
                college["college_type"] = c_type
                college["college_contact"] = contact

                print(college)
        except TimeoutException:
            print('Time out expception')

if __name__ == "__main__":
    driver = init_driver()
    get_college(driver)
    time.sleep(5)
    driver.quit()
