import heapq
import sys

num = int(input())

card_list = []
for i in range(num):
    heapq.heappush(card_list , int(sys.stdin.readline()))
    
sum = 0
while len(card_list) > 1:
    a = heapq.heappop(card_list)
    b = heapq.heappop(card_list)
    total = a + b
    
    sum += total
    heapq.heappush(card_list, total)
    
print(sum)