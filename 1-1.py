#1-1모험가 길드 문제

n = int(input())
array = list(map(int, input().split()))
array.sort()  #공포도 오름차순으로 정렬

count = 0
result = 0  #그룹의 숫자

for i in array:
    count += 1 #그룹 구성원 숫자
    if count >= i: #그룹구성원 숫자가 공포도보다 크면 그룹 형성
        result += 1 #그룹 숫자 +1
        count = 0 #그룹 초기화

print(result)
