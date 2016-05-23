import argparse,os,time
import urlparse,random
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
from selenium.webdriver.common.keys import Keys



def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    print('[+] eRail Scrapping Started[+]')
    return driver

def erail(driver,from_station,to_station,date):
    print(driver.title)
    data = {}
    driver.get('http://erail.in/?T='+args.from_station+'::'+args.to_station)

    datePickerElement = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="tdDateFromTo"]/input[2]')))
    datePickerElement.send_keys(date)
    datePickerElement.send_keys(Keys.ENTER)
    # soup = get_train_schedule(page)
    tableElement = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="divTrainsList"]/table[1]')))
    page = BeautifulSoup(driver.page_source,'lxml')
    table = page.find("table", {"class":"DataTable TrainList"})
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        data["train_num"] = cells[0].find(text=True)
        data["train_name"] = cells[1].find(text=True)
        data["fromStation"] = cells[2].find(text=True)
        data["dep"] = cells[3].find(text=True)
        data["toStation"] = cells[4].find(text=True)
        data["arr"] = cells[5].find(text=True)
        data["travel"] = cells[6].find(text=True)
        data["mon"] = cells[8].find(text=True)
        data["tue"] = cells[9].find(text=True)
        data["wed"] = cells[10].find(text=True)
        data["thu"] = cells[11].find(text=True)
        data["fri"] = cells[12].find(text=True)
        data["sat"] = cells[13].find(text=True)
        data["sun"] = cells[14].find(text=True)
        data["oneA"] = cells[15].find(text=True)
        data["twoA"] = cells[16].find(text=True)
        data["threeA"] = cells[17].find(text=True)
        data["SL"] = cells[18].find(text=True)
        print(data)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("from_station",help="erail from_station")
    parser.add_argument("to_station",help = "irctc password")
    args = parser.parse_args()
    driver = init_driver()
    os.system('clear')
    date="23-05-2016"
    erail(driver,args.from_station,args.to_station,date)
    time.sleep(5)
    driver.quit()
