import requests
import telegram
import time
import os
from bs4 import BeautifulSoup
import schedule

# txt 파일의 위치 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

chat_id = '1634697207'

# 서버 재부팅 확인용
# bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
# bot = telegram.Bot(bot_token)
# bot.sendMessage(chat_id, text="구름ide 서버 재부팅.")

# bot_token = "5341159894:AAFIDH6BUIyB0gMA3hGoCT2izLVRnG_9yrM"
# bot = telegram.Bot(bot_token)
# bot.sendMessage(chat_id, text="구름ide 서버 재부팅.")

def parsingsites():
    # 일반 공지 읽어옴
    url = 'https://www.mju.ac.kr/mjukr/255/subview.do'
    req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup3 = BeautifulSoup(html, 'html.parser')
    print("완료")
    time.sleep(3)

    # SEP 공지사항 읽어옴
    url = 'https://eciems.mju.ac.kr/eciems/7245/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZWNpZW1zJTJGMTA5NSUyRmFydGNsTGlzdC5kbyUzRg%3D%3D'
    req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup2 = BeautifulSoup(html, 'html.parser')
    print("완료")
    time.sleep(3)

    # 전자과 일반공지 게시판 읽어옴
    #url = 'http://ee.mju.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=ee&dum=dum&boardId=16716221&page=1&command=list'
    url = 'https://ee.mju.ac.kr/ee/8324/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZWUlMkYxMjcyJTJGYXJ0Y2xMaXN0LmRvJTNG'
    req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup1 = BeautifulSoup(html, 'html.parser')
    print("완료")
    time.sleep(3)

    # 진로/취업/창업공지 게시판 읽어옴
    url = 'https://www.mju.ac.kr/mjukr/260/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGbWp1a3IlMkYxNDYlMkZhcnRjbExpc3QuZG8lM0ZwYWdlJTNEMSUyNnNyY2hDb2x1bW4lM0QlMjZzcmNoV3JkJTNEJTI2YmJzQ2xTZXElM0QlMjZiYnNPcGVuV3JkU2VxJTNEJTI2cmdzQmduZGVTdHIlM0QlMjZyZ3NFbmRkZVN0ciUzRCUyNmlzVmlld01pbmUlM0RmYWxzZSUyNmlzVmlldyUzRHRydWUlMjY%3D'
    req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup0 = BeautifulSoup(html, 'html.parser')
    print("완료")
    time.sleep(3)

    # 현장실습지원센터 공지사항 읽어옴
    url = 'https://www.mju.ac.kr/intern/2913/subview.do'
    req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup4 = BeautifulSoup(html, 'html.parser')
    print("완료")

def crawingsties():
    # 일반 공지 크롤링
    nums = soup3.select('td._artclTdNum')
    latest_num3 = nums[i].next

    with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'r+') as f_read:
        compas3 = f_read.readline()
        if compas3 == latest_num3:
            title_latest = nums[i].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
            link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
            final_message = "[일반 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest

            bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
            bot = telegram.Bot(bot_token)

            bot.sendMessage(chat_id, text=final_message)

            with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'w+') as f_write:
                compas_int = int(compas3)
                compas_int = compas_int + 1
                compas_str = str(compas_int)
                f_write.write(compas_str)
                f_write.close()
        f_read.close()
    #print("일반공지 크롤링 완료")

    # SEP 공지사항 크롤링
    nums = soup2.select('td._artclTdNum')
    latest_num2 = nums[i].text.strip()

    with open(os.path.join(BASE_DIR, 'latest_num2.txt'), 'r+') as f_read:
        compas = f_read.readline()
        if compas == latest_num2:
            title_latest = nums[i].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
            link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
            final_message = "[SEP 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest

            bot_token = "5341159894:AAFIDH6BUIyB0gMA3hGoCT2izLVRnG_9yrM"
            bot = telegram.Bot(bot_token)

            bot.sendMessage(chat_id, text=final_message)

            with open(os.path.join(BASE_DIR, 'latest_num2.txt'), 'w+') as f_write:
                compas_int = int(compas)
                compas_int = compas_int + 1
                compas_str = str(compas_int)
                f_write.write(compas_str)
                f_write.close()
        f_read.close()
    #print("SEP 공지사항 크롤링 완료")

    # 전자과 일반공지 게시판 크롤링
    nums = soup1.select('td._artclTdNum')
    latest_num1 = nums[i].next

    with open(os.path.join(BASE_DIR, 'latest_num1.txt'), 'r+') as f_read:
        compas5 = f_read.readline()
        if compas5 == latest_num1:
            title_latest = nums[i].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
            link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
            final_message = "[전자과 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest

            bot_token = "5341159894:AAFIDH6BUIyB0gMA3hGoCT2izLVRnG_9yrM"
            bot = telegram.Bot(bot_token)

            bot.sendMessage(chat_id, text=final_message)

            with open(os.path.join(BASE_DIR, 'latest_num1.txt'), 'w+') as f_write:
                compas_int = int(compas5)
                compas_int = compas_int + 1
                compas_str = str(compas_int)
                f_write.write(compas_str)
                f_write.close()
        f_read.close()
    #print("전자과 일반공지 크롤링 완료")

    # 진로/취업/창업공지 게시판 크롤링
    nums = soup0.select('td._artclTdNum')
    latest_num0 = nums[0].text.strip()

    with open(os.path.join(BASE_DIR, 'latest_num0.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before != latest_num0:
            title_latest = nums[0].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
            link_latest = 'https://www.mju.ac.kr' + nums[0].findNext('a').get('href')
            final_message = "[진로/취업/창업공지 알림]\n\n" + title_latest + "\n\n" + link_latest

            bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
            bot = telegram.Bot(bot_token)

            bot.sendMessage(chat_id, text=final_message)
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest_num0.txt'), 'w+') as f_write:
        f_write.write(latest_num0)
        f_write.close()

    # 현장실습지원센터 공지사항 크롤링
    nums = soup4.select('td._artclTdNum')
    latest_num4 = nums[i].next

    with open(os.path.join(BASE_DIR, 'latest_num4.txt'), 'r+') as f_read:
        compas4 = f_read.readline()
        if compas4 == latest_num4:
            title_latest = nums[i].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
            link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
            final_message = "[현장실습지원센터 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest

            bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
            bot = telegram.Bot(bot_token)

            bot.sendMessage(chat_id, text=final_message)

            with open(os.path.join(BASE_DIR, 'latest_num4.txt'), 'w+') as f_write:
                compas_int = int(compas4)
                compas_int = compas_int + 1
                compas_str = str(compas_int)
                f_write.write(compas_str)
                f_write.close()
        f_read.close()

def onprogram():
    state == 1

def offprogram():
    state == 0

state = 1
while True:
    if state == 0:
        schedule.every().day.at("8:50").do(onprogram())

    if state == 1:
        schedule.every().day.at("17:00").do(offprogram())

# 메인 함수
while True:
    

    parsingsites()
    i=0
    while i < 10:
        crawingsties()
        i = i + 1
        #print(f"{i}사이클 완료")

        if i == 10:
            i = 0
            #print("사이클 초기화")
            time.sleep(600)
            break