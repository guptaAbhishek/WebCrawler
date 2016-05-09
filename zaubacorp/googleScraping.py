import time
import csv
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

def get_user_details_link(page):
    links =[]
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if college_name in url:
                link.append(url)
    return links

def get_user_details(driver,page):
    search_results = []
    links = get_user_details_link(page,'nitrkl.ac.in')

    for link in links:
        driver.get(link)
        p = driver.page_source
        s = BeautifulSoup(p)
        search = s.body.findAll(text='Abhishek')









def lookup(drive,query):
    driver.get('https://www.google.com')
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "btnK")))
        box.send_keys(query)
        try:
            button.click()
        except ElementNotVisibleException:
            button = driver.wait.until(EC.visibility_of_element_located((By.NAME,"btnG")))
            button.click()

    except TimeoutException:
        print('Box or button not found in google.com')



if __name__ == "__main__":
    driver = init_driver()
    lookup(driver,"Abhishek Kumar Gupta National Institute of Technology Rourkela")
    time.sleep(5)
    driver.quit()
