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
    data = {}
    count = 0
    with open('companies1.csv','a') as file:
        writer = csv.writer(file)
        try:
            for trs in driver.find_elements_by_xpath('//table[@cellpadding=3][@cellspacing=1][@border=0]//tbody//tr'):
                if trs.find_elements_by_xpath('//tr[@valign=top]'):
                    for tds in trs.find_elements_by_xpath('//tr[@valign=top]'):
                        company_name = tds.find_elements_by_xpath('//td[1]').text
                        industry = tds.find_elements_by_xpath('//td[2]').text
                        count +=1
                        if(company_name !='' and industry!=''):
                            writer.writerow([company_name,industry])
                            print(company_name)

                else:
                    for tds in trs.find_elements_by_xpath('//tr'):
                        writer.writerow([tds.text])
                        print(tds.text)

                writer.write('\n')
        except TimeoutException:
            print('element not visible')


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()