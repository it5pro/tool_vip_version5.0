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
luc = "\033[1;32m"
vang = "\033[0;93m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
xam='\033[1;30m'
end='\033[0m'
#đánh dấu bản quyền
tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__SHOP__ = 'nnn'
__ZALO__ = '0779398192'
__ADMIN__ = 'Nguyễn Minh Hùng'
__FACEBOOK__ = 'Nguyễn Minh Hùng(Tricker)'
__VERSION__ = '5.0'
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
os.system("cls" if os.name == "nt" else "clear")
banner()
import json,requests,time
from time import strftime
print("   \033[1;37mo O O    ")                                      
print("  o")              
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Messenger        \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝\033[1;30m'.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mĐếm Lần Yêu Hoặc Sủa")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool Spam Tin Nhắn\033[1;33m(Người Chỉ Định)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool Spam Box Mess\033[1;33m(Nội Dung Theo Ý Muốn)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool War Box Mess")
print("\033[1;30m╠===========================================")


print("   \033[1;37mo O O    ")                                      
print("  o")              
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Trao đổi sub     \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝\033[1;30m'.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TDS Instagram")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TDS Pro5")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool TDS Pro5 Đa Luồng")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool TDS TikTok")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool TDS TikTok + Tiktok Now")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool TDS Full Job")
print("\033[1;30m╠===========================================")


print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Golike           \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝\033[1;30m'.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool Golike TikTok ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mTool Golike Youtube\033[1;33m(bảo trì) ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Golike Facebook\033[1;33m(bảo trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32m.....")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32m.....")
print("\033[1;30m╠===========================================")

#fakebook 16-30
print("   \033[1;37mo O O    ")                                      
print("  o") 
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Facebook         \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝\033[1;30m'.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Buff Follow Bằng Pro5 ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTool Buff Like Bằng Pro5")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;32mTool Buff Cảm Xúc Bằng Pro5")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;32mTool Buff View Story Bằng Pro5")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m20\033[1;31m] \033[1;32mTool Buff Member Group Bằng Pro5 ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m21\033[1;31m] \033[1;32mTool Buff Share Ảo")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m22\033[1;31m] \033[1;32mTool Buff Share Ảo Pro5 - Cookie\033[1;33m(Đa Luồng)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m23\033[1;31m] \033[1;32mTool Buff Share Ảo Pro5 - Token")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m24\033[1;31m] \033[1;32mTool Buff Share Ảo Pro5\033[1;33m(Max Speed)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m25\033[1;31m] \033[1;32mTool Reg Page Vị Trí ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m26\033[1;31m] \033[1;32mTool Reg Page Pro5 + Up AVT")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m27\033[1;31m] \033[1;32mTool Kích Hoạt Pro5")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m28\033[1;31m] \033[1;32mTool Chuyển Page Vị Trí Về Pro5 + Up AVT")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m29\033[1;31m] \033[1;32mTool Tố Cáo Facebook")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m30\033[1;31m] \033[1;32mTool Làm Khoá Acc Facebook\033[1;33m(Bảo Trì)")
print("\033[1;30m╠===========================================")
#tiện ích facebook 31-39
print("   \033[1;37mo O O    ")                                      
print("  o") 
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Tiện Ích Facebook\033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝\033[1;30m'.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m31\033[1;31m] \033[1;32mTool Nuôi Facebook(Like, Join Group Dạo)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m32\033[1;31m] \033[1;32mTool Nuôi Facebook(Like, Add, Cmt Dạo)\033[1;33m(Bảo Trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m33\033[1;31m] \033[1;32mTool Buff Comment")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m34\033[1;31m] \033[1;32mTool Spam Comment Emoji")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m35\033[1;31m] \033[1;32mTool Spam Comment Bằng Pro5")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m36\033[1;31m] \033[1;32mTool Kết Bạn Facebook Gợi Ý")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m37\033[1;31m] \033[1;32mTool Check Liên Kết Facebook\033[1;33m(Bảo Trì) ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m38\033[1;31m] \033[1;32mTool Get ID Facebook\033[1;33m(Bảo Trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m39\033[1;31m] \033[1;32mTag Tên Vào Tiểu Sử")
print("\033[1;30m╠===========================================")
#telegram 40-41
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Telegram         \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m40\033[1;31m] \033[1;32mBuff Member Telegram ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m41\033[1;31m] \033[1;32mTool Spam Box Chat\033[1;33m(Bảo Trì) ")
print("\033[1;30m╠===========================================")
#tiktok 42-47
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Tiktok           \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m42\033[1;31m] \033[1;32mTool Buff View Zefoy ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m43\033[1;31m] \033[1;32mTool Buff View Proxy")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m44\033[1;31m] \033[1;32mTool Buff Tym TikTok\033[1;33m(Bảo Trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m45\033[1;31m] \033[1;32mTool Buff Yêu Thích\033[1;33m(Bảo Trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m46\033[1;31m] \033[1;32mTool Buff Share Ảo TikTok\033[1;33m(Bảo Trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m47\033[1;31m] \033[1;32mTool Buff Comment TikTok\033[1;33m(Bảo Trì)")
print("\033[1;30m╠===========================================")
#Đào bới 48-53
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Đào Bới          \033[1;36m║")
print("\033[1;36m./o--000'-╚═00═══════00════════00══╝.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m48\033[1;31m] \033[1;32mTool Đào Proxy\033[1;33m(Tạm Ổn)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m49\033[1;31m] \033[1;32mTool Đào Proxy 3 Chế Độ\033[1;33m(Pro)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m50\033[1;31m] \033[1;32mTool Lọc Proxy Ver1")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m51\033[1;31m] \033[1;32mTool Lọc Proxy\033[1;33m(Pro)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m52\033[1;31m] \033[1;32mTool Đào Mail ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m53\033[1;31m] \033[1;32mTool Lọc Mail ")
print("\033[1;30m╠===========================================")
#tiện ích ver1 54-62
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTiện Ích Ver1         \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m54\033[1;31m] \033[1;32mTool Reg Garena ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m55\033[1;31m] \033[1;32mTool Bug Vượt Link \033[1;33m(Bảo Trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m56\033[1;31m] \033[1;32mTool Spam SMS")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m57\033[1;31m] \033[1;32mTool Spam SMS + Call Ver1")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m58\033[1;31m] \033[1;32mTool Spam SMS + Call Ver2")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m59\033[1;31m] \033[1;32mTool Tải Video Facebook")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m60\033[1;31m] \033[1;32mTool Tải Video Instagram")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m61\033[1;31m] \033[1;32mTool Tải Video Youtube")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m62\033[1;31m] \033[1;32mTool Tải Video Tiktok")
print("\033[1;30m╠===========================================")
#tiện ích ver2 63-68
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Tiện Ích Ver2    \033[1;36m║")
print("\033[1;36m./o--000'-╚══00══════00════════00══╝.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m63\033[1;31m] \033[1;32mChat GPT\033[1;33m(Bảo Trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m64\033[1;31m] \033[1;32mTool Get Token Pro5")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m65\033[1;31m] \033[1;32mTool Get Token Full Quyền")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m66\033[1;31m] \033[1;32mTool Get Cookie Pro5")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m67\033[1;31m] \033[1;32mToolĐang Update!!")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m68\033[1;31m] \033[1;32mToolĐang Update!!")
print("\033[1;30m╠===========================================")
#game 69-74
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mTool Giải Trí         \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m69\033[1;31m] \033[1;32mTài Xỉu")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m70\033[1;31m] \033[1;32mRắn Săn Mồi")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m71\033[1;31m] \033[1;32mXếp Gạch")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m72\033[1;31m] \033[1;32mSpace Invader")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m73\033[1;31m] \033[1;32mPac-Man")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m74\033[1;31m] \033[1;32mSodoku\033[1;33m(Bảo Trì)")
print("\033[1;30m╠===========================================")
#enc và dec 75-81
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mEncode Và Decode      \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m75\033[1;31m] \033[1;32mTool ENCODE Ver1")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m76\033[1;31m] \033[1;32mTool ENCODE - INPOSTOR\033[1;33m(Bảo Trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m77\033[1;31m] \033[1;32mTool ENCODE - 5 LỚP")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m78\033[1;31m] \033[1;32mTool ENCODE - MARSHAL 16 CHẾ ĐỘ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m79\033[1;31m] \033[1;32mTool ENCODE - Emoji 4 Chế Độ")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m80\033[1;31m] \033[1;32mTool ENCODE - MARSHAL\033[1;33m(Bảo Trì)")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m81\033[1;31m] \033[1;32mTool DECCODE - MARSHAL")
print("\033[1;30m╠===========================================")
#Công cụ 82-86
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;33mCông Cụ Hữu Ích       \033[1;36m║")
print("\033[1;36m./o--000'-╚══00═══════00════════00═╝.o")
print("\033[1;30m╠===========================================")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m82\033[1;31m] \033[1;32mMáy Tính")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m83\033[1;31m] \033[1;32mSetup DDOS")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m84\033[1;31m] \033[1;32mDDOS Ver1")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m85\033[1;31m] \033[1;32mDDOS Ver2")
print("\033[1;30m║\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m86\033[1;31m] \033[1;32mDDOS Ver3\033[1;33m(Bảo Trì)")
print("\033[1;30m╠===========================================")
#Lựa chọn
print("   \033[1;37mo O O    ")                                      
print("  o")   
print("\033[1;36m  TS__[O] ╔════════════════════════╗")
print("\033[1;36m {======| ║  \033[1;34mVui Lòng Chọn Tool    \033[1;36m║")
chon = int(input('\033[1;36m./o--000"-╚\033[1;31m➤\033[1;32m➤\033[1;33m➤\033[1;34m➤  \u001b[32;1m'))
if chon == 1 :
	exec(requests.get('').text)
if chon == 2 :
	exec(requests.get('').text)
if chon == 3 :
	exec(requests.get('').text)
if chon == 4 :
	exec(requests.get('').text)
if chon == 5 :
	exec(requests.get('').text)
if chon == 6 :
	exec(requests.get('').text)
if chon == 7:
	exec(requests.get('').text)
if chon == 8 :
	exec(requests.get('').text)
if chon == 9 :
	exec(requests.get('').text)
if chon == 10 :
	exec(requests.get('').text)
if chon == 11 :
	exec(requests.get('https://run.mocky.io/v3/21d54eb8-b67b-4fde-973f-b728613fcae7').text)
if chon == 12 :
	exec(requests.get('').text)
if chon == 13 :
	exec(requests.get('').text)
if chon == 14 :
	exec(requests.get('').text)
if chon == 15 :
	exec(requests.get('').text)
if chon == 16 :
	exec(requests.get('').text)
if chon == 17 :
	exec(requests.get('').text)
if chon == 18 :
	exec(requests.get('').text)
if chon == 19 :
	exec(requests.get('').text)
if chon == 20 :
	exec(requests.get('').text)
if chon == 21 :
	exec(requests.get('').text)
if chon == 22 :
	exec(requests.get('').text)
if chon == 23 :
	exec(requests.get('').text)
if chon == 24 :
	exec(requests.get('').text)
if chon == 25 :
	exec(requests.get('').text)
if chon == 26 :
	exec(requests.get('').text)
if chon == 27 :
	exec(requests.get('').text)
if chon == 28 :
	exec(requests.get('').text)
if chon == 29 :
	exec(requests.get('').text)
if chon == 30:
	exec(requests.get('').text)
if chon == 31 :
	exec(requests.get('').text)
if chon == 32 :
	exec(requests.get('').text)
if chon == 33 :
	exec(requests.get('').text)
if chon == 34 :
	exec(requests.get('').text)
if chon == 35 :
	exec(requests.get('').text)
if chon == 36 :
	exec(requests.get('').text)
if chon == 37 :
	exec(requests.get('').text)
if chon == 38 :
	exec(requests.get('').text)
if chon == 39 :
	exec(requests.get('').text)
if chon == 40 :
	exec(requests.get('').text)
if chon == 41 :
	exec(requests.get('').text)
if chon == 42 :
	exec(requests.get('').text)
if chon == 43 :
	exec(requests.get('').text)
if chon == 44 :
	exec(requests.get('').text)
if chon == 45 :
	exec(requests.get('').text)
if chon == 46:
	exec(requests.get('').text)
if chon == 47 :
	exec(requests.get('').text)
if chon == 48 :
	exec(requests.get('').text)
if chon == 49 :
	exec(requests.get('').text)
if chon == 50 :
	exec(requests.get('').text)
if chon == 51 :
	exec(requests.get('').text)
if chon == 52 :
	exec(requests.get('').text)
if chon == 53 :
	exec(requests.get('').text)
if chon == 54 :
	exec(requests.get('').text)
if chon == 55 :
	exec(requests.get('').text)
if chon == 56 :
	exec(requests.get('https://run.mocky.io/v3/2d10fe46-574b-4627-807a-f759ae917fa9').text)
if chon == 57 :
	exec(requests.get('').text)
if chon == 58 :
	exec(requests.get('').text)
if chon == 59 :
	exec(requests.get('').text)
if chon == 60 :
	exec(requests.get('').text)
if chon == 61 :
	exec(requests.get('').text)
if chon == 62 :
	exec(requests.get('').text)
if chon == 63 :
	exec(requests.get('').text)
if chon == 64 :
	exec(requests.get('').text)
if chon == 65 :
	exec(requests.get('').text)
if chon == 66 :
	exec(requests.get('').text)
if chon == 67 :
	exec(requests.get('').text)
if chon == 68 :
	exec(requests.get('').text)
if chon == 69 :
	exec(requests.get('').text)
if chon == 70 :
	exec(requests.get('').text)
if chon == 71 :
	exec(requests.get('').text)
if chon == 72 :
	exec(requests.get('').text)
if chon == 73 :
	exec(requests.get('').text)
if chon == 74 :
	exec(requests.get('').text)
if chon == 75 :
	exec(requests.get('').text)
if chon == 76 :
	exec(requests.get('').text)
if chon == 77 :
	exec(requests.get('').text)
if chon == 78 :
	exec(requests.get('').text)
if chon == 79 :
	exec(requests.get('').text)
if chon == 80 :
	exec(requests.get('').text)
if chon == 81 :
	exec(requests.get('').text)
else :
    print("Sai Số")
   