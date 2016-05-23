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


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    print('[+] IRCTC Login Started[+]')
    return driver

def irctc_login(driver):
    print(driver.title)
    otp = input('[+] Enter the otp = ')
    optInputElement = driver.wait.until(EC.presence_of_element_located((By.NAME,'loginotp')))
    optInputElement.send_keys(otp)
    verifyButtonElement = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//input[@value="verify"]')))
    verifyButtonElement.click()
    print(driver.title)
    print('[+] Login Successful ! [+]')
    # plan_my_journey(driver)
    get_profile_info(driver)

def plan_my_journey(driver):
    # These are the inputs from the user
    # fromStation = input('[+] Enter From station [+]')
    # toStation = input('[+] Enter To station [+]')
    # dateOfJourney = input('[+] Enter Date of Journey [+]')

    fromStationElement = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="jpform:fromStation"]')))
    fromStationElement.send_keys("DEOS")
    fromStationElement.send_keys(Keys.TAB)

    toStationElement = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="jpform:toStation"]')))
    toStationElement.send_keys("NDLS")
    toStationElement.send_keys(Keys.TAB)

    dateOfJourneyElement = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="jpform:journeyDateInputDate"]')))
    dateOfJourneyElement.send_keys("23-05-2016")

    submitButtonElement = driver.wait.until(EC.presence_of_element_located((By.ID,'jpform:jpsubmit')))
    submitButtonElement.click()
    print(driver.title)
    print('Getting the Train Schedule.....')

# input from the user
# Quota e.g. tatkal,genral,premium tatkal
def select_quota(driver,quota):
    quotas = ['GN','PT','HP','LD','CK']
    if quota in quotas:
        quotaCheckBoxElement = driver.wait.until(EC.element_to_be_clickable((By.VALUE,quota)))
        quotaCheckBoxElement.click()
        print('[+] Quota Selection Success [+]')
    else:
        print('[-] Quota Selection Failed [-]')

# def count_classes(driver,train_num):
#
#
# # input from the user
# # Sleeper Class,1A,2A,3A class
# def select_class(driver,accommodation_class,train_num):
#     classes = ['1A','2A','3A','3E','CC','SL','2S']
#     if accommodation_class in classes:
#

def get_profile_info(driver):
    # driver.get('https://www.irctc.co.in/eticketing/userUpdateProfile.jsf')
    try:
        myProfileElement = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="topnav"]/li[4]/a')))
        hover = ActionChains(driver).move_to_element(myProfileElement)
        hover.perform()
        userUpdateProfileLinkElement = driver.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="topnav"]/li[4]/div/ul/li[1]/a')))
        userUpdateProfileLinkElement.click()
        try:
            user_first_name = driver.wait.until(EC.presence_of_element_located((By.ID,'updateUserDtls:firstName')))
            user_last_name = driver.wait.until(EC.presence_of_element_located((By.ID,'updateUserDtls:lastName')))
            user_full_name = user_first_name.text+' '+user_last_name.text
            user_email = driver.wait.until(EC.presence_of_element_located((By.ID,'updateUserDtls:email')))
            user_email = user_email.get_attribute('value')
            user_mobile = driver.wait.until(EC.presence_of_element_located((By.ID,'updateUserDtls:mobile')))
            user_mobile = user_mobile.get_attribute('value')
            print(user_full_name)
            print(user_email)
            print(user_mobile)
        except ElementNotVisibleException:
            print('[-] Could not extract user details! [-]')
    except ElementNotVisibleException:
        print('could not click on userUpdateProfile link')

def get_booked_ticket_history(driver):
    try:
        booked_ticket_history = driver.wait.until(EC.presence_of_element_located((By.LINK_TEXT,'Booked Ticket History (New)')))
        booked_ticket_history.click()
        booked_ticket_history_table_row = driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="txnHistory:bookedTicketHistoryDataTable:tb"]')))
        

    except ElementNotVisibleException:


    //*[@id="contentformid1:j_idt336_body"]/div[2]/table/tbody/tr[4]/td[2]/a


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user_id",help="irctc user_id")
    parser.add_argument("password",help = "irctc password")
    args = parser.parse_args()
    driver = init_driver()
    driver.get('https://www.irctc.co.in/eticketing/loginHome.jsf')

    try:
        userIdElement = driver.wait.until(EC.presence_of_element_located((By.ID,'usernameId')))
        userIdElement.send_keys(args.user_id)
        passElement = driver.wait.until(EC.presence_of_element_located((By.NAME,'j_password')))
        passElement.send_keys(args.password)
        otpRequestElement = driver.wait.until(EC.presence_of_element_located((By.ID,'otpId')))
        otpRequestElement.click()
        passElement.submit()
    except ElementNotVisibleException:
        print('could not find element')

    os.system('clear')
    irctc_login(driver)
    time.sleep(5)
    driver.quit()
