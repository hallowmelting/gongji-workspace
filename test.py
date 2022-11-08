# 현재 글번호를 가져온 다음 1을 뺀다
# for문을 돌려서
# 일치하는 숫자가 있으면 -> 글이 삭제되지 않은 상황 -> 
# 일치하는 숫자가 없으면 -> 글이 삭제된 상황 -> 현재 글번호에서 1을 뺀 숫자를 txt파일에 저장

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

# 일반 공지 읽어옴
url = 'https://www.mju.ac.kr/bbs/mjukr/141/artclList.do'
req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

html = req.text
soup3 = BeautifulSoup(html, 'html.parser')

for i in range(18):
    # 삭제된 글 확인
    nums = soup3.select('td._artclTdNum')
    latest_num3 = nums[i].text.strip() # for문을 돌면서 글번호를 i에 저장
    if (latest_num3.isdecimal()): # i가 숫자인지 아닌지 판별
        with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'r+') as f_read: 
            pastnum = f_read.readline() # 저장되어 있는 글번호 pastnum에 저장
            if (int(pastnum)-1 == int(latest_num3)):
                print("조치를 취함")
                break

        f_read.close()

print("크롤링 시작")