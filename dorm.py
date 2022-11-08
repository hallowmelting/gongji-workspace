import requests
import telegram
import time
import os
from bs4 import BeautifulSoup
import datetime as dt
from pytz import timezone

# txt 파일의 위치 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# chat id 설정
chat_id = '1634697207'
chat_id_sumin = '5210842931' # 수민이 아이디

while True:
    x=dt.datetime.now()

    # KST 설정
    W = dt.datetime.now(timezone('Asia/Seoul')).weekday()
    H = dt.datetime.now(timezone('Asia/Seoul')).hour

    if W < 5:
        if 9 <= H <= 18:
            # 식단표 홈페이지 파싱
            url = 'https://dorm.mju.ac.kr/bbs/dorm/961/artclList.do'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

            html = req.text
            soup5 = BeautifulSoup(html, 'html.parser')

            # 게시글 번호 읽어오기
            nums = soup5.select('td._artclTdNum')
            latest_num9 = nums[0].next

            with open(os.path.join(BASE_DIR, 'latest_num9.txt'), 'r+') as f_read:
                compas5 = f_read.readline()
                if compas5 == latest_num9: # 저장된 글번호와 읽어온 글번호가 같으면
                    # 게시글 링크 읽기
                    title_latest = nums[0].findNext('strong').text.replace('\n','').replace('\t','')
                    link_latest = 'https://www.mju.ac.kr' + nums[0].findNext('a').get('href')

                    # 게시글 링크 파싱 후 이미지 링크 읽기
                    req = requests.get(link_latest, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
                    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
                    req.encoding = 'uft-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

                    html = req.text
                    soup5 = BeautifulSoup(html, 'html.parser')
                    imglink1 = soup5.select('img')[0]['src']
                    imglink2 = soup5.select('img')[1]['src']
                    #print(imglink1)
                    #print(imglink2)

                    #final_message = "[식단 알림]\n\n" + title_latest + "\n\n" + link_latest + "\n\n" + imglink

                    bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
                    bot = telegram.Bot(bot_token)

                    #bot.sendMessage(chat_id, text=final_message)
                    bot.sendPhoto(chat_id, photo=imglink1, caption=title_latest)
                    time.sleep(1)
                    bot.sendPhoto(chat_id, photo=imglink2, caption=title_latest)

                    # bot.sendPhoto(chat_id_sumin, photo=imglink1, caption=title_latest)
                    # time.sleep(1)
                    # bot.sendPhoto(chat_id_sumin, photo=imglink2, caption=title_latest)

                    with open(os.path.join(BASE_DIR, 'latest_num9.txt'), 'w+') as f_write:
                        compas_int = int(compas5)
                        compas_int = compas_int + 1
                        compas_str = str(compas_int)
                        f_write.write(compas_str)
                        f_write.close()
                        f_read.close()

    time.sleep(3600) # 한 시간에 한 번 읽음