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