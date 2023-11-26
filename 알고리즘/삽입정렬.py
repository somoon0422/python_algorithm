# 이미 정렬되어 있는 부분에 내 자신이 어디에 들어가야 하는지 판단해서 정렬하는 방식


nums = [5,10,2,1,0]

#ascending
for i1 in range(1,len(nums)):
    i2 = i1 -1 #5
    cNum = nums[i1] #10
    
    while nums[i2] > cNum and i2 >= 0:
        nums[i2 +1] = nums[i2]
        
        i2 -= 1
        
    nums[i2 +1] = cNum


print(f'nums: {nums}')

#descending
nums = [0,5,2,10,1]

for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]
    
    while nums[i2] < cNum and i2 >= 0:
        nums[i2+1] = nums[i2]
        i2 -= 1
    
    nums[i2+1] = cNum
    
    print(f'nums: {nums}')