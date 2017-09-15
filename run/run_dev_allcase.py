#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import run.case_name_list as namelist
import common as com
from selenium import webdriver

#配置被测环境, 值与testdata下的环境包名相同
ENV_CONFIG = "dev"

#配置被测浏览器
BROWSER = webdriver.Chrome()

#------List为要执行的case name, 取至case_name_list.py------
caselist = []
caselist.append(namelist.CASE1)
caselist.append(namelist.CASE1)
#-------------------------------------------------------

com.startrun(ENV_CONFIG, BROWSER, caselist)
