
# 1. 파일 읽기
# 파일명이 여러 개 적혀 있는 텍스트 파일 files_to_check.txt를 드릴 거예요.
# 그럼 files_to_check.txt를 읽어와서 (코드 상에서 불러온다는 의미입니다)
# files라는 이름의 리스트에 저장하고 print 해 보세요. 
# (파일 읽는 방법은 with open 관련된 키워드로 검색해 보세요)

# 2. 파일이 존재하는지 확인
# 반복문을 이용해 1에서 만든 files 리스트를 순회하면서 각 파일명이 실제로 존재하는 파일인지,
# 존재하지 않는 파일인지 체크합니다. (os.path.isdir 사용법을 검색해 보세요)

# 3. 읽은 파일을 리스트로 변환
# 존재하지 않는 파일이 발견되었다면 no_files라는 이름으로별도의 리스트를 만들고 
# 해당 파일명들을 저장합니다.

# 4. 파일 쓰기
# 파이썬 파일이 있는 폴더 (상대 경로 기억하시나요?) 안에 none_exist.txt라는 텍스트 파일을 만들고,
# (코드를 이용해 만들어야 합니다) 
# 그 안에 no_files 리스트의 내용을 써 보세요. 
# (파일 쓰는 방법은 지난 시간 복습 또는 with open 관련 키워드로 검색해 보세요)


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


# (다른방법)
# file_path = "C:\\Users\\kimsh-dt01\\Downloads\\read_write\\files_to_check.txt"

# with open(file_path , 'r') as f:
#     files= f.read().splitlines()
    
# print(files)


import os.path

file_path = "D:\\read_write\\files_to_check.txt"

with open(file_path , 'r') as f:
    files = f.readlines() 
# print(files)

no_files = []

for file in files:
    if os.path.isfile(file.strip()) == False:
        no_files.append(file.strip())
        num_files = len(no_files)
print("존재하지 않는 파일은: 총", num_files ,"개 입니다.\n"  ,no_files)

f = open("D:\\read_write\\none_exist.txt", 'w')
f.write(str(no_files))
f.close()
