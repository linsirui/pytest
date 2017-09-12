#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import run.case_name_list as namelist
import run.common as com

#配置被测环境
ENV_CONFIG = "dev"

#------List为要执行的case name, 取至case_name_list.py------
caselist = []
caselist.append(namelist.CASE1)
#-------------------------------------------------------

com.startrun(ENV_CONFIG, caselist)
