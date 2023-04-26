# 과제 1 - 기준에서 벗어나 있는 데이터 찾기
# 1. YOLO 포맷으로 작성된 텍스트 파일 읽기 (* YOLO 포맷 - label, center_x, center_y, width, height)
# 2. label 값이 38보다 크면서 99가 아닌 경우 기준에서 벗어난 데이터로 간주, 해당 파일명을 리스트에 저장
# 3. 저장된 리스트를 텍스트 파일로 쓰기 (파일명은 'error.txt')

# 과제 2 - 특정 라벨 일괄 수정하기
# 1. 기준에서 벗어나 있지 않은 파일들 중에서 label 값이 99인 경우를 모두 38로 수정하기
# 원래는 99번을 38로 수정하지는 않지만, 확인하기 쉽도록 이번에는 99번을 38번으로 수정하도록 하겠습니다.
import os

file_path = 'C:\\Users\\kimsh-dt01\\Downloads\\modify_txtfile'

def read_files(path, exts):
    files = []    
    for r, d, f in os.walk(path):  
        for file in f:
            if file.lower().endswith(exts):  
                file = os.path.join(r, file) 
                file = os.path.abspath(file) 
                file = file.replace(os.sep, "/")
                files.append(file)
    return files


file_list = read_files(file_path, ('.txt'))

error_list = []
for files in file_list:
    with open(files, 'r') as f:
        lines = f.readlines() #readlines 는 enter를 기준으로 한 줄을 하나의 항목으로 리스트화 함 
        for line in lines:
            # line = line.split()#split 은 인자를 넣지 않고 사용하면 모든 공백(스페이스 여러 칸, \n 등) 을 잘라줌  / (" ") 로 하면 지정한 그대로 스페이스 한 칸을 기준으로 잘라줌
            # print(line[0])
            label, cx, cy, w, h = line.split() # 리스트에 들어 있는 5개 항목을 순서대로 변수에 할당 (언패킹)
            #print(label)
            if int(label) > 38 and int(label) != 99:
                with open('error.txt', 'w') as f:
                    f.write(line)
                    error_list.append(line)
                    

print(error_list)

#미해결