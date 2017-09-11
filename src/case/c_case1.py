#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import src.testdata.dev.config as tconfig  #导入某环境配置文件
from src.action.a_login import Alogin

def run_step(test_env):
    '''执行本case所有步骤, 每个case文件必须包含此函数'''
    exec("import src.testdata." + test_env + ".config as tconfig") #导入某环境配置文件
    exec("clogin(tconfig.CFG_ENV_URL, tconfig.CFG_BUYER_USERNAME, tconfig.CFG_BUYER_PASSWORD)")

def clogin(url, username, password):
    '''登录'''
    act = Alogin(url, username, password)
    act.login()
    