temperature = 15
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다.")


# 학점 계산기(if)
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print("A")
    elif 80 <= total < 90:
        print("B")
    elif 70 <= total < 80:
        print("C")
    elif 60 <= total < 70:
        print("D")
    else:
        print("F")


print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)


# 이상한 수학 문제 1(while and if)
i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
        i += 1
    else:
        i += 1


# 이상한 수학 문제 2(while and if)
i = 1
cnt = 0
while i < 1000:
    if i % 2 == 0:
        cnt += i
        i += 1
    elif i % 3 == 0:
        cnt += i
        i += 1
    else:
        i += 1

print(cnt)


# 약수 찾기
print()
i = 1
cnt = 0
while i <= 120:
    if 120 % i == 0:
        print(i); i += 1; cnt += 1
    else:
        i += 1

print("120의 약수는 총 {}개입니다.".format(cnt))


# 택이의 우승 상금 (while and if)
print()
APARTMENT_PRICE_2016 = 1100000000

year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance += (bank_balance*0.12)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print("{:.0f}원 차이로 동일 아저씨 말씀이 맞습니다.".format(bank_balance-APARTMENT_PRICE_2016))
else:
    print("{:.0f}원 차이로 미란 아주머니 말씀이 맞습니다.".format(APARTMENT_PRICE_2016-bank_balance))


# 피보나치 수열(Fibonacci Sequence)
print()
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1


# 구구단 (while)
print()
i = 1
j = 1
while i <= 9:
    while j <= 9:
        print("{} * {} = {}".format(i, j, i*j))
        j += 1
    i += 1
    j = 1
