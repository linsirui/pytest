#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.action.a_login import Alogin

def run_step(test_env):
    '''执行本case所有步骤, 每个case文件必须包含此函数'''
    import_string = "src.testdata." + test_env + ".config"
    tcfg = __import__(import_string, None, None, "config", 0)        #导入某环境配置文件
    clogin(tcfg.CFG_ENV_URL, tcfg.CFG_BUYER_USERNAME, tcfg.CFG_BUYER_PASSWORD)

def clogin(url, username, password):
    '''登录'''
    act = Alogin(url, username, password)
    act.login()
    