# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:46:57 2021

@author: usenaslan
"""
## Selenium Kutuphanesinin Import edilmesi
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



#Class Olusturulmasi
class Insider():

  #init fonkiyonu ile insider classi calistitiildiginda calisacak fonksiyonu gostermektedir.
  def __init__(self):
      self.setup(self)
   
  #test baslamadan once girilmesi gereken degisken ve ayarlarin yer aldigi fonksiyon
  def setup(self,method):
    self.driver = webdriver.Chrome()
    self.var = {"url":"https://useinsider.com/",
                "window-height":1936,
                "window-width":1056     
                }
  #verilen websistesini istenilen duruma gore test yapan fonksiyon
  def testing(self):
    #selenium webdriver kutuphanesiyle chrome web tarayacisinda ilgili url'yi acar
    self.driver.get(self.var["url"])
    
    #web browserin boyutlarini set etmek icin kod adimi
    self.driver.set_window_size(self.var["window-height"], self.var["window-width"])
    
    try:
        #web tarayicisi ilgili web sitesine gittikten sonra anasayfanin acilip acilmadigini navbara'a gore kontrolunu saglayan kod 
        WebDriverWait(self.driver,3000).until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, "#navbarNavDropdown")))
        print("Ana Sayfa Yuklendi.")
        
        #Carrers sayfasina gitmek icin web tarayaicisi  uzerinden navbarda ilgili element'e click eden kod adimlari
        self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[5]/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[5]/div/div[1]/div[3]/div/a/h5").click()
        
        try:
            #Carrers sayfasina gidildiktan sonra 'find a job' elementine gore sayfanin yuklenip yuklenmemesini saglayan kod 
            WebDriverWait(self.driver,3000).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//*[@id='find-job-widget']/div/div/div[2]/a")))
            print("'Careers' Sayfası Yüklendi.'")
            
            #Carress sayfasinda 'Find a job' eleminine sayfasiyi scroll yapan kod adimi
            element = self.driver.find_element_by_xpath("//*[@id='find-job-widget']/div/div/div[2]/a")
            
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            
            #'Find a job' sayfasina ilgili elemente tiklayarak gondren adim
            self.driver.find_element(By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a").click()
            
            try:
                
                #'find a job' sayfasinin acilip acilmadigini filtre elementini kontrol ederek gosteren test adimi
                WebDriverWait(self.driver,3000).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//*[@id='top-filter-form']/div[1]")))
                
                #'Job locations' filtresini acmak ve acildigini gostermek icin kodu beleden kod 
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//*[@id='top-filter-form']/div[1]/span/span[1]/span/span[2]/b").click()
                time.sleep(15)
                
                #'istanbul' lokasyonunu filtreye set eden kod adimlari
                element = self.driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[12]")
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                time.sleep(5)
                self.driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[9]").click()
                time.sleep(5)
                
                #'Job Departmant' filtresini acmak ve acildigini gostermek icin kodu beleden kod adimlari
                self.driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div/form/div[2]/span/span[1]/span/span[2]/b").click()
                time.sleep(5)
                
                #'Quality Assurance' filtreye set eden kod adimi 
                element = self.driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[16]")
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                time.sleep(5)
                self.driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[14]").click()
                time.sleep(5)
                
                
                #ilgili filtrelemeler yapildiktan sonra 'Apply Job' elementine sayfayi scroll eden kod adimi
                element_job_list =  self.driver.find_element_by_xpath("//*[@id='career-position-list']/div/div/div[1]/h3")
                self.driver.execute_script("arguments[0].scrollIntoView();", element_job_list)
                
                #'Apply Job' koduna giden test adimi
                #jobs-list > div:nth-child(2) > div > a
                self.driver.find_element_by_css_selector("jobs-list > div:nth-child(2) > div > a").click()
                
            except TimeoutException:
                print("'Open Positions' sayfası acilmamistir.")
                self.driver.quit()    
            
        except TimeoutException:
            print("Careers sayfasında 'Find Your Dream Job' alani bulunamadi.")
            self.driver.quit()
        
    except TimeoutException:
        print("Ana Sayfa Yüklenmemistir.")
        self.driver.quit()


Test = Insider()
Test.testing()