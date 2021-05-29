import sys
n = int(sys.stdin.readline())
dp = [0] * (n+1)
if n == 1:
    print(0)
    sys.exit()
if n == 2:
    print(1)
    sys.exit()
if n == 3:
    print(1)
    sys.exit()
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
print(dp[n])
'''
0 1 1 2 3 2 3 3 2 3
dp 에 연산횟수를 담는다.
n = 1
print(0)

n = 2
print(1)
-1 연산 또는 //2 연산

n = 3
//3 연산
print(1)

n = 4
//2 연산하고 -1 연산 또는 //2 연산
print(2)

n = 5
-1 연산하고 //2 연산하고 -1 또는 //2 연산
print(3)

n = 6
//2연산 또는 //3연산하고 //2연산 또는 //3연산 또는 -1연산
print(2)
점화식: 
dp[n] = dp[n연산] + 1 
모든 경우를 탐색해봐야한다는게 핵심
'''