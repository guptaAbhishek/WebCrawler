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
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


# i have changed this line


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("email",help="linkedin email")
    parser.add_argument("password",help = "linkedin password")
    args = parser.parse_args()

    browser = init_driver()
    browser.get('https://linkedin.com/uas/login')
    try:
        emailElement = browser.wait.until(EC.presence_of_element_located((By.ID,'session_key-login')))
        emailElement.send_keys(args.email)
        passElement = browser.wait.until(EC.presence_of_element_located((By.ID,'session_password-login')))
        passElement.send_keys(args.password)
        passElement.submit()
    except ElementNotVisibleException:
        print('could not find element')

    os.system('clear')
    print("[+] Success Logged In, Bot Starting!")
    # here to start your function to scrappe the data

    browser.close()




def init_driver():
    browser = webdriver.Firefox()
    browser.wait = WebDriverWait(driver,5)
    print('[+] LinkedIn Scrapping Started[+]')
    return browser



if __name__ == "__main__":
    Main()
