# 과제 1 - 기준에서 벗어나 있는 데이터 찾기
# 1. YOLO 포맷으로 작성된 텍스트 파일 읽기 (* YOLO 포맷 - class, center_x, center_y, width, height)
# 2. class 값이 38보다 크면서 99가 아닌 경우 기준에서 벗어난 데이터로 간주, 해당 파일명을 리스트에 저장
# 3. 저장된 리스트를 텍스트 파일로 쓰기 (파일명은 'error.txt')

# 과제 2 - 특정 라벨 일괄 수정하기
# 1. 기준에서 벗어나 있지 않은 파일들 중에서 class 값이 99인 경우를 모두 38로 수정하기
# 원래는 99번을 38로 수정하지는 않지만, 확인하기 쉽도록 이번에는 99번을 38번으로 수정하도록 하겠습니다.
import argparse
import os

error_list = []

f = open('error_txt' , 'w')

def yolo(path):
    for file in path:
        files = os.listdir(file)
        for file2 in files:
            if file2[0] > 38 and file2[0] != 99:
                error_list.append(file2)
                f.write(error_list)
                
parser = argparse.ArgumentParser(description = '폴더명을 입력하세요')

parser.add_argument('--path')
args = parser.parse_args()

#미해결
                
                
                
                
    
    
    
    
