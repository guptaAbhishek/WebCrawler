import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver,5)
    return driver

def lookup(driver):
    count = 0
    with open('hackernew.csv',"w") as textSave:
        for i in range(1,20):
            driver.get('https://news.ycombinator.com/news?p='+str(i));
            try:
                articles = driver.find_elements_by_class_name('title')
                for i in articles:
                    if(i):
                        print(i.text)
                        textSave.write(i.text+"")
                        count+=1
                        if(count == 30):
                            continue
                    else:
                        print('empty')
            except ElementNotVisibleException:
                print('ElementNotVisibleException')

if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()
