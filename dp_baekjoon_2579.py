import sys
n = int(sys.stdin.readline())
score = [0]
dp = [0] * (n+1)
for _ in range(n):
    score.append(int(sys.stdin.readline()))
dp[1] = score[1]
if n == 1:
    print(dp[1])
    sys.exit()
dp[2] = score[1] + score[2]
if n == 2:
    print(dp[2])
    sys.exit()
for i in range(3, n+1):
    dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
print(dp[-1])
'''
dp 문제는 적은 수준의 예제를 직접 해보면서 반복구조를 찾아내야 한다.
규칙 3가지
1. 다음 계단 또는 다다음 계단으로만 이동 가능
2. 연속된 계단 3개를 밝을 수 없음.
3. 마지막 계단은 반드시 밟아야함.

계단이 6개일 때 10, 20, 15, 25, 10, 20
10 -> 20 -> 25 -> 20 = 75

dp 에 합 결과를 담으면 됌
마지막 계단 반드시 밟아야하니까 이걸 기준으로 점화식 세워야함
마지막 계단 밟았을 때, 이전 계단을 밟았는 지 아닌지
밟았다면, dp[n] = dp[n-3] + score[n-1] + score[n]
안밟았다면, dp[n] = dp[n-2] + score[n]
초기값은 n이 곧 길이라고 생각하고 dp[1]일때는 1개만 있을때
dp[2]는 두개만 있을때로 가정해서 넣어주면 된다.
참고로 이젠 그냥 1번째부터 인덱싱하는 문제들은 0번째 다 버려야겠다.
괜히 머리아프다.
'''