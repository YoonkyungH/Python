# return과 print 차이
def print_square(x):
    print(x*x)

def get_square(x):
    return x*x

print(print_square(3)) # 함수에 return이 없기 때문에 None이 출력됨.

# optional parameter (dafault value 설정)
# 꼭 마지막에 있어야함
def myself(name, age, nationality="한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)

myself("코드잇", 1, "미국") # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1) # 옵셔널 파라미터를 제공하지 않는 경우

# scope(범위)
def my_function():
    x = 3   # x는 로컬변수. my_function 안에서만 존재
    print(x)

x = 2   # 이 경우 x는 글로벌 변수. 모든 곳에서 사용 가능
def my_function():
    print(x)

# 상수(constant)
PI = 3.14 # 대문자. 실수 없기위함 + 상수와 일반변수를 구분하기 위함

# PEP 8
# 많은 개발자들이 PEP8 스타일 가이드를 따름
# 함수를 정의할 때는 위아래로 빈 줄이 두개씩 있어야 함
# 괄호 안에는 띄어쓰기 하지않기, 함수 이름과 괄호 사이에 띄어쓰기 하지않기
# 지정 연산자 앞뒤로 띄어쓰기 하나씩, 기본적으로 연산자 앞뒤로 띄어쓰기 하나씩
# 하지만 연산의 "우선 순위" 강조를 위해서는 연산자 앞뒤로 붙여쓰는 것을 권장
# 코드 옆에 코멘트 쓸 경우, 코멘트 앞에 띄어쓰기 최소 두 개