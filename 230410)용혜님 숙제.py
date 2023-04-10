#(1) 차번 데이터셋 폴더의 모든 이미지 경로를 하나의 리스트에 저장

import os

file_path = 'C:/Users/kimsh-dt01/Downloads/PlateCut/New_Plate'

file_name_list = []

for file in file_path:
    files = os.walk(file)
    file_name_list.append(files)
print(file_name_list)