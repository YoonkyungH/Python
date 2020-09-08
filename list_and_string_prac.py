# 자릿수 합 구하기
# 자리수 합 리턴 함수
def sum_digit(num):
    total = 0
    str_num = str(num)

    for digit in str_num:
        total += int(digit)

    return total

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit_total = 0
for i in range(1, 1001):
    digit_total += sum_digit(i)

print(digit_total)
print()



# 주민등록번호 가리기
"""
def mask_security_number(security_number):
    num_list = list(security_number)
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = '*'
    return ''.join(num_list)   # ''.join(list) : 리스트에서 문자열로
                               # 방법 1
"""

def mask_security_number(security_number):
    return security_number[:-4] + '****'  # 방법 2 (모범답안)


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))



# 팰린드롬 : "토마토" "기러기"처럼 거꾸로 읽어도 똑같은 단어
def is_palindrome(word):
    for left in range(len(word) // 2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))