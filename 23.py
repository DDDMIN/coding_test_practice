n = int(input())
students = []
for _ in range(n):
    #이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    students.append(input().split())

#정렬기준
# 1) 두 번째 원소를 기준으로 내림차순 정렬
# 2) 두 번째 원소가 같은 경우 세 번째 원소를 기준으로 오름차순 정렬
# 3) 세 번째 원소가 같은 경우 네 번째 원소를 기준으로 내림차순 정렬
# 4) 네 번째 원소가 같은 경우 첫 번재 원소를 기준으로 오름차순 정렬

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
