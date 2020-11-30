from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
import time
import pause
#import pynput
import os
#import re
#from pynput.keyboard import Key, Controller
from datetime import datetime


class AutoGMeet():
    usernameStr = None
    passwordStr = None
    url_meet = None
    chatbox = None
    options = None
    browser = None
    

    def __init__(self,username_string,password_string,url_of_meet,text_in_chat_box,endtime,):
        self.usernameStr = username_string
        self.passwordStr = password_string
        self.url_meet = url_of_meet
        self.chatbox = text_in_chat_box
        self.end = endtime
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--window-size=800,600")
        self.options.add_experimental_option("prefs", { \
                "profile.default_content_setting_values.media_stream_camera": 2,
                "profile.default_content_setting_values.media_stream_mic": 2, 
                # "profile.default_content_setting_values.geolocation": 2, 
                "profile.default_content_setting_values.notifications": 2 
        })
        self.browser = webdriver.Chrome(chrome_options=self.options)

    
    #------------------------------------Wrapper for Gmail ID And Non Gmail ID-------------------------------------------------
    
    def automeetX(self):
        self.browser.get(('https://stackoverflow.com/'))
        self.waiting_N_click("/html/body/header/div/ol[2]/li[2]/a[2]")
        self.waiting_N_click("//*[@id=\"openid-buttons\"]/button[1]")
        username = self.browser.find_element_by_id('identifierId')
        username.send_keys(self.usernameStr)
        nextButton = self.browser.find_element_by_id('identifierNext')
        nextButton.click()
        time.sleep(2) # 5
        password = self.browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
        password.send_keys(self.passwordStr)
        signInButton = self.browser.find_element_by_id('passwordNext')
        signInButton.click()
        time.sleep(2) # 3
        self.browser.get(self.url_meet)
        time.sleep(6) # 6
        try:
            self.waiting_N_click('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div')
            try:
                self.browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
            except:
                self.browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]").click()
        except:
            try:
                self.browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
            except:
                self.browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]").click()
        time.sleep(5) # As your wish
        clickchaticon= self.waiting_N_click('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span')
        time.sleep(4)
        textbox=self.browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea')
        textbox.send_keys(self.chatbox,Keys.RETURN)
        textbox.send_keys(Keys.ESCAPE)
        while True:
            getTime = str(datetime.today().time())
            currentTime = int(getTime[:2] + getTime[3:5])
            if currentTime>self.end:
                self.browser.refresh()
                self.browser.close()
                try:
                    #self.browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div/span').click()
                    break
                except:
                    #self.browser.close()
                    break
        return self.browser


    def waiting_N_click(self,path):
        try:
            self.browser.find_element_by_xpath(path).click()
        except:
            time.sleep(1)
            self.waiting_N_click(path)