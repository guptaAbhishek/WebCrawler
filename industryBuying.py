import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
import json
import sys

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    return driver

def lookup(driver):
    info = {}
    driver.get('http://www.industrybuying.com/');
    try:
        data = driver.find_elements_by_class_name('AH_CategoriesList')
        for i in data:
            if(i):
                 h = i.get_attribute('href')
                 driver.get(h)
                 try:
                    print('working')
                    products = driver.find_elements_by_class_name('catethumb')
                    for product in products:
                        if(product):
                            print(product.find_element(By.XPATH,'//*[@id="main"]/div[1]/div/div/div/div/div[4]/div[2]/div[1]/div/p/a').get_attribute('href'))
                            print(product.find_element(By.CLASS_NAME,'productTitle').text)
                        else:
                            print('empty product')
                 except TimeoutException:
                    print('could not found product listing')
            else:
                print 'empty'
    except TimeoutException:
        print('fucking fuck off')

    return json.dumps(info)


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()
