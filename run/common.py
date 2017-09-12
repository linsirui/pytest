#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''run的公用函数模块'''
def startrun(env, caselist):
    '''执行每个case文件的run_step()函数'''
    for index, text in enumerate(caselist):
        import_string = "src.case." + text
        submod = __import__(import_string, None, None, text, 0)  #import要执行的case模块
        submod.run_step(env)        #执行该模块的run_step()函数
