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

# 3. 바탕화면에 만든 hello.txt를 C드라이브 (C:\) 에 복사하기
import os
import sys
import shutil
import fileinput
from datetime import datetime

src = "C:\\Users\\kimsh-dt01\\Desktop\\hello.txt"
dst = "C:\\hello.txt"

shutil.copyfile(src,dst)
# ★. hello.txt 안에 작성할 내용을 Hello, world! 대신 오늘의 날짜와 시간 (코드를 실행한 시점) 이 되게 할 수 있을까요?
nowDatetime = str(datetime.now())

for line in fileinput.input("C:\\hello.txt" , inplace = True):
    if 'Hello, World!' in line:
        line = line.replace(line, nowDatetime)
        
    sys.stdout.write(line)


1. 바탕화면 폴더의 위치, 바탕화면 폴더에 접근하는 방법
2. 현재 시간 모듈 사용 방법
3. 파이썬 모듈을 불러올 때 import와 from의 차이
4. 절대경로와 상대경로의 의미, 사용법
5. open문 사용법
6. shutil로 파일 복사하는 방법
7. PermissionError : Permission denied 에러 원인과 대처 방법
"""