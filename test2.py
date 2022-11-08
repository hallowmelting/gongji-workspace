import requests
import telegram
import time
import os
from bs4 import BeautifulSoup
import datetime as dt
from pytz import timezone

url = 'https://www.mju.ac.kr/bbs/mjukr/141/artclList.do'
req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

status = req.status_code

print(status)