#럭키스트라이크
#123456과 같이 짝수 입력
#앞쪽 절반 숫자 합이랑 뒷쪽 절반 숫자 합이 같으면 LUCKY 출력, 합이 다르면 READY 출력

data = input()

first = 0
second = 0

for i in range(len(data) // 2):
    first += int(data[i])

for i in range((len(data) // 2), len(data)):
    second += int(data[i])

if first == second:
    print("LUCKY")
else:
    print("READY")
