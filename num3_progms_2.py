def solution(n):
    if n == 1 or n == 2:
        return str(n)
    answer = ''
    #  n을 3으로 나눈 몫이 존재할 경우 while 시작
    while n // 3 >= 1:
        remainder = n % 3  # 현재 n 값으로 나머지 구하기.
        n = n // 3  # n을 현재 n의 몫으로 교체
        # 나머지가 1 또는 2이면 그대로 정답지(문자열)에 삽입
        if remainder == 1 or remainder == 2:
            answer += str(remainder)
        # 나머지가 0이면 윗 자리수에서 끌어와야함으로 4를 삽입한 뒤에 n(몫)을 - 1 해줌.
        if remainder == 0:
            answer += '4'
            n -= 1
    # while 문이 끝난 뒤에, 몫이 1 또는 2가 남아있을 수 있고 그렇다면 정답지에 삽입
    if n == 1 or n == 2:
        answer += str(n)
    # 큐로 전면삽입을 했어도 되지만, 문자열로 받았기 때문에 좌우 반전 시켜서 리턴
    return answer[::-1]


print(solution(16))

'''
1, 2, 4, 11, 12, 14, 21, 22, 24, 41, 42, 44, 111, 112 ... = 124 나라
1, 2, 3,  4,  5,  6,  7,  8,  9, 10, 11, 12,  13,  14 ... = 10진법

만약 for 문을 돌려서 입력받은 10진법의 수를 124 나라의 수로 변경한다면
500,000,000이 입력되었을 때, 시간초과가 날 것이 분명하다.

규칙을 찾아보면, 반드시 1, 2, 4가 일의 자리에 반복되서 나오고 있다.
3번마다 십의 자리가 바뀌고
9번마다 백의 자리가 바뀐다.
그러면 27번마다 천의 자리가 바뀔 것이다.
'''