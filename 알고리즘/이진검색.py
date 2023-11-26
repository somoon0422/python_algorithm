# 정렬되어 있는 자료구조에서 중앙값과 크고 작음을 이용해서 데이터를 검색한다.

datas = [1,2,3,4,5,6,7,8,9,10,11]

print(f'datas: {datas}')
print(f'datas length: {len(datas)}')

searchData = int(input('찾으려는 숫자 입력 : '))
searchResultIdx = -1

staIdx = 0
endIdx = len(datas) -1
midIdx = (staIdx + endIdx) // 2
midVal = datas[midIdx] #가운데 인덱스의 값

while searchData <= datas[len(datas)-1] and searchData >= datas[0]:
    
    if searchData == datas[len(datas)-1]:
        searchResultIdx = len(datas) -1
        break


    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')
        
    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')
        
    elif searchData == midVal:
        searchResultIdx = midIdx
        break


