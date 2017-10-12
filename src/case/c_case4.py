#!/usr/bin/env python3
#_*_ coding:utf-8 _*_


import time
import json
from common import httprequest
import os
from common import reporter

def run_step(test_env, browser):
    '''执行本case所有步骤, 每个case文件必须包含此函数'''
    #拼接config数据文件路径
    import_string = "src.testdata." + test_env + ".config"
    #拼接
    import_string_case ="src.testdata."+ test_env + ".d_case4"
    tcfg = __import__(import_string, None, None, "config", 0)        #导入某环境配置文件
    tcfg_case = __import__(import_string_case,None,None,"d_case4",0)
   
    url = tcfg_case.REQUEST_URL
    #print("url is", url)
    #获取该接口所需要调用的参数
    pagenum = tcfg_case.PAGENUM
    pagesize = tcfg_case.PAGESIZE
    companyid = tcfg_case.COMPANYID
    #将参数与url path拼接
    jointurl = url + "?pageNum=" + pagenum + "&pageSize=" + pagesize + "&companyId=" + companyid
    #print("jointurl is", jointurl)
    #获取需要传入的header
    requestheader = tcfg_case.REQUEST_HEADER
    #调用httpget，获取接口返回response,并将结果json转换成dict格式，方便读取每个key对应的数据
    response = json.loads(httprequest.httpget(jointurl,requestheader))
    statusresult = response["status"]
    returncode = statusresult["returnCode"]
    #print("the type of response is", type(response))
    #print("the type of result is", type(statusresult))
    #print("status is", statusresult)
    
    #print("return code is", returncode)
    if(returncode =="200"):
        reporter.checkpoint(returncode == "200","用例通过")
    else:
        reporter.checkpoint(returncode!="200","用例失败",returncode)
    #result = json.loads(response)
    










