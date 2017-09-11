#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import pytest
import sys
sys.path.append("/Users/chenlisha/pyprojects/pytest_templete") #项目地址

RUN_NAME = "run_sandbox_allcase" #要执行的run文件名字(不包含后缀.py)

if __name__ == "__main__":
    rel_address = "reporter/rel_" + RUN_NAME + "_"
    rel_address = rel_address + time.strftime("%y%m%d%H%M%S", time.localtime()) + ".txt"
    str_run = "-q run/" + RUN_NAME + ".py --resultlog=" + rel_address
    pytest.main(str_run)
