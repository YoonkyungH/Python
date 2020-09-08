alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[-1])
# 알파벳 리스트의 슬라이싱
print(alphabet_list[0:5])
print(alphabet_list[4:])
print(alphabet_list[:4])
print()


alphabet_string = 'ABCDEFGHIJ'
print(alphabet_list[-1])
# 알파벳 문자열의 슬라이싱
print(alphabet_list[0:5])  # 새로운 문자열이 생긴 것
print(alphabet_list[4:])
print(alphabet_list[:4])
print()


list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2
print(list_3)


name = 'codeit'
# name[0] = 'C'  # 오류남 ; 문자열은 리스트와 달리 수정 불가
name = 'codeit' + 'it'  # 더하는 것은 아무문제 없이 실행
print(name)


# 알파벳 리스트의 반복문
alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
for alphabet in alphabets_list:
    print(alphabet)

# 알파벳 문자열의 반복문
alphabets_string = 'CODEIT'
for alphabet in alphabets_string:
    print(alphabet)


# 리스트의 길이 재기
print(len(['H', 'E', 'L', 'L', 'O']))

# 문자열의 길이 재기
print(len("Hello, world!"))