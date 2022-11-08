from typing import SupportsComplex
import requests
import telegram
import time
import os
from bs4 import BeautifulSoup

bot_token = "5341159894:AAFIDH6BUIyB0gMA3hGoCT2izLVRnG_9yrM"
bot = telegram.Bot(bot_token)
chat_id = '1634697207'

# txt 파일의 위치 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 서버 재부팅 확인용
bot.sendMessage(chat_id, text="구름ide 서버 재부팅. 소스 확인 할 것")

while True:
# 전자과 일반공지 게시판 크롤링
    req = requests.get('http://ee.mju.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=ee&dum=dum&boardId=16716221&page=1&command=list')
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    nums = soup.select('td.no')
    latest_num1 = nums[0].text.strip()

    with open(os.path.join(BASE_DIR, 'latest_num1.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before != latest_num1:
            title_latest = nums[0].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
            link_latest = 'http://ee.mju.ac.kr/user/' + nums[0].findNext('a').get('href')
            final_message = "[전자과 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest
            bot.sendMessage(chat_id, text=final_message)
            f_read.close()

    with open(os.path.join(BASE_DIR, 'latest_num1.txt'), 'w+') as f_write:
        f_write.write(latest_num1)
        f_write.close()
        time.sleep(1)
        
    # SEP 공지사항 크롤링
    req = requests.get('https://eciems.mju.ac.kr/eciems/7245/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZWNpZW1zJTJGMTA5NSUyRmFydGNsTGlzdC5kbyUzRg%3D%3D')
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    nums = soup.select('td._artclTdNum')
    latest_num2 = nums[6].text.strip()

    with open(os.path.join(BASE_DIR, 'latest_num2.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before != latest_num2:
            title_latest = nums[6].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
            link_latest = 'https://eciems.mju.ac.kr/' + nums[6].findNext('a').get('href')
            final_message = "[SEP 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest
            bot.sendMessage(chat_id, text=final_message)
            f_read.close()

    with open(os.path.join(BASE_DIR, 'latest_num2.txt'), 'w+') as f_write:
        f_write.write(latest_num2)
        f_write.close()
        
        time.sleep(60)