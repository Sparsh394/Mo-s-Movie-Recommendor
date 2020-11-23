import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup
import re
import time
import os

# GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
# CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

def get_links(movie): 
    movie=re.sub(r'([^\s\w]|_)+', '', movie.lower().strip())
    # print(test_string)
    movie=movie.replace(' ','-')
    
    print('Test: ' + movie)
    
    url='https://www.justwatch.com/in/movie/'+movie
    # print(url)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--diable-dev-shm-usage')
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.maximize_window() 
    driver.get(url)
    time.sleep(10)
    # page_load = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/ion-app/div[1]/div[1]/div/div[2]/ion-tab-bar/div[1]/a/img")))
    
    page_source=driver.page_source
    soup=BeautifulSoup(page_source,'html.parser')
    pretty_soup=soup.prettify()
    
    categories = soup.find_all('div', {'class': 'price-comparison__grid__row__title'})
    holders = soup.find_all('div', {'class': 'price-comparison__grid__row__holder'})
    
    watch_options = {}
    
    for i in range(len(categories)): 
        links = {}
        
        urls = holders[i].find_all('a')
        icons = holders[i].find_all('img')
        
        for j in range(len(urls)): 
            links[urls[j].get('href')] = { 'src': icons[j].get('src')}
        
        watch_options[categories[i].text.strip()] = links

    # print(watch_options)
    
    return watch_options