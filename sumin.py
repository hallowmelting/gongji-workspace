import requests

import time
import os
from bs4 import BeautifulSoup

# txt 파일의 위치 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    # 일반 공지 읽어옴
    url = 'https://www.mju.ac.kr/mjukr/255/subview.do'
    req = requests.get(url, verify=False)
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup3 = BeautifulSoup(html, 'html.parser')

    # SEP 공지사항 읽어옴
    url = 'https://eciems.mju.ac.kr/eciems/7245/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZWNpZW1zJTJGMTA5NSUyRmFydGNsTGlzdC5kbyUzRg%3D%3D'
    req = requests.get(url, verify=False)
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup2 = BeautifulSoup(html, 'html.parser')

    # 전자과 일반공지 게시판 읽어옴
    #url = 'http://ee.mju.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=ee&dum=dum&boardId=16716221&page=1&command=list'
    url = 'https://ee.mju.ac.kr/ee/8324/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZWUlMkYxMjcyJTJGYXJ0Y2xMaXN0LmRvJTNG'
    req = requests.get(url, verify=False)
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup1 = BeautifulSoup(html, 'html.parser')

    # 진로/취업/창업공지 게시판 읽어옴
    url = 'https://www.mju.ac.kr/mjukr/260/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGbWp1a3IlMkYxNDYlMkZhcnRjbExpc3QuZG8lM0ZwYWdlJTNEMSUyNnNyY2hDb2x1bW4lM0QlMjZzcmNoV3JkJTNEJTI2YmJzQ2xTZXElM0QlMjZiYnNPcGVuV3JkU2VxJTNEJTI2cmdzQmduZGVTdHIlM0QlMjZyZ3NFbmRkZVN0ciUzRCUyNmlzVmlld01pbmUlM0RmYWxzZSUyNmlzVmlldyUzRHRydWUlMjY%3D'
    req = requests.get(url, verify=False)
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    req.encoding = 'utf-8'    # clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가

    html = req.text
    soup0 = BeautifulSoup(html, 'html.parser')

    print("사이트 다 읽음")

    i=0
    while i < 10:
        # 일반 공지 크롤링
        nums = soup3.select('td._artclTdNum')
        latest_num3 = nums[i].next

        with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'r+') as f_read:
            compas3 = f_read.readline()
            if compas3 == latest_num3:
                print('\033[96m' + "일반 공지 문자 전송")


                with open(os.path.join(BASE_DIR, 'latest_num3.txt'), 'w+') as f_write:
                    compas_int = int(compas3)
                    compas_int = compas_int + 1
                    compas_str = str(compas_int)
                    f_write.write(compas_str)
                    f_write.close()
            f_read.close()
        print("일반공지 크롤링 완료")

        # SEP 공지사항 크롤링
        nums = soup2.select('td._artclTdNum')
        latest_num2 = nums[i].text.strip()

        with open(os.path.join(BASE_DIR, 'latest_num2.txt'), 'r+') as f_read:
            compas = f_read.readline()
            if compas == latest_num2:
                print('\033[96m' + "SEP 공지사항 문자 전송")


                with open(os.path.join(BASE_DIR, 'latest_num2.txt'), 'w+') as f_write:
                    compas_int = int(compas)
                    compas_int = compas_int + 1
                    compas_str = str(compas_int)
                    f_write.write(compas_str)
                    f_write.close()
            f_read.close()
        print("SEP 공지사항 크롤링 완료")

        # 전자과 일반공지 게시판 크롤링
        nums = soup1.select('td._artclTdNum')
        latest_num1 = nums[0].text.strip()

        with open(os.path.join(BASE_DIR, 'latest_num1.txt'), 'r+') as f_read:
            before = f_read.readline()
            if before != latest_num1:
                print('\033[96m' + "전자과 일반공지 문자 전송")
            f_read.close()

        with open(os.path.join(BASE_DIR, 'latest_num1.txt'), 'w+') as f_write:
            f_write.write(latest_num1)
            f_write.close()
        print("전자과 일반공지 크롤링 완료")

        # 진로/취업/창업공지 게시판 크롤링
        nums = soup0.select('td._artclTdNum')
        latest_num0 = nums[0].text.strip()

        with open(os.path.join(BASE_DIR, 'latest_num0.txt'), 'r+') as f_read:
            before = f_read.readline()
            if before != latest_num0:
                print('\033[96m' + "진로/취업/창업공지 문자 전송")
            f_read.close()

        with open(os.path.join(BASE_DIR, 'latest_num0.txt'), 'w+') as f_write:
            f_write.write(latest_num0)
            f_write.close()
        print("진로/취업/창업공지 크롤링 완료")

        i = i + 1
        print(f"{i}사이클 완료\n")

        if i == 10:
            i = 0
            print("사이클 초기화")
            time.sleep(10)