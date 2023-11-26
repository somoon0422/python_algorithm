nums = [ 4,10,22,5,0,17,7,11,9,61,88]
print(f'nums: {nums}')

nums.sort() #API 이용
print(f'nums: {nums}')


searchData = int(input('찾으려는 숫자 입력: '))
searchResertIdx = -1

staIdx = 0
endIdx = len(nums) -1
midIdx = (staIdx + endIdx) //2
midVar = nums[midIdx]

while searchData <= nums[len(nums)-1] and searchData >= nums[0]:
    
    if searchData == nums[len(nums) -1 ]:
        searchResertIdx = len(nums) -1
        break
    
    if searchData > midVar:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVar = nums[midIdx]
    
    elif searchData < midVar:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVar = nums[midIdx]
    
    elif searchData == midVar:
        searchResertIdx = midIdx
        break
    
print(f'searchResultIdx : {searchResertIdx}')