total_cost = int(input())  #총 가격
total_objects = int(input()) #총 물건 개수
total = 0

for i in range(1,total_objects+1):
    object_cost, num_object = map(int,input().split()) #물건 가격
    total += object_cost * num_object

if total_cost == total:
    print("yes")
else:
    print("no")
    
        
#미해결