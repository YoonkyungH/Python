x = [2, 3, 5, 7, 11]
y = x  # y는 x의 alias
y[2] = 99
print(x)
print(y)
print()


x = [2, 3, 5, 7, 11]
y = list(x)  # list함수의 역할은 list를 복사
             # y는 x의 alias가 아님
y[2] = 4
print(x)
print(y)