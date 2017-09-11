#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import run.case_name_list

#配置被测环境
ENV_CONFIG = "sandbox"

#------List为要执行的case name, 取至case_name_list.py------
caselist = []
caselist.append(run.case_name_list.CASE1)
#-------------------------------------------------------

#执行每个case文件的run_step()函数
for index, text in enumerate(caselist):
    import_string = "from src.case." + text + " import run_step" #import模块下所有run_step函数
    exec(import_string)
    exec("run_step(ENV_CONFIG)")
