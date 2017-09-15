#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import run.case_name_list as namelist
from common.runcase import Run

def startrun(env, browser):
    #------List为要执行的case name, 取至case_name_list.py------
    caselist = []
    caselist.append(namelist.CASE1)
    caselist.append(namelist.CASE2)
    #-------------------------------------------------------
    Run(env, browser, caselist)
