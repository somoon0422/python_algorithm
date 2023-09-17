import sys
import heapq

#보석,가방의 정보
n , k = map(int, sys.stdin.readline().split())

# 보석의 줄만큼 무게,가격 받기
mv_list = []
for _ in range(n):
    m,k = list(map(int, sys.stdin.readline().split()))
    mv_list.append(m,k)
mv_list.sort()

bag_list = []
for _ in range(k):
    c = int(input)
    bag_list.append(d)
bag_list.sort()


