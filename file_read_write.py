
with open('hello.txt', 'r') as f:  # r은 read w는 write
# 읽어들인 파일을 f에 저장
    print(type(f))
    for line in f:
        print(line)
# 줄마다 띄어지는 이유는 "hello python\n" + print문 원래 줄넘기기 가 있기 때문


# strip
# white space란 "" "\t" "\n"
print("       abc       def      ".strip())  # .strip()을 사용하면 앞, 뒤에 있는 공백을 없앰
print("     \t \n abc   def \n\n\n".strip())
print()


with open('hello.txt', 'r') as f:  # r은 read w는 write
    for line in f:
        print(line.strip())



# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split("."))
print(my_string.split(". "))  # my_string에서 특징이 .다음 띄어쓰기 로 되어있기 때문에 split(". ")로 하면 사이의 띄어쓰기 없이 출력할 수 있음
# .split("") 사이에 있는 것을 기준으로 문자열을 나눈다고 생각


full_name = "Kim, Yuna"
print(full_name.split(", "))

name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]
print(first_name, last_name)


print("    \n\n1  \t 2   3    \n 4".split())
numbers = "    \n\n1  \t 2   3    \n 4   ".split()
print(numbers[0] + numbers[1])  # 답은 23 문자열로 출력되기 때문
print(int(numbers[0]) + int(numbers[1]))  # 이렇게 형변환을 해줘야 숫자 +가 돼서 출력


# 파일 쓰기
with open('new_file.txt', 'w') as f:  # 파일을 생성하고 내용을 씀
    f.write("hello world!\nMy name is Y\n")  # 마지막 작성한 글이 파일을 덮어씀


with open('new_file.txt', 'a') as f:  # 기존의 파일에 내용을 추가
    f.write("My number is 010\n")
# new_file이라는 파일이 없으면 만들어서 씀