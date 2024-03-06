import os,sys,re
import datetime
import json
import random
try:
  import requests
except ImportError:
  os.system('pip install requests')
else:
  pass
try:
  from colorama import Back, Fore, Fore, Style, init
except ImportError:
  os.system('pip install colorama')
else:
  pass
try:
  import time
except ImportError:
  os.system('pkg install time')
else:
  pass
try:
  from bs4 import BeautifulSoup
except ImportError:
  os.system('pip3 install beautifulsoup4')
else:
  pass
from colorama import Back, Fore, Fore, Style, init
import requests
from bs4 import BeautifulSoup
import time
from time import sleep
import json,ast
os.system('clear')
 
init(autoreset=True)



def pr3(text):
  lines = text.split('\n')
  for line in lines:
      sys.stdout.write(line+'\n')
      sys.stdout.flush()
      sleep(0.1)
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.01)
  print()

def time():
  current_time = datetime.datetime.now()

  time = current_time.strftime("%M:%S")
  return time




def changetoken(red,green,white):
  if not os.path.exists("cache_golike_auth.txt"):
   pass
  else:
    text=f'''{green}BẠN MUỐN DÙNG AUTH CŨ HAY ĐỔI AUTH
{red}[{white}1{red}] ĐỔI AUTH
{red}[{white}2{red}] DÙNG AUTH CŨ'''
    pr3(text)
    changetoken=int(input(f'{red}NHẬP LỰA CHỌN: {green}'))
    if changetoken==1:
      file_name = 'cache_golike_auth.txt'
      if os.path.exists(file_name):
          os.remove(file_name)
    else:
      pass
      







