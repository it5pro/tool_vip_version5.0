import os
try:
    import requests,colorama,prettytable
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install prettytable")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
tim = "\033[1;40m"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
end='\033[0m'
#đánh dấu bản quyền
hung_ban_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
ebemiz = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config 
__SHOP__ = 'concac.net'
__ZALO__ = '0779398192'
__ADMIN__ = 'NGUYỄN MINH HÙNG'
__FACEBOOK__ = 'NGUYỄN MINH HÙNG'
__VERSION__ = '1.0'
def banner():
 banner = f""" 
\033[1;37m  .-⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦-.
\033[1;37m (    \033[1;35m     .-') _   \033[1;31m _   .-')     \033[1;34m  ('-. .-.    \033[1;37m)
\033[1;37m (    \033[1;35m    ( OO ) )  \033[1;31m( '.( OO )_   \033[1;34m ( OO )  /    \033[1;37m)
\033[1;37m (    \033[1;35m ,--./ ,--,'  \033[1;31m ,--.   ,--.) \033[1;34m ,--. ,--.    \033[1;37m)
\033[1;37m (    \033[1;30m'|░░ \ |░░|\  \033[1;36m '|░░ `.' ░░| \u001b[32;1m '|░░| |░░|   \033[1;37m)
\033[1;37m (    \033[1;30m'|░░░ \|░░| ) \033[1;36m '|░░░░'░░░░| \u001b[32;1m '|░░ .|░░|   \033[1;37m)
\033[1;37m (    \033[1;30m'|░░.░░░░░|/  \033[1;36m '|░░|'.'|░░| \u001b[32;1m '|░░░░░░░|   \033[1;37m)
\033[1;37m (    \033[1;30m'|░░|\░░░░|   \033[1;36m '|░░|   |░░| \u001b[32;1m '|░░.-.░░|   \033[1;37m)
\033[1;37m (    \033[1;30m'|░░| \░░░|   \033[1;36m '|░░|   |░░| \u001b[32;1m '|░░| |░░|   \033[1;37m)
\033[1;37m (    \033[1;30m'`--'  `--'   \033[1;36m `--'   `--' \u001b[32;1m   `--' `--'   \033[1;37m)
\033[1;37m  `-⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦-'
\033[0;37m                        O
\033[0;37m		         o 
\033[1;34m                           ^__^
\033[1;34m                           (oo)\_______
\033[1;34m                           (__)\ \033[0;31mADMIN  \033[1;34m)\/
\033[1;34m                               ||----w |
🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
\033[1;34m╠═══════════════════════════════════════════════
\033[1;32m║➢ Admin : NGUYỄN MINH HÙNG                       
\033[1;36m║➢ Gihul :                    
\033[1;31m║➣ Zalo  : 0779398192               
\033[1;33m║➣ fở Bò :https://www.facebook.com/editpro2k      
\033[1;34m╚═══════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00250)
# =======================[ RUN KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
import json,requests,time
from time import strftime
print("")
print("   \033[1;37mo O O    ")                                      
print("  o")  
print("\033[1;36m  TS__[1] ╔══════════════════════════╗")
print("\033[1;36m {======| ║ \033[1;33mVượt link nhận key free  \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═══╝\033[1;30m'.o")
print("\033[1;30m╠===========================================")
print("   \033[1;37mo O O    ")                                      
print("  o")  
print("\033[1;36m  TS__[2] ╔══════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mKey vip mua ở Admin     \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═══╝\033[1;30m'.o")
print("\033[1;30m╠===========================================")
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;40mVui Lòng Chọn Key     \033[1;36m║")
chon = int(input('\033[1;36m./o--000"-╚\033[1;31m➤\033[1;32m➤\033[1;33m➤\033[1;34m➤  \u001b[32;1m'))
if chon == 1 :
    exec(requests.get('https://raw.githubusercontent.com/it5pro/tool_vip_version5.0/main/KEY/key.py').text)                
if chon == 2 :
    exec(requests.get('https://raw.githubusercontent.com/it5pro/tool_vip_version5.0/main/KEY/keyvip.py').text)
else :
    print("Sai Số")
