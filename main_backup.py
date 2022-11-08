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
    x = dt.datetime.now()
    # KST 설정
    W = dt.datetime.now(timezone('Asia/Seoul')).weekday()
    H = dt.datetime.now(timezone('Asia/Seoul')).hour

    if W < 5: # 평일에만 작동
        if 9 <= H <= 17: # 작동하는 시간대 9-17
            # 일반 공지 읽어옴
            url = 'https://www.mju.ac.kr/bbs/mjukr/141/artclList.do'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가
            
            html = req.text
            soup3 = BeautifulSoup(html, 'html.parser')
            time.sleep(5)

            # SEP 공지사항 읽어옴
            url = 'https://eciems.mju.ac.kr/bbs/eciems/1095/artclList.do'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

            html = req.text
            soup2 = BeautifulSoup(html, 'html.parser')
            time.sleep(5)

            # 전자과 일반공지 게시판 읽어옴
            url = 'https://ee.mju.ac.kr/bbs/ee/1272/artclList.do'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

            html = req.text
            soup1 = BeautifulSoup(html, 'html.parser')
            time.sleep(5)

            # 진로/취업/창업공지 게시판 읽어옴
            url = 'https://www.mju.ac.kr/bbs/mjukr/146/artclList.do'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

            html = req.text
            soup0 = BeautifulSoup(html, 'html.parser')
            time.sleep(5)

            # 현장실습지원센터 공지사항 읽어옴
            url = 'https://www.mju.ac.kr/bbs/intern/541/artclList.do'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

            html = req.text
            soup4 = BeautifulSoup(html, 'html.parser')
            time.sleep(5)

            # 교육개발센터 공지사항 읽어옴
            url = 'https://www.mju.ac.kr/bbs/ctl/792/artclList.do'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

            html = req.text
            soup5 = BeautifulSoup(html, 'html.parser')
            time.sleep(5)

            # 학생활동공지 읽어옴
            url = 'https://www.mju.ac.kr/bbs/mjukr/853/artclList.do'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

            html = req.text
            soup6 = BeautifulSoup(html, 'html.parser')
            time.sleep(5)

            # 학사 공지 읽어옴
            url = 'https://www.mju.ac.kr/bbs/mjukr/143/artclList.do'
            req = requests.get(url, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

            html = req.text
            soup7 = BeautifulSoup(html, 'html.parser')

            for i in range(18):
                # 일반 공지 크롤링
                nums = soup3.select('td._artclTdNum')
                # latest_num3 = nums[i].next
                latest_num3 = nums[i].text.strip()

                with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'r+') as f_read:
                    pastnum = f_read.readline()
                    if pastnum == latest_num3:
                        title_latest = nums[i].findNext('strong').text.replace('\n','').replace('\t','')
                        link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
                        final_message = "[일반 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest

                        bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
                        bot = telegram.Bot(bot_token)

                        bot.sendMessage(chat_id, text=final_message)
                        bot.sendMessage(chat_id_sumin, text=final_message)
                        # print(latest_num3)

                        with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'w+') as f_write:
                            compas_int = int(pastnum)
                            compas_int = compas_int + 1
                            compas_str = str(compas_int)
                            f_write.write(compas_str)
                            f_write.close()
                            f_read.close()

                # 학사 공지 크롤링
                nums = soup7.select('td._artclTdNum')
                latest_num8 = nums[i].text.strip()

                with open(os.path.join(BASE_DIR, 'latest_num8.txt'), 'r+') as f_read:
                    pastnum = f_read.readline()
                    if pastnum == latest_num8:
                        title_latest = nums[i].findNext('strong').text.replace('\n','').replace('\t','')
                        link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
                        final_message = "[학사 공지 알림]\n\n" + title_latest + "\n\n" + link_latest

                        bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
                        bot = telegram.Bot(bot_token)

                        bot.sendMessage(chat_id, text=final_message)
                        bot.sendMessage(chat_id_sumin, text=final_message)

                        with open(os.path.join(BASE_DIR, 'latest_num8.txt'), 'w+') as f_write:
                            compas_int = int(pastnum)
                            compas_int = compas_int + 1
                            compas_str = str(compas_int)
                            f_write.write(compas_str)
                            f_write.close()
                            f_read.close()

            for i in range(16):
                # SEP 공지사항 크롤링
                nums = soup2.select('td._artclTdNum')
                latest_num2 = nums[i].text.strip()

                with open(os.path.join(BASE_DIR, 'latest_num2.txt'), 'r+') as f_read:
                    pastnum = f_read.readline()
                    if pastnum == latest_num2:
                        title_latest = nums[i].findNext('strong').text.replace('\n','').replace('\t','')
                        link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
                        final_message = "[SEP 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest

                        bot_token = "5341159894:AAFIDH6BUIyB0gMA3hGoCT2izLVRnG_9yrM"
                        bot = telegram.Bot(bot_token)

                        bot.sendMessage(chat_id, text=final_message)
                        # bot.sendMessage(chat_id_sumin, text=final_message)

                        with open(os.path.join(BASE_DIR, 'latest_num2.txt'), 'w+') as f_write:
                            compas_int = int(pastnum)
                            compas_int = compas_int + 1
                            compas_str = str(compas_int)
                            f_write.write(compas_str)
                            f_write.close()
                            f_read.close()
                            
            for i in range(6):
                # 전자과 일반공지 게시판 크롤링
                nums = soup1.select('td._artclTdNum')
                latest_num1 = nums[i].text.strip()

                with open(os.path.join(BASE_DIR, 'latest_num1.txt'), 'r+') as f_read:
                    compas5 = f_read.readline()
                    if compas5 == latest_num1:
                        title_latest = nums[i].findNext('strong').text.replace('\n','').replace('\t','')
                        link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
                        final_message = "[전자과 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest

                        bot_token = "5341159894:AAFIDH6BUIyB0gMA3hGoCT2izLVRnG_9yrM"
                        bot = telegram.Bot(bot_token)

                        bot.sendMessage(chat_id, text=final_message)
                        # bot.sendMessage(chat_id_sumin, text=final_message)

                        with open(os.path.join(BASE_DIR, 'latest_num1.txt'), 'w+') as f_write:
                            compas_int = int(compas5)
                            compas_int = compas_int + 1
                            compas_str = str(compas_int)
                            f_write.write(compas_str)
                            f_write.close()
                            f_read.close()

                # 진로/취업/창업공지 게시판 크롤링
                nums = soup0.select('td._artclTdNum')
                latest_num0 = nums[i].text.strip()

                with open(os.path.join(BASE_DIR, 'latest_num0.txt'), 'r+') as f_read:
                    before = f_read.readline()
                    if before == latest_num0:
                        title_latest = nums[i].findNext('strong').text.replace('\n','').replace('\t','')
                        link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
                        final_message = "[진로/취업/창업공지 알림]\n\n" + title_latest + "\n\n" + link_latest

                        bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
                        bot = telegram.Bot(bot_token)

                        bot.sendMessage(chat_id, text=final_message)
                        bot.sendMessage(chat_id_sumin, text=final_message)

                        with open(os.path.join(BASE_DIR, 'latest_num0.txt'), 'w+') as f_write:
                            compas_int = int(before)
                            compas_int = compas_int + 1
                            compas_str = str(compas_int)
                            f_write.write(compas_str)
                            f_write.close()
                            f_read.close()
            
                # 현장실습지원센터 공지사항 크롤링
                nums = soup4.select('td._artclTdNum')
                latest_num4 = nums[i].text.strip()

                with open(os.path.join(BASE_DIR, 'latest_num4.txt'), 'r+') as f_read:
                    compas4 = f_read.readline()
                    if compas4 == latest_num4:
                        title_latest = nums[i].findNext('strong').text.replace('\n','').replace('\t','')
                        link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
                        final_message = "[현장실습지원센터 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest

                        bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
                        bot = telegram.Bot(bot_token)

                        bot.sendMessage(chat_id, text=final_message)
                        bot.sendMessage(chat_id_sumin, text=final_message)

                        with open(os.path.join(BASE_DIR, 'latest_num4.txt'), 'w+') as f_write:
                            compas_int = int(compas4)
                            compas_int = compas_int + 1
                            compas_str = str(compas_int)
                            f_write.write(compas_str)
                            f_write.close()
                            f_read.close()
                
                # 교육개발센터 공지사항 크롤링
                nums = soup5.select('td._artclTdNum')
                latest_num6 = nums[i].text.strip()

                with open(os.path.join(BASE_DIR, 'latest_num6.txt'), 'r+') as f_read:
                    compas5 = f_read.readline()
                    if compas5 == latest_num6:
                        title_latest = nums[i].findNext('strong').text.replace('\n','').replace('\t','')
                        link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
                        final_message = "[교육개발센터 공지사항 알림]\n\n" + title_latest + "\n\n" + link_latest

                        bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
                        bot = telegram.Bot(bot_token)

                        bot.sendMessage(chat_id, text=final_message)
                        # bot.sendMessage(chat_id_sumin, text=final_message)

                        with open(os.path.join(BASE_DIR, 'latest_num6.txt'), 'w+') as f_write:
                            compas_int = int(compas5)
                            compas_int = compas_int + 1
                            compas_str = str(compas_int)
                            f_write.write(compas_str)
                            f_write.close()
                            f_read.close()

                # 학생활동공지 크롤링
                nums = soup6.select('td._artclTdNum')
                latest_num7 = nums[i].text.strip()

                with open(os.path.join(BASE_DIR, 'latest_num7.txt'), 'r+') as f_read:
                    compas5 = f_read.readline()
                    if compas5 == latest_num7:
                        title_latest = nums[i].findNext('strong').text.replace('\n','').replace('\t','')
                        link_latest = 'https://www.mju.ac.kr' + nums[i].findNext('a').get('href')
                        final_message = "[학생활동공지 알림]\n\n" + title_latest + "\n\n" + link_latest

                        bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
                        bot = telegram.Bot(bot_token)

                        bot.sendMessage(chat_id, text=final_message)
                        bot.sendMessage(chat_id_sumin, text=final_message)

                        with open(os.path.join(BASE_DIR, 'latest_num7.txt'), 'w+') as f_write:
                            compas_int = int(compas5)
                            compas_int = compas_int + 1
                            compas_str = str(compas_int)
                            f_write.write(compas_str)
                            f_write.close()
                            f_read.close()

    time.sleep(600) # 10분마다 접속