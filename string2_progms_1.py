s = "A Z"
n = 1
answer = ''
for i in range(len(s)):
    if s[i] == ' ':
        answer += ' '
        continue
    temp = ord(s[i]) + n
    if s[i].islower():
        if temp <= 122:
            answer += chr(temp)
        else:
            answer += chr((temp - 122) + 96)
    else:
        if temp <= 90:
            answer += chr(temp)
        else:
            answer += chr((temp - 90) + 64)
print(answer)
'''
아스키코드로 범위 지정해서 문자열 이동 후 출력 문제 (시저암호)
'''