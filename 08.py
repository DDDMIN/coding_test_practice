#알파벳은 오름차순으로 정렬하고 뒤에 모든 숫자를 더한 값 출력
#K1KA5CB7
#ABCKK13

data = input()
array = []
number = 0

for i in range(len(data)):
    if data[i].isalpha():
        array.append(data[i])
    
    elif data[i].isdigit():
        number += int(data[i])

array.sort()
str_array = ''
for i in range(len(array)):
    str_array += array[i]

str_number = str(number)

print(str_array + str_number)
