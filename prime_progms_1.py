import math
import itertools
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

def solution(nums):
    answer = 0
    for v in list(itertools.combinations(nums, 3)):
        #print('logs', sum(v))
        answer += isPrime(sum(v))
    return answer

print(solution([1, 2, 3, 4]))
'''
배열에서 3개를 고르고 소수인지 판별해서 맞다면 cnt += 1 해준다.
'''