# range 연습
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for i in range(len(numbers)):
    print(i, numbers[i])
print()


# 거듭제곱
for i in range(11):
    print("{}^{} = {}".format(2, i, 2 ** i))

print()


# for문으로 구구단
for i in range(1, 10):  # 주의사항 : 3~10까지임
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i * j))

print()


# 피타고라스 삼조
for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)

print()


# 리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

numbers.sort(reverse=True)

print("뒤집어진 리스트: " + str(numbers))

# 모범답안
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers) // 2):
    right = len(numbers) - left - 1  # 인덱스 left와 대칭인 인덱스 right 계산
    numbers[right], numbers[left] = numbers[left], numbers[right]  # 위치 바꾸기

print("뒤집어진 리스트: " + str(numbers))
print()