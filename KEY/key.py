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
       sleep(0.00250)
menu=f"""
\033[1;36mVượt Link Rút Gọn Giúp Mình Để Nhận Key Free Nhé
\033[1;36mCảm ơn mọi người rất nhiều
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;37m┌─────────────────────┐
\033[1;36m║  \033[1;37m    INPUT KEY FREE\033[1;36m║
\033[1;37m└─────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = """
for h in menu:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0005)
ngay=int(strftime('%d'))
key1=str(ngay*1246881818+2888181472) 
key = 'NMH/'+key1
url = 'https://nguyenminhhungxyz.wpcomstaging.com/?key='+key
token_link1s = '14491af62cfe3cc2cc998f76f96cf8291192fdae'
link1s = requests.get(f'https://traffic1s.com/api?api={token_link1s}&url={url}').json()
if link1s['status']=="error": 
    print(link1s['message'])
    quit()
else:
    link_key=link1s['shortenedUrl']
h=open('keyDEV.txt',mode='a+')
h=open('keyDEV.txt',mode='r')
thien=h.read()
h.close()
print()
if  thien== key:
    print(dau,'\033[1;33mXIN CHÀO \033[1;32m! CHÚC BẠN CHẠY TOOL VUI VẺ...')
    sleep(1)
    exec(requests.get('https://run.mocky.io/v3/4b7dde8d-b9fb-4a4b-9ad3-f7c5f1f811d6').text)
else:
     print(dau,'\033[1;32mTOOL FREE !')
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print(dau ,'\033[1;36mChúc Mọi Người Chạy Tool Vui Vẻ')
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print(dau,'\033[1;33mLINK LẤY API KEY LÀ:\033[1;31m '+link_key)
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =  ')
keynhap = input('\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩ \033[1;32mINPUT API KEY\033[1;33m ~>\033[1;36m ')
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =  ")
if keynhap == key :
    print(dau,'\033[1;32mAPI KEY ĐÚNG OPEN TOOL !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    sleep(2)
    h=open('keyDEV.txt',mode='w')
    h.write(keynhap)
    h.close()
    exec(requests.get('https://run.mocky.io/v3/4b7dde8d-b9fb-4a4b-9ad3-f7c5f1f811d6').text)
else:
    print(dau,'\033[1;33mAPI KEY SAI !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    