def banner(red,green,blue,yellow,cyan,pink):
  text=f'''
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
'''
 
  pr3(text)
  text=f'''{red}            ┌───────────────────────┐ 
{red}            ║ {green}   GOLIKE - TIKTOK  {red}  ║
{red}            └───────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{red}MỌI NGƯỜI {cyan}CHÚ Ý!!!!
 ~[+]{green}TIỀN SAU KHI LÀM NVỤ SẼ ĐƯỢC CỘNG SAU VÀI PHÚT
 ~[+]{blue}KIỂM TRA KHÔNG THẤY LÊN XU KO PHẢI DO TOOL LỖI 
 ~[+]{pink}MÀ DO HỆ THỐNG GOLIKE CHƯA LOAD!!!
 ~[+]{yellow}CHÚC MỌI NGƯỜI SỬ DỤNG VUI VẺ😘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''
  pr3(text)






def checkver():
  url='https://dameconghe7749.blogspot.com/2023/11/version-golike.html'
  ver=bes4(url)
  return ver












def newtool():
    print(f"{magenta}Version 1.2.0")
    url='https://dameconghe7749.blogspot.com/2023/11/newtool-golike.html'
    inversionlink =bes4(url)
    text=f'''{red}~[+]TOOL ĐÃ CÓ PHIÊN BẢN MỚI {green}VERSION 1.3.0!!!!!!
{red}Hello{green} C25 {red}C25
{red}TikTok:{green}C25Tool    {red}YOUTUBE:{green}C25Tool
  {red}Facebook:{green}C25Tool
{yellow}HOẶC {red}TRUY CẬP {green}LINK {red}DƯỚI ĐỂ TRỰC TIẾP LẤY TOOL:
🔹🔹🔹🔹{inversionlink}🔸🔸🔸🔸'''
    pr3(text)
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    text=f'''~[+]{red}XEM VIDEO CÓ TOOL MỚI NHẤT :
~[+]{red}[1] : {green}Youtube
~[+]{red}[2] : {green}TikTok
~[+]{red}[3] : {green}Facebook
~[+]{red}[4] : {green}LẤY TOOL TRỰC TIẾP'''
    pr3(text)
    selec=int(input('NHẬP LỰA CHỌN CỦA BẠN:'))
    if selec==1:
      url='https://dameconghe7749.blogspot.com/2023/11/yt-golike.html'
      link=bes4(url)
      os.system(f'termux-open-url {link}')       
    elif selec==2:
      url='https://dameconghe7749.blogspot.com/2023/11/tiktok-golike.html'     
      link=bes4(url)
      os.system(f'termux-open-url {link}')
    elif selec==3:
      url='https://dameconghe7749.blogspot.com/2023/11/fb-golike.html'
      link=bes4(url)
      os.system(f'termux-open-url {link}')
    elif selec==4:
      os.system(f'termux-open-url {inversionlink}')


def user():
  response1 = requests.get('https://ghichu.vn/gdhA')
  
  # Kiểm tra xem tải trang thành công hay không (HTTP status code 200 là thành công)
  if response1.status_code == 200:
      # Parse nội dung HTML bằng BeautifulSoup
      soup1 = BeautifulSoup(response1.text, 'html.parser')
  
      # Tìm thẻ <textarea> bằng class 'content'
      textarea = soup1.find('textarea', {'class': 'content'})
  
      # Lấy nội dung bên trong thẻ <textarea>
      if textarea:
          content = textarea.string.strip()  # Sử dụng .string để lấy nội dung 
          count=str(content.count('Key'))
          current_time = datetime.datetime.now()
          time = current_time.strftime("%F")
          
          
          data={'t':content+'\n'+count+'-'+time+key}
          
          
          
          print(requests.post(f'https://ghichu.vn/gdhA',data=data))
      else:
          print(f'{Fore.LIGHTRED_EX}KIỂM TRA MẠNG CỦA BẠN')
def key():
  url='https://run.mocky.io/v3/0265d989-a123-4c50-85eb-da86ff44d357'
  a=requests.get(url).text
  a=ast.literal_eval(a)
  return a





def bes4(url):
  html_source = requests.get(url).text
  soup = BeautifulSoup(html_source, 'html.parser')
  
  # Lấy văn bản từ thẻ meta có thuộc tính property='og:description'
  og_description = soup.find('meta', {'property': 'og:description'})
  if og_description:
      text =og_description['content']
      return text
  else:
      print("Không tìm thấy thẻ meta với thuộc tính property='og:description'")





def checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
 while True :
  while True :
    if not os.path.exists("cache_golike_auth.txt"):
      auth=str(input(f'~[+]{red}NHẬP AUTH:{green} '))
      headers ={
    'Authorization'	:auth,
    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
 }
      check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)
      if check['status']==200:
              name=check['data'][0]['username']
              hea={
'Authorization':auth
}
# Chuỗi JSON đầu vào
              data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text
              try:
                data=json.loads(data)
              except :
                break
              # Tính tổng pending coin
              total_pending_coin = 0
              for key, value in data.items():
                  if isinstance(value, dict) and 'pending_coin' in value:
                      total_pending_coin += value['pending_coin']
              xht=data['current_coin']
              text=f'~[+]{red}SUCCESS'
              text=f'{red}TÊN TÀI KHOẢN: {green} {name}'
              pr(text)
              text=f'{red}XU HIỆN TẠI :{green}{xht}'
              pr(text)
              # In tổng pending coin
              text=f'{red}XU CHỜ DUYỆT:{green}{total_pending_coin}'
              pr(text)
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              text=f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ '
              pr(text)
              nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
              for i, nickname in enumerate(nicknames, start=1):
                  globals()[f'{i}'] = nickname
              # In giá trị của các biến
              for i, nickname in enumerate(nicknames, start=1):
                  text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
                  pr(text)
              with open("cache_golike_auth.txt", "w") as state_file:
                state_file.write(auth)
              return auth,check
      else:
        text=f'~[+]{red}FAIL AUTH KHÔNG CHÍNH XÁC>>{green}VUI LÒNG NHẬP LẠI'
        continue 
    else:
        with open('cache_golike_auth.txt') as f:
            lines = f.readlines()
            auth=lines[0]
            headers ={
          'Authorization'	:auth,
          't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
}
            check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)
            if check['status']==200:
              name =check['data'][0]['username']
              hea={
'Authorization':auth
}
# Chuỗi JSON đầu vào
              data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text
              try:
                data=json.loads(data)
              except :
                break
              # Tính tổng pending coin
              total_pending_coin = 0
              for key, value in data.items():
                  if isinstance(value, dict) and 'pending_coin' in value:
                      total_pending_coin += value['pending_coin']
              xht=data['current_coin']
              text=f'{red}TÊN TÀI KHOẢN: {green} {name}'
              pr(text)
              text=f'{red}XU HIỆN TẠI :{green}{xht}'
              pr(text)
              # In tổng pending coin
              text=f'{red}XU CHỜ DUYỆT:{green}{total_pending_coin}'
              pr(text)
              nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
              for i, nickname in enumerate(nicknames, start=1):
                  globals()[f'{i}'] = nickname
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              text=f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ '
              pr(text)
              # In giá trị của các biến
              for i, nickname in enumerate(nicknames, start=1):
                  text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'
                  pr(text)
                  
            return auth, check




def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :
    
    user_input=input(f'~[+]{random.choice(ranmau)}>{random.choice(ranmau)}>{random.choice(ranmau)}> {green}CHỌN ACC TIKTOK MUỐN CHẠY JOB:{green} ')
    try:
      n = int(user_input)
      if 'data' in check and len(check['data']) >= n:
          idtiktok = check['data'][n-1]['id']
          if idtiktok :
              text=f"{red}ID CỦA NICKNAME SỐ {n} LÀ: {green}{idtiktok}"
              pr(text)
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              return idtiktok 
          else:
              text=f"{red}KHÔNG TÌM THẤY NICKNAME TƯƠNG ỨNG."
              pr(text)
      else:
          continue 
    except ValueError:
          pr(f"{red}VUI LÒNG CHỈ NHẬP SỐ.")
          continue 





def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  job_success=0
  while True :
    while True :
      hea={
      'Authorization':	auth,
      't':	'VFZSWk5VOUVUWHBOVkUxM1QwRTlQUT09'
  }
      a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).text
      try:
        a=json.loads(a)
      except :
        break
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        os.system(f'termux-open-url {link}')
      except :
        break
      for k in range(delay,-1,-1):
        mau=random.choice(ranmau)
        print(f'{green}JOB SUCCESS :{red}{job_success}✅ {random.choice(ranmau)}LOADING  {random.choice(ranmau)}>> {yellow}NVỤ MỚI SAU {random.choice(ranmau)}>> {random.choice(ranmau)}[{k}s]',end='\r')
        sleep(1)
      print(f'{red}ĐANG KIỂM TRA TRẠNG THÁI JOB                ',end='\r')
      headers = {
          'authorization': auth,
          't': 'VFZSWk5VOUVUVFZOVkZsNVRrRTlQUT09',
  }
      
      json_data = {
          'ads_id': id,
          'account_id': idtiktok ,
          'async': True,
          'data': None,
      }
      
      g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
      try:
        g=json.loads(g)
      except :
        break
      if g['status']==200:
        job_success+=1
        print(f'{green}JOB SUCCESS:{red}{job_success}✅ {green}[{startmaxjob}]{cyan} [{time()}] | {random.choice(ranmau)}SUCCESS |  {green}FOLLOW |''',end="\r")
        startmaxjob+=1
        if startmaxjob == maxjob+1:
          print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
          return
      if g['status'] !=200:
        print(f'{green}ĐANG KIỂM TRA LẠI TRẠNG THÁI JOB        ',end="\r")
        sleep(1)
        g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
        try:
          g=json.loads(g)
        except :
          break
        if g['status']==200:
          job_success+=1
          print(f'{green}JOB SUCCESS:{red}❤ {green}[{startmaxjob}]{cyan} [{time()}] | {random.choice(ranmau)}SUCCESS |  {green}FOLLOW |                      ''',end="\r")
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
            return
        if g['status'] !=200:
          print(f'{red}ĐANG BỎ QUA NHIỆM VỤ                   ',end='\r')
          headers = {
              'authorization': auth,
              't': 'VFZSWk5VOUVVWGhQVkZFeFRsRTlQUT09',
          }
          
          json_data = {
              'description': 'Báo cáo hoàn thành thất bại',
              'users_advertising_id': id,
              'type': 'ads',
              'provider': 'tiktok',
              'fb_id': idtiktok ,
              'error_type': 3,
          }
          
          requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)
         
          
          headers = {
              'authorization': auth,
              't': 'VFZSWk5VOUVVWGhQVkZFeFQwRTlQUT09',
     }
          
          json_data = {
              'ads_id': id,
              'object_id': object_id,
              'account_id': idtiktok ,
              'type': 'follow',
          }
          skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
              headers=headers,
              json=json_data,
          )
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'~[+]{green}ĐÃ ĐẠT MAX JOB')
            return 
      
def getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  job_success=0
  while True :
    while True :
      hea={
      'Authorization':	auth,
      't':	'VFZSWk5VOUVUWHBOVkUxM1QwRTlQUT09'
  }
      a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).text
      try:
        a=json.loads(a)
      except :
        break
      try:
        link=a['data']['link']
        id=a['data']['id']
        object_id=a['lock']['object_id']
        if 'video' in link:
          print(f"{red}ĐANG LỌC JOB LIKE                             ",end='\r')
          headers = {
              'authorization': auth,
              't': 'VFZSWk5VOUVVWGhQVkZFeFRsRTlQUT09',
          }
          
          json_data = {
    'description': 'Tôi không muốn làm Job này',
    'users_advertising_id': id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': idtiktok,
    'error_type': 0,
}

          response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)

          
          json_data = {
    'ads_id': id,
    'object_id': object_id,
    'account_id': idtiktok,
    'type': 'like',
}
          response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
)
          break
        os.system(f'termux-open-url {link}')
      except :
        break
      for k in range(delay,-1,-1):
        mau=random.choice(ranmau)
        print(f'{green}JOB SUCCESS :{red}{job_success}✅ {random.choice(ranmau)}LOADING  {random.choice(ranmau)}>> {yellow}NVỤ MỚI SAU {random.choice(ranmau)}>> {random.choice(ranmau)}[{k}s]',end='\r')
        sleep(1)
      print(f'{red}ĐANG KIỂM TRA TRẠNG THÁI JOB                  ',end='\r')
      headers = {
          'authorization': auth,
          't': 'VFZSWk5VOUVUVFZOVkZsNVRrRTlQUT09',
  }
      
      json_data = {
          'ads_id': id,
          'account_id': idtiktok ,
          'async': True,
          'data': None,
      }
      
      g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
      try:
        g=json.loads(g)
      except :
        break
      if g['status']==200:
        job_success+=1
        print(f'{green}JOB SUCCESS:{red}{job_success}✅ {green}[{startmaxjob}]{cyan} [{time()}] | {random.choice(ranmau)}SUCCESS |  {green}FOLLOW |''',end="\r")
        startmaxjob+=1
        if startmaxjob == maxjob+1:
          print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
          return
      if g['status'] !=200:
        print(f'{green}ĐANG KIỂM TRA LẠI TRẠNG THÁI JOB                     ',end="\r")
        sleep(1)
        g = requests.post(
          'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
          headers=headers,
          json=json_data,
      ).text
        try:
          g=json.loads(g)
        except :
          break
        if g['status']==200:
          job_success+=1
          print(f'{green}JOB SUCCESS:{red}❤ {green}[{startmaxjob}]{cyan} [{time()}] | {random.choice(ranmau)}SUCCESS |  {green}FOLLOW |                      ''',end="\r")
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
            return
        if g['status'] !=200:
          print(f'{red}ĐANG BỎ QUA NHIỆM VỤ                   ',end='\r')
          headers = {
              'authorization': auth,
              't': 'VFZSWk5VOUVVWGhQVkZFeFRsRTlQUT09',
          }
          
          json_data = {
              'description': 'Báo cáo hoàn thành thất bại',
              'users_advertising_id': id,
              'type': 'ads',
              'provider': 'tiktok',
              'fb_id': idtiktok ,
              'error_type': 3,
          }
          
          requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)
         
          
          headers = {
              'authorization': auth,
              't': 'VFZSWk5VOUVVWGhQVkZFeFQwRTlQUT09',
     }
          
          json_data = {
              'ads_id': id,
              'object_id': object_id,
              'account_id': idtiktok ,
              'type': 'follow',
          }
          skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
              headers=headers,
              json=json_data,
          )
          startmaxjob+=1
          if startmaxjob == maxjob+1:
            print(f'~[+]{green}ĐÃ ĐẠT MAX JOB')
            return 
      


  
  


  
  
  
  
  

  




  
  
  
  
  
