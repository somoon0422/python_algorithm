#(1) 차번 데이터셋 폴더의 모든 이미지 경로를 하나의 리스트에 저장

import os

file_path = 'C:\\Users\\kimsh-dt01\\Downloads\\PlateCut\\Special_Plate'
file_list =[]
filextention = ('.bmp')

for root, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith(filextention):
            file_list.append(file) #file_path의 .bmp파일들을 file_list에 저장
            
for file in file_list:
    if file.endswith(filextention):
        print(os.path.splitext(file)[0].split('_')[0]) #file_list의 .bmp파일일경우 파일명에서 차번만 출력