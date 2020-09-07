# 사전 (dictionary)
# key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary))
print(my_dictionary[3])
my_dictionary[9] = 81
print(my_dictionary)

# 사전에는 딱히 순서라는 개념이 없음
# 사전의 키는 정수일 필요가 없음
my_family = {
    '엄마': '경',
    '아빠': '택',
    '오빠': '석'
}
print(my_family['엄마'])


# 사전 활용법
my_family = {
    '엄마': '경',
    '아빠': '택',
    '오빠': '석'
}

print(my_family.values())
print('경' in my_family.values())  # 원소가 존재하는지 확인

for value in my_family.values():  # 모든 value 출력하기
    print(value)


print(my_family.keys())

print()
for key in my_family.keys():  # 모든 key 출력하기
    print(key)


print()
for key in my_family.keys():  # key와 value 출력하기
    value = my_family[key]
    print(key, value)


print()
for key, value in my_family.items():  # key와 value 출력하기
    print(key, value)