'''
Created: Jul 23, 2016
Last Edited: Feb 22, 2017

@author: jes97210

This file handles all the scraping with Selenium. Fairly simple, since the ubc
site for courses is also very simple.
'''

from selenium import webdriver
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException


# Desc: Initialized the driver, and returns it.
# Takes: N/A
# Returns: driver (WebDriver)
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 50)
    return driver


def scrape_dept(driver):
    text_inside = driver.find_element_by_tag_name("dl").text
    # print(text_inside)
    return text_inside


def main(dept_code):
    driver = init_driver()
    driver.get('http://www.calendar.ubc.ca/vancouver/courses.cfm?page=code&institution=12&code=' + dept_code)
    contained = scrape_dept(driver)
    time.sleep(10)
    driver.quit()
    return contained

if __name__ == "__main__":
    main()
