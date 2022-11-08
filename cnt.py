import requests
import telegram
import time
import os
from bs4 import BeautifulSoup

bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
bot = telegram.Bot(bot_token)
chat_id = '1634697207'

# txt 파일의 위치 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 일반 공지 크롤링
req = requests.get('https://www.mju.ac.kr/mjukr/255/subview.do')
req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

html = req.text
soup = BeautifulSoup(html, 'html.parser')
nums = soup.select('td._artclTdNum')

i=0

while i < 10:
    latest_num3 = nums[i].next

    with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'r+') as f_read:
        compas = f_read.readline()
        if compas == latest_num3:
            print("같다")
        else:
            print("다르다")
            time.sleep(1)
    i = i + 1

print("종료")

# with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'r+') as f_read:
#     compas = f_read.readline()
#     if compas == latest_num3:
#         print("같다")
#     else:
#         print("다르다")
#         time.sleep(1)

# while i < 10:
#     with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'r+') as f_read:
#         compas = f_read.readline()
#         latest_num3 = str(latest_num3)
#         if compas == latest_num3:
#             print("tq")
#             title_latest = nums[i].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
#             link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
#             final_message = "[일반 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest
#             bot.sendMessage(chat_id, text=final_message)

#             with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'w+') as f_write:
#                 compas_int = int(compas)
#                 compas_int = compas_int + 1
#                 compas_str = str(compas_int)
#                 f_write.write(compas_str)
#                 f_write.close()
#         f_read.close()
    
#     i = i + 1
#     if i == 10:
#         i =0
#         time.sleep(1)
#         print("종료")

# print("뭐여")
