import sys
tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())
    one_cache = [0] * 41
    zero_cache = [0] * 41
    one_cache[0], one_cache[1] = 0, 1
    zero_cache[0], zero_cache[1] = 1, 0
    if n == 0:
        print(1, 0)
        continue
    elif n == 1:
        print(0, 1)
        continue
    for i in range(2, n+1):
        one_cache[i] = one_cache[i-1] + one_cache[i-2]
        zero_cache[i] = zero_cache[i-1] + zero_cache[i-2]
    print(zero_cache[n], one_cache[n])

'''
일반적인 피보나치와는 다르게 n번째 피보나치 수열 값을 구하는 dp문제가 아니라
n번째 수열 값이 0과 1를 몇번 호출하는 지를 dp로 구현해서 푸는 문제다.
간단하게 예시로 확인해보면 0과 1의 호출 또한 피보나치 수열 수식과 같게 동작하는 것을 알 수 있다.
그래서 0과 1에 대한 dp 배열을 만들고 똑같이 실행해주면 된다.
'''