# format을 이용한 문자열 포맷팅
year = 2020
month = 9
day = 1
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

data_string = "오늘은 {}년 {}월 {}일입니다."
print(data_string.format(year, month, day+1))

# format 다루기
print("나는 {1}, {0}, {2}를 좋아한다.".format("귤", "복숭아", "딸기"))
num_1 = 1;num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1/num_2))
name = "윤경";age = 22
print(f"제 이름은 {name}이고 {age}살입니다.") # 새로운 방식(f-string) 파이썬 3.6부터 새롭게 나온 방식. 아직 대중화 안됨.

# 문자열 포맷팅 연습
wage = 5  # 시급 (1시간에 5달러)
exchange_rate = 1142.16  # 환율 (1달러에 1142.16원)
print("{}시간에 {}{} 벌었습니다.".format(1, wage, "달러"))
print("{}시간에 {}{} 벌었습니다.".format(5, 5*wage, "달러"))
print("{}시간에 {:.1f}{} 벌었습니다.".format(1, exchange_rate*wage, "원"))
print("{}시간에 {:.1f}{} 벌었습니다.".format(5, 5*exchange_rate*wage, "원"))