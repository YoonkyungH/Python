# list
numbers = [2, 3, 5, 7, 11, 13]
names = ["우식", "지석", "래완", "선호"]

print(names)
print(names[1])  # indexing
print(numbers[0:4])  # list slicing / 0부터 인덱스 3까지임
print(numbers[2:])  # 인덱스 2부터 끝까지
print(numbers[:3])  # 맨 앞부터 인덱스 2까지

new_list = numbers[:3]
print(new_list[2])
print(len(numbers))  # len 길이를 알려줌
numbers.append(100)  # append(추가연산) 추가하고 싶은 값을 넣어줌, 자리를 지정할 수 없음
print(numbers)
print()
del numbers[3]  # del 삭제하고 싶은 인덱스를 지움
print(numbers)
print()
numbers.insert(4, 99)  # insert(삽입연산) 4번 인덱스에 99를 삽입
print(numbers)

print()
new_list = sorted(numbers)
print(new_list)
new_list = sorted(numbers, reverse=True)  # reverse=True로 반대로 정렬, numbers는 건들이지 않음 new_list만 만들어 정렬시킴
print(new_list)

print()
print(numbers.sort())  # sort는 아무것도 return하지 않음. 리스트 자체만 정렬
numbers.sort()
print(numbers)  # 이렇게 해야 원하는 결과를 얻을 수 있음
numbers.sort(revers=True)  # 이렇게 하면 거꾸로 정렬

# sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
# sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