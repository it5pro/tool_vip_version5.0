import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("clear")
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"
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
for h in banner:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0003)
menu=f"""
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;37m┌─────────────────────┐
\033[1;36m║  \033[1;37m    INPUT KEY \033[1;332mVIP      \033[1;36m║
\033[1;37m└─────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = """
for h in menu:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0005)
key_vip = 'NMH/130225'
h=open('keyvipDEV.txt',mode='a+')
h=open('keyvipDEV.txt',mode='r')
thien=h.read()
h.close()
print()
if thien== key_vip :
    print(dau,'\033[1;33mXIN CHÀO \033[1;32m! CHÚC BẠN CHẠY TOOL VUI VẺ...')
    sleep(1)
    exec(requests.get('https://run.mocky.io/v3/4b7dde8d-b9fb-4a4b-9ad3-f7c5f1f811d6').text)
else:
     print(dau,'\033[1;32mTOOL FREE !')
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print(dau ,'\033[1;36mChúc Mọi Người Chạy Tool Vui Vẻ')
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print(dau,'\033[1;97mNếu bạn ngại vượt link ')
print(dau,'\033[1;97mLiên hệ admin để mua key vip ')
print(dau,'\033[1;97mZalo : 0779398192 ')
print(dau,'\033[1;97mFacebook : https://www.facebook.com/editpro2k')
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =  ')
print("\033[1;34m╔═══════════════════════════════════════╗")
print( "║ Vui Lòng Nhập Key Vip  Để Vào Tool ")
keynhap= input('╚➤➤➤➤ : ' )
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =  ")
if keynhap == key_vip:
    print(dau,'\033[1;32mAPI KEY ĐÚNG OPEN TOOL !.....')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    sleep(2)
    h=open('keyvipDEV.txt',mode='w')
    h.write(keynhap)
    h.close()
    exec(requests.get('https://run.mocky.io/v3/4b7dde8d-b9fb-4a4b-9ad3-f7c5f1f811d6').text)
else:
    print(dau,'\033[1;33mAPI KEY SAI !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    