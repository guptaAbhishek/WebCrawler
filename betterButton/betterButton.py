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

def getRecipesLink(page):
    recipes = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if 'recipes/' and not '?q=cuisines' in url:
                recipes.append(url)
    return recipes

def getRecipesCuisines(page):
    recipesCuisines = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if '?q=cuisines:' in url:
                recipesCuisines.append(url)
    return recipesCuisines

def chefAndRest(page):
    chefAndRest = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if 'recipes/' and '?q=cuisines' in url:
                chefAndRest.append(url)
            else:
                chefAndRest.append(url)
    return chefAndRest


def lookup(driver):
        driver.get('http://www.betterbutter.in/')
        data = {}
        count = 0
        try:
            page = driver.page_source
            soup = BeautifulSoup(page)
            recipes = getRecipesLink(soup)
            for recipesLink in recipes:
                driver.get('http://www.betterbutter.in/'+recipesLink)

                print(BeautifulSoup(driver.page_source).title)
        except TimeoutException:
            print('element not visible')


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()
