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

while True:
    try:
        while True:
            x = dt.datetime.now()
            # KST 설정
            W = dt.datetime.now(timezone('Asia/Seoul')).weekday()
            H = dt.datetime.now(timezone('Asia/Seoul')).hour

            if W < 5: # 평일에만 작동
                if 9 <= H <= 17: # 작동하는 시간대 9-17
                    # 한국전자통신연구원 공지 읽어옴
                    url = 'https://www.etri.re.kr/kor/bbs/list.etri?b_board_id=ETRI01'
                    req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
                    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
                    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가
                    
                    html = req.text
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    for i in range(6):
                        # 한국전자통신연구원 공지 크롤링
                        nums = soup.select('td.num_rwd')
                        latest_num11 = nums[i].text.strip()
                        
                        with open(os.path.join(BASE_DIR, 'latest_num11.txt'), 'r+') as f_read:
                            pastnum = f_read.readline()
                            if pastnum == latest_num11:
                                title_latest = nums[i].findNext('a').text.replace('\n','').replace('\t','')
                                link_latest = 'https://www.etri.re.kr' + nums[i].findNext('a').get('href')
                                final_message = "[한국전자통신연구원]\n\n" + title_latest + "\n\n" + link_latest

                                bot_token = "5695275545:AAExBiOXGi0xMXbdcgwlaMrRzMzZ9Y6WuGU"
                                bot = telegram.Bot(bot_token)

                                bot.sendMessage(chat_id, text=final_message)

                                with open(os.path.join(BASE_DIR, 'latest_num11.txt'), 'w+') as f_write:
                                    compas_int = int(pastnum)
                                    compas_int = compas_int + 1
                                    compas_str = str(compas_int)
                                    f_write.write(compas_str)
                                    f_write.close()
                                    f_read.close()
 
            time.sleep(1800) # 30분마다 접속

    except:
        bot_token = "5695275545:AAExBiOXGi0xMXbdcgwlaMrRzMzZ9Y6WuGU"
        bot = telegram.Bot(bot_token)

        bot.sendMessage(chat_id, text="ETRI 오류 발생. 30분 대기")

        time.sleep(1800) # 오류 발생 시 실행되는 코드, 30분 대기