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

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    print('[+] ICAI Scrapping Started[+]')
    return driver

def get_web_links(page):
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if '.icai.org.in' in url:
                links.append(url)
    return links

def grab_info(page):
    content = page.find('div',id='content')
    return content.contents

def grab_email(page):
    email = page.findAll('a')
    if email:
        if 'mailto:' in email:
            result = email
    return result

def grab_company_name(page):
    company_name = page.find('div',{'id':'header'})
    company_name = company_name.get_text()
    return company_name


def Main(driver):
    driver.get('http://www.icai.org.in/search.html')
    elm = driver.find_element_by_name('searchbyarea')
    for option in elm.find_elements_by_tag_name('option'):
        if option.text == 'Accounting Advisory Services':
            option.click()
            break

    button = driver.find_element_by_name('submit')
    button.click()
    try:
        table = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//table[@cellpadding=3][@cellspacing=3][@bgcolor=#FCF4C9]'))
        )
        page = BeautifulSoup(driver.page_source)
        links = get_web_links(page)
        with open('icai.csv','a') as file:
            writer = csv.writer(file)
            for link in links:
                driver.get(link)
                p = BeautifulSoup(driver.page_source)
                content = grab_info(p)
                company_name = grab_company_name(p)
                email = grab_email(p)
                writer.writerow([company_name,email,link,content])

    except ElementNotVisibleException:
        print('[-] ElementNotVisibleException [-]')



if __name__ == "__main__":
    driver = init_driver()
    Main(driver)
    time.sleep(5)
    driver.quit()
