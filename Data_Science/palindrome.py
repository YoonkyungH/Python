# 팔린드롬(palindrome) : 토마토, 기러기와 같은 회문
# for문 사용, append, insert, del 사용 금지

def is_palindrome(word):
    wordlist = list(word)
    j = len(wordlist) - 1
    for i in range(0, len(wordlist) // 2):
        if wordlist[i] != wordlist[j]:
            return False
        elif wordlist[i] == wordlist[j]:
            j -= 1

    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
