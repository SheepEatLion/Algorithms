import itertools
import math
def isPrime(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        if n == 2:
            return 1
        else:
            return 0
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return 0
    return 1
def solution(numbers):
    answer = 0
    visited = []
    p = []
    for i in range(1, len(numbers)+1):
        p.extend(list(itertools.permutations(numbers, i)))
    for n in p:
        temp = ''
        for k in n:
            temp += k
        if isPrime(int(temp)) and int(temp) not in visited:
            answer += 1
            visited.append(int(temp))
    return answer

print(solution('17'))

'''
[소수 찾기] - 완전탐색
입력받은 문자 타입의 숫자를 자릿수 별로 나눠서 조합할 수 있는 숫자들을 가지고 소수인지 판별해서
총 몇개의 소수가 나올 수 있는지 출력하는 문제.
itertools 활용해서 조합 구하고 소수 판별 함수를 돌리면 해결.
'''