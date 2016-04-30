import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    return driver

def lookup(driver):
    driver.get('http://www.crisil.com/ratings/credit-ratings-list.jsp')
    data = []
    columnCount = 0
    with open('companies.csv','w') as file:
        writer = csv.writer(file,delimiter = '\t', lineterminator = '\n',)
        try:
            for tds in driver.find_elements_by_class_name('inner_content_table'):
                print(tds.text)
                columnCount +=1
                data['companyName'] = tds.text
                writer.writerow(tds.text)
        except ElementNotVisibleException:
            print('element not visible')


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()
