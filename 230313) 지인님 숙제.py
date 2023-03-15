# 0. 바탕화면 폴더의 위치 알아내기
#     (C:\TEST\aaa 이런 평범한 폴더처럼, 바탕화면도 사실 C드라이브 어딘가에 있는 폴더입니다)

# 1. 현재 코드가 위치한 폴더에 hello.txt라는 이름의 텍스트 파일 하나 만들고 그 안에 Hello, World! 라는 문구 작성하기

# 3. 현재 폴더에 만든 hello.txt를 사용자 폴더 (C:\Users) 에 복사하기
# ★. hello.txt 안에 오늘의 날짜와 시간 (코드를 실행한 시점) 이 작성되게 할 수 있을까요?



"""
파이썬 모듈 import 과정

aaa라는 모듈(파이썬 파일) 안에 있는 bb 함수(메소드)를 쓰고 싶을 경우 다음과 같이 쓴다

import aaa
aaa.bb()


그런데 일부 모듈은 모듈명과 함수명이 동일하다 (datetime, tqdm 등)
그럴 경우에는 다음과 같이 쓰이게 된다

import aaa
aaa.aaa()


이게 귀찮거나 헷갈릴 가능성이 있어서 다음과 같은 식으로 쓰기도 한다. from ~ import을 사용해서 불러올 경우
모듈명.함수명() 처럼 불러오는 게 아닌 함수명()으로 바로 불러올 수 있다.
원래는 모듈을 가져오는 거라 모듈을 타고 함수에 접근해야 하지만, 함수를 바로 가져왔기 때문에 모듈을 타지 않고 접근 가능한 것

from aaa import aaa
aaa()

from 모듈명 import 함수명


모듈명과 함수명이 다른 상황에서도 종종 사용된다

from aaa import bb
bb()
"""

import os
import sys
import shutil
import fileinput
from datetime import datetime


src = ".\\hello.txt" # source, 상대 경로로 설정함
dst = "C:\\Users\\hello.txt" # destination, 절대 경로로 설정함 *이 위치로 파일 복사를 하려면 관리자 권한이 필요

# 절대 경로와 상대 경로
# 절대경로 : "C:\\Users\\hello.txt" 처럼, 폴더의 주소창에 붙여넣으면 바로 그 폴더로 이동할 수 있는 경로
# 절대경로로 폴더에 접근하면 어떤 위치에서든 그 폴더로 갈 수 있다
#
# 상대경로 : 현재 폴더를 기준으로 상위/하위 폴더에 접근하는 방법
# ./ 는 현재 폴더를 의미하며 ../는 상위 폴더를 의미한다
# 현재 폴더 안에 있는 하위 폴더 asdf에 접근하고 싶다면 ./asdf 라고 쓰면 된다


nowDatetime = str(datetime.now())


with open(src, "w") as txt:
    txt.write(nowDatetime)
    
# open으로 파일을 읽으려고 할 때는 파일이 존재해야만 한다 (존재하지 않으면 오류남)
# 쓰려고 할 때는 파일이 존재하지 않아도 상관 없다 (존재하지 않으면 새로 하나 만들고, 존재하면 거기다가 덮어쓰거나 이어쓴다)

shutil.copyfile(src,dst) # 파일 처리(이동, 복사, 삭제) 등을 수행하는 모듈

print("Done!")


"""
이 예제의 의미와 기억하길 바라는 것들

1. 바탕화면 폴더의 위치, 바탕화면 폴더에 접근하는 방법
2. 현재 시간 모듈 사용 방법
3. 파이썬 모듈을 불러올 때 import와 from의 차이
4. 절대경로와 상대경로의 의미, 사용법
5. open문 사용법
6. shutil로 파일 복사하는 방법
7. PermissionError : Permission denied 에러 원인과 대처 방법
"""