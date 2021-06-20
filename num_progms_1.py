import math

def solution(n):
    temp = math.sqrt(n)
    if str(temp) == str(round(temp)) + '.0':
        return pow(int(temp) + 1, 2)
    else:
        return -1
'''
정수 제곱근 판별
'''