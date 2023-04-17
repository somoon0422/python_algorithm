import os # os 모듈을 가져옴

exts=(".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG")  # 확장자명을 튜플로 저장 

def read_files(path, exts): # path: 폴더 경로, exts: 확장자명 
    files = []  # 파일 경로를 저장할 리스트
    
    for r, d, f in os.walk(path):   # 폴더 경로, 폴더명, 파일명
        for file in f: # 파일명  
            if file.lower().endswith(exts): # 확장자명이 튜플에 있으면 
                file = os.path.join(r, file) # 파일 경로를 생성 
                file = os.path.abspath(file) # 절대 경로로 변환 
                file = file.replace(os.sep, "/") # 경로 구분자를 "/"로 변경 
                files.append(file) # 리스트에 추가 
            
    return files # 파일 경로를 반환 