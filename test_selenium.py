# coding: utf-8
# !/usr/bin/python3



import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

def test_basic_headless_selenium_example():
    """Test selenium installation by opening python website.
    (inspired by https://selenium-python.readthedocs.io/getting-started.html)
    """
    opts = Options()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    driver.get("http://10.29.229.156:8000/")
    lat = driver.find_element_by_id('addlat')
    lat.send_keys("50")
    lon= driver.find_element_by_id('addlng')
    lon.send_keys("50")
    what = driver.find_element_by_id('addname')
    what.send_keys("test auto")
    date = driver.find_element_by_id('adddate')
    date.send_keys("2023-01-18")
    time.sleep(5)
    driver.find_element_by_id('addpoint').click()
    time.sleep(5)
    driver.find_element_by_xpath('//img[@alt="test auto"]').click()
    time.sleep(5) # pour que le bouton DELETE apparait
    driver.find_element_by_xpath('//a[@class="btn btn-danger delete-point"]').click()
    
    
    driver.close()
