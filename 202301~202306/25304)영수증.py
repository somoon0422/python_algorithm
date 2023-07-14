total_cost = int(input())  # 총 가격
total_objects = int(input())  # 총 물건 개수
total = 0

for i in range(total_objects):
    object_cost, num_object = map(int, input().split())  # 물건 가격
    total += object_cost * num_object

if total_cost == total:
    print("Yes")
else:
    print("No")


# 미해결
