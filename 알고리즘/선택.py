nums = [4,2,5,1,3]
print(f'nums: {nums}')

for i in range(len(nums)-1):
    minIdx = i #최솟값의 자리
    
    for j in range(i + 1, len(nums)):
        if nums[minIdx] > nums[j]:
            minIdx = j
    
    # tempNum = nums[i]
    # nums[i] = nums[minIdx]
    # nums[minIdx] = tempNum
    
    nums[i], nums[minIdx] = nums[minIdx] , nums[i]
    
    
print(f'nums: {nums}')
            

