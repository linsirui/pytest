import json
import os
import re
from common import httprequest

def Run(env, browser, caselist):
    '''执行每个case文件的run_step()函数'''
    GetUserToken(env)
    for index, text in enumerate(caselist):
        import_string = "src.case." + text
        mod= __import__(import_string, None, None, text, 0)  # import要执行的case模块
        mod.run_step(env, browser)  # 执行该模块的run_step()函数


#调用登陆接口，获取用户token值，存储到testdata中的config文件
def GetUserToken(env):
    '''获取用户的token，由于后续接口的token校验'''
    import_string = "src.testdata." + env + ".config"
    tcfg = __import__(import_string, None, None, "config", 0)
    login_url = tcfg.LOGIN_URL
    loginpostdata = json.dumps(tcfg.LOGINPOST_DATA)
    loginrequestheader = tcfg.REQUEST_HEADER
    httpresponse = httprequest.httppost(login_url,loginrequestheader,loginpostdata,True)
    body = json.loads(httpresponse) # 将response转换成dict格式，方便根据key读取具体字段
    usertoken = body["body"]
    bearer = usertoken["token"]
    projectdir = os.getcwd() #获取当前项目路径
    fp = open(projectdir+"/usertoken.txt","w")
    fp.write(bearer)#将token写入项目路径下的usertoken.txt 文件中，方便后续接口调用
    fp.close

    
    



