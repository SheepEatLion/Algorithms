'''import collections
def solution(land):
    #answer = 0
    n = len(land)
    dp = [[-1] * 4 for _ in range(n)]
    for k in range(4):
        dp[0][k] = land[0][k]
    print('시작', dp)
    print('땅', land)
    for i in range(1, n):
        dp[i][0] = max(land[i][1], land[i][2], land[i][3]) + dp[i-1][0]
        dp[i][1] = max(land[i][0], land[i][2], land[i][3]) + dp[i-1][1]
        dp[i][2] = max(land[i][0], land[i][1], land[i][3]) + dp[i-1][2]
        dp[i][3] = max(land[i][0], land[i][1], land[i][2]) + dp[i-1][3]
    print('최종', dp)
    return max(dp[n-1])


print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))'''

'''
[땅 따먹기] - dp
dp 를 하려면, 초기값을 어떻게 줄지 파악해야하고, 점화식을 세워야한다.
n 번째
dp(n) = dp(n-1) + land[n][x] x: max(본인 열 제외 3곳)
1)
dp[1] = land[1][x]
2)
dp[2] = dp[1] + land[2][x]
3)
dp[3] = dp[2] + land[3][x]
'''

def solution(land):
    n = len(land)

    for i in range(1, n):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
    return max(land[n-1])

print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))
