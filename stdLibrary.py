# standard library (표준 라이브러리)

"""
import math

print(math.log10(100))
print(math.cos(0))
print(math.pi)
"""


"""
import random  # random한 값을 가져다줌

print(random.random())  # 0.0 ~ 1.0 사이의 랜덤한 수를 가져다줌
print(random.randint(1, 20))  # randint는 두 사이의 어떤 랜덤한 정수를 리턴하는 함수 (randint(a,b) -> a<=N<=b인 N값을 리턴)
print(random.uniform(0, 1))  # 두 수 사이의 랜덤한 소수를 리턴하는 함수
# uniform이 randint와 다른 점은 리턴하는 값이 정수가 아니라 소수라는 점
"""


"""
import os  # 운영체제를 조작하기 위한 것

print(os.getlogin())  # 어느 계정에 로그인 되어있는지 알려줌
print(os.getcwd())  # 현재 이 파일이 있는 경로
"""