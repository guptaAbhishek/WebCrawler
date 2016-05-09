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
    driver.set_window_size(1120,550)
    driver.wait = WebDriverWait(driver,5)
    print('[+] ZaubaCorp Scrapping Started[+]')
    return driver


def lookup(driver,company):
    with open('chargesAndBorrowings.csv','a') as file:
        # fieldnames = ['company_name', 'cin','company_status','date_of_incorporation','age_of_company','company_activity','auth_capital','paid_up_capital','company_address','email']
        writer = csv.writer(file)
        # writer.writeheader()
        try:
            row_count = 0
            driver.get('https://www.zaubacorp.com/')
            box = driver.wait.until(EC.presence_of_element_located(
                (By.NAME, "searchvalue")))
            button = driver.wait.until(EC.element_to_be_clickable(
                (By.NAME, "op")))
            box.send_keys(company)
            button.click()
            link = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="results"]/tbody/tr/td[2]/a')))
            link.click()
            company_name = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[1]/h1'))).text
            cin = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[1]/table/thead/tr/td[2]/p/a'))).text
            company_status = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]/p/span'))).text
            date_of_incorporation = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[1]/table/tbody/tr[8]/td[2]/p'))).text
            age_of_company =driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[1]/table/tbody/tr[9]/td[2]/p'))).text
            company_activity =driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[1]/table/tbody/tr[10]/td[2]/p[1]'))).text
            auth_capital =driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[2]/p'))).text
            paid_up_capital =driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[4]/table/tbody/tr[2]/td[2]/p'))).text
            company_address =driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[14]/table/tbody/tr/td[4]/p'))).text
            email =driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[8]/div/div[1]/p[1]'))).text
            # charges_borrowing_details = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="block-system-main"]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]/p/span'))).text
            row_count = len(driver.find_elements_by_xpath("//*[@id='charges']/tbody/tr"))

            print(row_count)
            if row_count > 3:
                charges_borrowing_details = 'Yes'
                link = driver.current_url
            else:
                charges_borrowing_details = 'No'
                link = 'Not Applicable'
            auth_capital = auth_capital.replace(u"\u20b9","")
            paid_up_capital = paid_up_capital.replace(u"\u20B9","")
            email = email.replace("Email ID: ","")
            writer.writerow([company_name,cin,company_status,email,company_address,date_of_incorporation,age_of_company,auth_capital,paid_up_capital,charges_borrowing_details,link])
            print('success')
        except TimeoutException:
            print('element not visible')


if __name__ == "__main__":
    driver = init_driver()
    file = open('companies_list.csv','rU')
    for line in file:
        cells = line.split(',')
        lookup(driver,cells[2])
    time.sleep(5)
    file.close()
    driver.quit()

# //*[@id="block-system-main"]/div[2]/div[1]/div[1]/table/thead/tr/td[2]/p/a
