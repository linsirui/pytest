#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

from src.action.a_login import Alogin
from src.action.a_logout import Alogout
from selenium import webdriver
import time
import json
from common import httprequest

def run_step(test_env, browser):
    '''执行本case所有步骤, 每个case文件必须包含此函数'''
    import_string = "src.testdata." + test_env + ".config"
    import_string_case ="src.testdata."+ test_env + ".d_case1"
    tcfg = __import__(import_string, None, None, "config", 0)        #导入某环境配置文件
    tcfg_case = __import__(import_string_case,None,None,"d_case3",0)
    #__clogin(tcfg.CFG_ENV_URL, browser, tcfg.CFG_SUPPLIER_USERNAME, tcfg.CFG_SUPPLIER_PASSWORD)
    #app_icon = browser.find_element_by_xpath("//i[contains(@class, 'ts-icon-apps')]")
    #app_icon.click()
    url = tcfg_case.REQUEST_URL
    postdata = json.dumps(tcfg_case.LOGINPOST_DATA)
    requestheader = tcfg_case.REQUEST_HEADER
    print("the json data is", postdata)
    httprequest.httppost(url,requestheader,postdata)

    #browser.get("https://cn-sandbox.tradeshift.com/#/apps/Tradeshift.AppStore/apps/activated")
     #  time.sleep(4)

    #__clogout(tcfg.CFG_ENV_URL, browser)

def __httpget(url, header, data):
    '''httpget'''
    
    httprequest.httpget(url, header, data)
    

#def __clogout(url, browser):
    #'''登出'''
    #act = Alogout(url, browser)
    #act.logout()


