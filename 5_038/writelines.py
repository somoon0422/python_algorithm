# writelines() 는 리스트 또는 튜플 데이터를 반복문 없이 파일에 쓰기 위한 함수이다.

languages =['c/c++', 'java', 'c#', 'python', 'javascript']

uri = './languages.txt'

with open(uri, 'a') as f:
    f.writelines(item + '\n' for item in languages)
        