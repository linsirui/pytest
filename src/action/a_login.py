#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import src.object.o_login
import src.object.o_tasklist
from common.reporter import checkpoint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Alogin(object):
    '''参数:url, username, passowrd'''

    def __init__(self, url, browser, username, password):
        self.username = username
        self.password = password
        self.url = url
        self.driver = browser

    def login(self):
        '''登录'''
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(60)
        driver.get(self.url)
        obj = src.object.o_login
        input_username = driver.find_element_by_name(obj.INPUT_USERNAME_NAME)
        input_username.clear()
        input_username.send_keys(self.username)
        input_password = driver.find_element_by_name(obj.INPUT_PASSWORD_NAME)
        input_password.clear()
        input_password.send_keys(self.password)
        driver.find_element_by_name(obj.BUTTON_LOGIN_NAME).click()
       
        #检查登录跳转正确
        
        #使用expected_conditions中的visibility_of_element_located方法等待id = "user"的元素加载完成
        try:
            obj = src.object.o_tasklist
            locator = (By.ID,obj.DIV_USER_ID)
            element_user = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
        
        finally:
            checkpoint(element_user != None, "检查用户登录是否成功")

        
        
