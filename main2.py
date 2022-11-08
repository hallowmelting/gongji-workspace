import requests
import telegram
import time
import os
from bs4 import BeautifulSoup

# txt 파일의 위치 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

chat_id = '1634697207'

while True:
    # 학사공지 읽어옴
    url = 'https://www.mju.ac.kr/mjukr/257/subview.do'
    req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0'})
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup5 = BeautifulSoup(html, 'html.parser')

    i=0
    while i < 19:
        # 학사공지 크롤링
        nums = soup5.select('td._artclTdNum')
        latest_num5 = nums[i].next

        with open(os.path.join(BASE_DIR, 'latest_num5.txt'), 'r+') as f_read:
            compas5 = f_read.readline()
            if compas5 == latest_num5:
                title_latest = nums[i].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
                link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
                final_message = "[학사공지 알림]\n\n" + title_latest + "\n\n" + link_latest

                bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
                bot = telegram.Bot(bot_token)

                bot.sendMessage(chat_id, text=final_message)

                with open(os.path.join(BASE_DIR, 'latest_num5.txt'), 'w+') as f_write:
                    compas_int = int(compas5)
                    compas_int = compas_int + 1
                    compas_str = str(compas_int)
                    f_write.write(compas_str)
                    f_write.close()
            f_read.close()

        i = i + 1

        if i == 19:
            i = 0
            #print("사이클 초기화")
            time.sleep(600)
            break