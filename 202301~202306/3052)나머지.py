<<<<<<< HEAD
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

arr = []
for i in range(10):
    a = int(input())
    arr.append(a % 42)
print(len(set(arr)))
=======
num = []

for i in range(10):
    num.append(int(input()) % 42)
if i == 9:
    print(len(set(num)))
>>>>>>> b0db4c99de1ab1d6adebf6487e504d99108e595d
