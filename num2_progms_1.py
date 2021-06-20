def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))


def solution(n, m):
    answer = []
    if n < m:
        answer.append(gcd(n, m))
        answer.append(lcm(n, m))
    elif m < n:
        answer.append(gcd(m, n))
        answer.append(lcm(m, n))
    return answer


print(solution(3, 12))

'''
최소공배수 = a * b / 최대공약수
최대공약수는 유클리드 호제법으로 구한다.
'''
