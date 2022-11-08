import requests
import telegram
import time
import os
from bs4 import BeautifulSoup

# txt 파일의 위치 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

chat_id = '1634697207'

while True:
    try:
        while True:
            url = 'https://www.sptakorea.com/spta-notice'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'UTF8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

            html = req.text
            soup5 = BeautifulSoup(html, 'html.parser')
            
            latest_title = soup5.find_all('p', attrs={"class" : "bD0vt9 KNiaIk"})
            latest_title = latest_title[0].text

            with open(os.path.join(BASE_DIR, 'latest_title.txt'), 'r+', encoding='utf-8') as f_read:
                current_title = f_read.readline()
                if current_title != latest_title:
                    link_latest = soup5.find('div','JMCi2v blog-post-homepage-link-hashtag-hover-color so9KdE lyd6fK').find('a')['href']

                    final_message = "[SPTA 공지사항 알림]\n\n" + latest_title + "\n\n" + link_latest

                    bot_token = "5711992408:AAENrcwGhPtmGcNfmnri_lbmb7Nyh_LMdFc"
                    bot = telegram.Bot(bot_token)

                    bot.sendMessage(chat_id, text=final_message)

                    with open(os.path.join(BASE_DIR, 'latest_title.txt'), 'w+', encoding='utf-8') as f_write:
                        f_write.write(latest_title)
                        f_write.close()
                        f_read.close()

            time.sleep(7200) # 2시간 마다 사이트에 접속

    except:
        bot_token = "5711992408:AAENrcwGhPtmGcNfmnri_lbmb7Nyh_LMdFc"
        bot = telegram.Bot(bot_token)

        bot.sendMessage(chat_id, text="SPTA 오류 발생. 30분 대기")

        time.sleep(1800) # 오류 발생 시 실행되는 코드, 30분 대기