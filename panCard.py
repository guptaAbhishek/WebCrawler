import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    return driver

def lookup(driver,pan):
    baseUrl = 'https://incometaxindiaefiling.gov.in/e-Filing'
    driver.get('https://incometaxindiaefiling.gov.in/e-Filing/Services/KnowYourJurisdictionLink.html')
    try:
        panBox = driver.find_element_by_id('KnowYourJurisdiction_panOfDeductee')
        panBox.clear()
        panBox.send_keys(pan)
        imageElm = driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "captchaImgBox")))
        imageSrc = imageElm.get_attribute('src')
        imageSrc =baseUrl + imageSrc
        driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'captchaImgBox'))).save_screenshot('1.png')
        print(imageSrc)
    except ElementNotVisibleException:
        print('shit happens')


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver,'AVZPG5008J')
    time.sleep(5)
    driver.quit()
