import urllib.request
import time
import requests
import time
import os
import telegram

# 지살남녀 동영상 다운로드 코드
# 11번에 원하는 주차를 입력 후 실행하기

week = 10-1
url1 = "https://contents3.chosun.ac.kr/human/%d/vod/" % week
url2 = ".mp4"

# 동영상 개수 찾기
for a in range(10,100):
    url_full = url1 + str(a).zfill(2) + url2
    req = requests.get(url_full, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    status = req.status_code

    time.sleep(1)
    if status == 404:
        break

# txt파일 생성
print(a)
f = open("C:/Users/tjtjd/OneDrive/바탕 화면/PythonWorkspace/JISAL/file.txt", 'w')
f.close()

f = open("C:/Users/tjtjd/OneDrive/바탕 화면/PythonWorkspace/JISAL/file.txt", 'w')
for i in range(1, a):
    data = "file %d.mp4\n" % i
    f.write(data)
f.close()

# 영상 다운로드
for i in range(1,a):
    url_full = url1 + str(i).zfill(2) + url2
    savename = str(i) +'.mp4'

    urllib.request.urlretrieve(url_full,savename)
    time.sleep(3)

# 영상 합침
# os.system('cmd /k ffmpeg -f concat -i file.txt -c copy 6-1.mp4 ')
os.system('ffmpeg -f concat -i file.txt -c copy %d.mp4') % week

# 동영상 삭제
for i in range(1,a):
    removepath1 = "C:/Users/tjtjd/OneDrive/바탕 화면/PythonWorkspace/JISAL/"
    removepath2 = ".mp4"
    os.remove(removepath1 + str(i) + removepath2)

# 텔레그램으로 완료메세지 전송
chat_id = '1634697207'
bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
bot = telegram.Bot(bot_token)

bot.sendMessage(chat_id, text= str(a) + "merge complete")
