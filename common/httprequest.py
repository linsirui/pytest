#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

from urllib import request, parse
import json
import os


def httpget(url,header,data=None):
    '''http get request, url为必传参数，url中的参数需要提前拼接好，
    header可根据需要为None get 场景 data不传入'''

    req = request.Request(url)
    if header:
        for k,v in header.items():
            req.add_header(k,v)
    #接口必须添加Authorization header
    fp = open(os.getcwd()+"/usertoken.txt","r")
    authheader = fp.readline()
    req.add_header("Authorization",authheader)
    getapi = request.urlopen(req)
    getresponse = getapi.read().decode('utf-8')
    responsecode = getapi.status
    responsedes = getapi.reason

    #print("response code:",responsecode)
    #print("reason:",responsedes)
    #print("response body is",getresponse)
    getapi.close()
    return getresponse


#httpget('https://api.douban.com/v2/book/2129650',None,None)

def httppost(url,header,data,islogin,authorizationcode=None):
         
    '''url为post api的地址，api地址如果包含参数，需要提前拼接好。
    post 必须传入data. header可根据实际情况可以不传入，即None即可
    当接口为非login接口时，调用post函数需要传入islogin = False, authorizationcode
    需要提前取好，在调取该函数时传入'''
    req = request.Request(url)
    
    if header:
        for (k1,v1) in header.items():
            #print("key and value is",k1,v1)
            req.add_header(k1,v1)
    #data = parse.urlencode(data)
    if (islogin == False):
        req.add_header("Authorization",authorizationcode)
    postapi = request.urlopen(req, data = data.encode('utf-8'))

    responsecode = postapi.status
    responsedes = postapi.reason
    responsebody = postapi.read().decode('utf-8')
    #body = json.loads(responsebody) # 将response转换成dict格式，方便根据key读取具体字段
    #usertoken = body["body"]
    #bearer = usertoken["token"]
    #print ("token type is", type(body))
    #print("user token is", bearer)
    #print("response body is", responsebody)

    #print("response code:",responsecode)
    #print("reason:",responsedes)
    postapi.close()
    return responsebody



