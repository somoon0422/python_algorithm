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
change_list = []
for file in file_list:
    with open(file, 'r') as f:
        lines = f.readlines() #readlines 는 enter를 기준으로 한 줄을 하나의 항목으로 리스트화 함 
        for line in lines:
            line = line.strip() #strip 은 인자를 넣지 않고 사용하면 양쪽 공백을 제거해줌
            # line = line.split()#split 은 인자를 넣지 않고 사용하면 모든 공백(스페이스 여러 칸, \n 등) 을 잘라줌  / (" ") 로 하면 지정한 그대로 스페이스 한 칸을 기준으로 잘라줌
            # print(line[0])
            label, cx, cy, w, h = line.split() # 리스트에 들어 있는 5개 항목을 순서대로 변수에 할당 (언패킹)
            #print(label)
            if int(label) > 38 and int(label) != 99:
                error_list.append(file)
            else:
                change_list.append(file)

   
with open('error.txt', 'w') as f:
    error_str = '\n'.join(error_list)
    f.write(error_str)
    
    

#-------------------------------------------------------------------------------------------------

#과제2 :특정라벨 일괄 수정하기




# 1. error_list 에 없는 파일들을 list 로 만들기
# 2. change_list 에 있는 것들을 순회를 해야함. 파일을 돌면서 각 파일을 열어 line 을 순회해야 한다.
# 3. line을 검사하면서 조건에 맞는 레이블들을 변경해야 한다.
#    1. line 을 split() 해서 각각의 변수에 할당한다.
#    2. label 이 99 인 경우 label 변수를 38로 변경한다.
#    3. join을 사용해서 label, cx, cy, w, h 를 하나의 line(문자열)로 만든다.
# 4. 변경된 line이든 변경되지 않은 line이든 리스트에 추가한다.
# 5. 리스트 -> 문자열 -> 파일로 저장.
