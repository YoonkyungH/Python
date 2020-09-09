import datetime
# 이 모듈은 '날짜'와 '시간'을 다루기 위한 다양한 '클래스'를 갖추고 있음

# 2020년 9월 9일을 표현하기
pi_day = datetime.datetime(2020, 9, 9, 14, 33, 10)
print(pi_day)
print(type(pi_day))
print()


# 코드를 실행한 '지금 이 순간'의 날짜와 시간을 받아오려면
today = datetime.datetime.now()
print(today)
print(type(today))