#biến
#green='\033[38;5;10m'
blue='\033[38;5;12m'
cyan='\033[38;5;14m'
white='\033[1;39m'
magenta='\033[38;5;5m'
orange='\033[38;5;202m'
xanhnhat = "\033[1;36m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
xduong = "\033[1;34m"
pink = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
redb="\033[1;31m"
end='\033[0m'
ranmau=(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)


banner(red,green,blue,yellow,cyan,pink)
ver=checkver()


              
              
              
              
if ver == 'Version 1.2.0':
  print(f'{pink}VERSION 1.2.0')
  changetoken(red,green,white) 
  auth,check =checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
  
  idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
  print(f'''~[+]{red}BẠN CÓ MUỐN LỌC JOB LIKE KHÔNG:
{red}[1]:{green}CÓ
{red}[2]:{green}KHÔNG''')
  select_job=int(input(f'{red}NHẬP LỰA CHỌN:{green}'))
  delay =int(input(f'~[+]{red}NHẬP DELAY: {green}'))
  maxjob= int(input(f'~[+]{red}NHẬP MAX JOB: {green}'))
  print(f'{cyan}KHỞI CHẠY NHIỆM VỤ',end='\r')
  sleep(1)
  if select_job==1:
    getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
  else:
    getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
  
else:
  newtool()