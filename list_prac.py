# 리스트 인덱싱 연습
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1
print()



# 온도 단위 바꾸기
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return ((fahrenheit-32)*5)/9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)  # round (반올림)
    i += 1
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력
print()



# 환전 서비스
# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return round(krw/1000, 1)


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return round(usd*1000/8, 1)


prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

# prices를 원화(￦)에서 달러($)로 변환하기
i = 0
while i < len(prices):
    prices[i] = krw_to_usd(prices[i])
    i += 1

print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)로 변환하기
i = 0
while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i += 1

print("일본 화폐: " + str(prices))