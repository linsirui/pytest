import inspect

def a():
    listcpinfo = inspect.stack()
    for i in range(len(listcpinfo)):
        print(listcpinfo[i])

a()