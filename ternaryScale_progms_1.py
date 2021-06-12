def solution(n):
    answer = ''
    real = 0
    x = 1
    #  입력받은 n에 가장 가까운 3의 제곱수 찾기
    for i in range(100000000):
        if pow(3, i) >= n:
            #  몇 제곱인지 찾았다면 -1씩 해가면서 제곱한 뒤에 저장하기
            for j in range(i, -1, -1):
                answer += str(n // pow(3, j))
                n = n % pow(3, j)
            break
    #  위에 if문을 >= 로 했기 때문에 > 일 경우 앞에 0이 붙어서 제거해주기.
    answer = answer.lstrip('0')
    #  다시 각 자리에 3의 제곱수를 곱하고 더해서 최종결과 10진수 구하기.
    for k in range(len(answer)):
        if answer[k] != 0:
            real = real + (pow(3, k) * int(answer[k]))
    return real
'''
입력받은 10진수를 3진법으로 변환한 뒤, 반전(뒤짚기)시키고 다시 10진수로 변환하여 출력하는 문제;
1200 == (27*1) + (9*2) + (3*0) + (1*0) == 45
3의 제곱수 중에서 가장 근접한 값으로 나누어야함.
'''