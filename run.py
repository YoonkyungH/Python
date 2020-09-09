"""
import calculator
# calculator이라는 파이썬 파일을 불러오겠다
# 이렇게 파일을 불러와서 사용할 때는 이 calculator.py를 모듈이라고 함
# 다른 파이썬 파일에서 사용할 수 있는 코드를 모듈이라고 함
# 단, 같은 파일 안에 존재해야 불러올 수 있음
# 이렇게 하면 caculator안에 있는 함수를 사용할 수 있음


print(calculator.add(2, 3))
print(calculator.multiply(5, 6))
"""

# 추천방식 1
"""
import calculator as calc  # calculator라는 모듈을 사용할 때 calc라는 이름으로 대신 사용하겠다는 것

print(calc.multiply(3, 5))
"""


# 추천방식 2
from calculator import add, multiply  # calculator라는 모듈에서 add, multiply 함수만 불러오겠다는 뜻
# 이렇게하면 위의 예제처럼 모듈 이름을 쓰지 않아도 됨

# 또는
# from calculator import *
# *를 사용하면 calculator 안의 모든 함수를 불러오겠다는 뜻이 됨
# 하지만 권장하지 않는 방법. (출처가 불분명해짐)

print(add(2, 4))
print(multiply(5, 6))
