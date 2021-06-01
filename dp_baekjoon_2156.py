import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
grape = [0]
for _ in range(n):
    grape.append(int(sys.stdin.readline()))
#  예외처리
if n == 1:
    print(grape[1])
    sys.exit()
if n == 2:
    print(grape[1] + grape[2])
    sys.exit()
#  초기값 설정
dp[1] = grape[1]
dp[2] = dp[1] + grape[2]
#  핵심 로직
for i in range(3, n+1):
    dp[i] = max(dp[i-2]+grape[i], dp[i-3]+grape[i-1]+grape[i], dp[i-1])
#  출력
print(dp[n])
'''
규칙1) 선택한 포도주는 다 마셔야하고, 마신 뒤에 제자리에 놓는다.
규칙2) 연속으로 놓여있는 3잔을 모두 마실 순 없다.

포도주 잔의 순서(인덱스) 1  2  3  4  5  6
각 잔에 담긴 포도주 양   6 10 13  9  8  1

최대값인 13을 먹었어야 할 것 같은데,,, 연속으로 3개를 못먹기 때문에 만약 13을 먹으려고 한다면
그 앞에 10 또는 뒤에 9를 포기해야 한다.
최대로 마셔야되니까, 어찌됐건 2개씩 계속 선택하는 게 유리
n = 1 --> 6
n = 2 --> 16
n = 3 --> 10 + 13 = 23
n-3 n-2 n-1 n
n번을 선택했을때 n-3과 n-2를 선택하고 n을 선택하거나
n-3과 n-1을 선택하고 n을 선택해야한다.
dp[n] = max(dp[n-3] + graph[n-1] + grape[n], dp[n-2] + grape[n])
선택하는 가짓수를 보면 예를 들어 A B C 라는 숫자가 있을 때
A B 또는 B C 또는 A C 를 선택해야만 한다.
그래서 C가 곧 n이 되는데, dp[n]으로 나타낸 점화식은 A B의 경우가 없다.
때문에 dp[2]의 초기값이 A+B로 들어가서 dp[n-1]도 점화식에 넣어주면 끝.
'''