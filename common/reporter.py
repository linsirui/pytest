#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''测试结果模块'''
import sys
from os import rename
import inspect

def checkpoint(exp, des="None"):
    '''执行断言并记录到report<.txt>文件中'''
    liststack = inspect.stack()
    filename = liststack[1][1]
    if "case" in filename:   #True表示checkpoint是从case中调用
        casename = filename[filename.rfind("/")+1:len(filename)-3]
    elif "action" in filename:
        casename = liststack[2][1]
        casename = casename[casename.rfind("/")+1:len(casename)-3]
    filename = filename[filename.rfind("/")+1:]
    line = liststack[1][2]
    if exp:
        status = "Pass,"
    else:
        status = "Fail,"
    des = des + ","
    casename = casename + ","
    filename = filename + ","
    if len(status) <= 5:
        status = status.ljust(5)
    if len(des) <= 40:
        des = des.ljust(40)
    if len(casename) <= 20:
        casename = casename.ljust(20)
    if len(filename) <= 20:
        filename = filename.ljust(20)
    strlog = status + des + casename + filename + "line " + str(line) + "\n"
    __writetempresult(strlog)

def __writetempresult(strline):
    path = sys.path[-1] + "/reporter/temp.txt"
    tempresl = open(path, "a", encoding="utf-8", newline="\n")
    tempresl.writelines(strline)
    tempresl.close()

def initreport():
    status = "状态,"
    status = status.ljust(5)
    des = "描述,"
    des = des.ljust(40)
    casename = "用例名,"
    casename = casename.ljust(20)
    filename = "文件名,"
    filename = filename.ljust(20)
    strtitle = status + des + casename + filename + "行号\n"
    #strtitle = "Status, Description, CaseName, FileName, Line"
    __writetempresult(strtitle)

def buidreport(reportname):
    currentname = sys.path[-1] + "/reporter/temp.txt"
    newname = sys.path[-1] + "/reporter/" + reportname
    rename(currentname, newname)
