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