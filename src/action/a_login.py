#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import src.object.o_login
import src.object.o_tasklist
from selenium import webdriver


class Alogin(object):
    '''参数:url, username, passowrd'''

    def __init__(self, url, username, password, browser = webdriver.Chrome()):
        self.username = username
        self.password = password
        self.url = url
        self.driver = browser

    def login(self):
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
        time.sleep(1)
        #检查登录跳转正确
        obj = src.object.o_tasklist
        check_user_title = driver.find_element_by_id(obj.DIV_USER_ID)
        str_title = check_user_title.get_attribute(obj.ATTRIBUTE_USER_TITLE)
        assert str_title == obj.TEXT_USER_TITLE  #登录用户名和公司名匹配失败
