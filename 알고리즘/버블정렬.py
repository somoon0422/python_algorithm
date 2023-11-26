nums = [10,2,7,21,0]
print(f'not sorted nums: {nums}')

length = len(nums) -1

for i in range(length):
    for j in range(length - i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1] , nums[j] # 좀 더 쉬운 자리바꾸는 방법


print(f'sorted nums: {nums}')
            
        