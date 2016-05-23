import time
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from bs4 import BeautifulSoup

cities = ['Bangalore','Chandigarh','Chennai','Coimbatore','Delhi','Delhi-NCR','Ernakulam','Goa','Hyderabad',
'Indore','Jaipur','Kolkata','Mumbai','Mysore','Nagpur','Nashik','Pune','Surat','Vadodara','Vizag']

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    print('[+] JustDial Scrapping Started[+]')
    return driver


def lookup(driver,cities):
    with open('just_dial_B_2_B.csv','a') as file:
        writer = csv.writer(file)
        try:
            driver.get('http://www.justdial.com/')
            city_box = driver.wait.until(EC.presence_of_element_located(
                (By.ID,'city')))
            search_box = driver.wait.until(EC.presence_of_element_located(
                (By.ID,'srchbx')))
            search_button = driver.wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME,'search-button')
            ))

            for city in cities:
                city_box.send_keys(city)
                search_box.send_keys('b2b')
                search_button.click()

                for data in driver.find_elements_by_class_name('cntanr'):
                    company_name = data.find_element_by_class_name('jcn').text
                    print(company_name)

        except ElementNotVisibleException:
            print('Element not visible')



if __name__ == "__main__":
    driver = init_driver()
    lookup(driver,cities)
    time.sleep(5)
    driver.quit()
