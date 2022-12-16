import os
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from csv import writer
from selenium.webdriver.common.by import By
import pandas as pd
import re

class Scraper():
    
    def __init__(self):
        pass
    
    def US_Census(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.census.gov/data.html')
        time.sleep(5)
        driver.find_element("xpath","/html/body/div[3]/div/div/div[6]/div/div[4]/section/div[2]/a[1]").click()
        time.sleep(2)
        driver.find_element("xpath","/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[2]/main/div[2]/div[1]/div/div[4]/div[3]/div/div[1]/div/div[1]/div[2]/div[1]/button").click()
        time.sleep(10)
        driver.find_element("xpath","/html/body/div/div/div[2]/div/div/div[3]/div[1]/header/div/div[2]/div[2]/div/div[1]/nav/div/div[1]/a[2]").click()
        time.sleep(10)
        driver.find_element("xpath","/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[2]/div[1]/div/div[5]/div/section/ul/li[2]/div").click()
        time.sleep(2)
        driver.find_element("xpath","/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[3]/main/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/div[2]/div/div[2]/div").click()
        time.sleep(2)
        driver.find_element("xpath","/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[3]/main/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/form/div[2]/input").send_keys("Alaska")
        time.sleep(2)
        driver.find_element("xpath","/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[3]/main/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div/section/ul/li").click()
        time.sleep(2)
        driver.find_element("xpath","/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[3]/main/div[2]/div[1]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/div[4]").click()
        time.sleep(10)





        for i in range(1,11):
            path=f"/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[3]/aside/div/div/div/div[2]/div/div[2]/div{[i]}"
            driver.find_element("xpath",path).click()
            time.sleep(5)
            path=f"/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[3]/aside/div/div/div/div[2]/div/div[2]/div{[i]}/div/div/div/div[3]"
            driver.find_element("xpath",path).click()
            time.sleep(2)
            all_pages=driver.find_element("xpath",path).text
            temp = re.findall(r'\d+', all_pages)
            products = list(map(int, temp))
            time.sleep(10)
            for pro in range(1,products[0]+1):
                time.sleep(5)
                path=f"/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[3]/aside/div/div/div/div[2]/div/div[2]/div{[i]}/div/div/div/div[4]/div/div{[pro]}"
                driver.find_element("xpath",path).click()
                time.sleep(20)
                driver.find_element("xpath","/html/body/div/div/div[2]/div/div/div[4]/div[2]/div[1]/div/div[4]/main/div[1]/div[1]/section/div[2]/div/div[1]/div[17]/div/div[1]").click()
                time.sleep(10) 


obj=Scraper()
obj.US_Census()