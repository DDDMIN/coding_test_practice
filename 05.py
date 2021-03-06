n, m = map(int, input().split())
data = list(map(int, input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    #각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
#1 부터 m 까지의 각 무게에 대해 처리
for i in range(1, m + 1):
    n -= array[i] #무게가 i 인 볼링공의 개수 제외(a가 선택할 수 있는 개수)
    result += array[i] * n #b가 선택할 수 있는 갯수(n - array[i])와 곱하기

print(result)
