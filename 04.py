#주어진 동전을 이용하여 만들수 없는 양의 정수 금액중 최소값을 구하는 프로그램
n = int(input())
data = list(map(int, input().split()))
data.sort

target = 1
for x in data:
    #만들 수 없는 금액을 찾았을 때 반복 종료
    if x > target:
        break
    target += x

#만들 수 없는 금액 출력
print(target)


            
