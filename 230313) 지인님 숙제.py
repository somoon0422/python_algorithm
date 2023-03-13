# 1. 바탕화면 폴더의 위치 알아내기
#     (C:\TEST\aaa 이런 평범한 폴더처럼, 바탕화면도 사실 C드라이브 어딘가에 있는 폴더입니다)
# 2. 바탕화면에 hello.txt라는 이름의 텍스트 파일 하나 만들고 그 안에 Hello, World! 라는 문구 작성하기

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

