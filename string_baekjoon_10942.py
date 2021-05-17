import sys

#  인풋받고 DP 메모 초기화 (문제가 인덱싱을 1부터 시작하므로 길이를 늘리고 0번째를 버림)
n = int(sys.stdin.readline())
numbers = [0] + list(map(int, sys.stdin.readline().split()))
memo = [[0] * (n+1) for _ in range(n+1)]
m = int(sys.stdin.readline())

#  길이가 0인 경우, 즉 자기자신에 해당하는 경우 1(TRUE)로 메모
for i in range(1, n+1):
    memo[i][i] = 1

#  길이가 1인 경우, 두 값이 같은지 비교하고 같다면 1로 메모
for i in range(1, n):
    if numbers[i] == numbers[i+1]:
        memo[i][i+1] = 1

#  길이가 2이상인 경우, J를 기준으로 I만큼 범위를 넓혀가면서 양 끝값이 같은지 비교하고 그 전의 메모가 1인지 확인한다.
for i in range(2, n):
    for j in range(1, n-i+1):
        if numbers[j] == numbers[i+j] and memo[j+1][i+j-1]:
            memo[j][i+j] = 1

#  출력 구문
for k in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(memo[s][e])


'''
이 문제는 쉬운 듯 보이지만 꾀나 어렵다.
처음엔 단순한 문자열 문제로써 펠린드롬 체크하는 문제처럼 보이는데 막상 돌려보면 시간초과가 난다.
그래서 다시 읽어보니, 시간제한과 메모리제한이 야박하다.
즉, DP 로 풀어야하는 문제라는 뜻이다.

솔직히 나는 펠린드롬을 하도 풀어서 이미 그 방식을 외우다시피 하고 있는데 이게 오히려 독이됐다.
일반적인 펠린드롬을 푸는 방식으로 접근해서는 도저히 DP 형태를 유추할 수가 없다.

일단 예시로 주어지는 입력을 보자.
1 2 1 3 1 2 1
이렇게 1차원 배열이 주어진다.
펠린드롬인지 확인하기 위해선 사실 범위별로 다 해보면 된다.
예를 들어서 0번째 값인 1부터 시작한다면 다음과 같다.
1에서 1(자기자신)까지, 1에서 2까지, 1에서 1까지, 1에서 3까지 ...
이렇게 다 해보면서 메모해두면 어떤 범위가 펠린드롬인지 물었을 때 바로 출력이 가능하다.
여기까지가 최적화구조를 가지고 있는 문제라는 뜻이 된다.
그럼 어떤식으로 메모를 할 것인가를 떠올려야 한다.
즉, 반복 구조를 찾고 그걸 최소화 시켜야한다는 것이다.
실제로 저걸 다 구하는 식으로는 당연히 시간초과가 난다.
주어진 예시로 돌아가보자.
1 2 1 까지의 펠린드롬 여부를 조사한다고 하자
그러면 양 끝이 1로 같기 때문에 가능성이 있다.
그래서 내부를 보니 2가 하나 있어서 펠린드롬이다.
여기서 범위가 홀수일 경우를 생각해낸 분들이 있었다.
그렇게 해도 될 수 있지만 그건 좀 애매하다고 보는게, 이건 DP로 풀어야하는 문제인데 속도가 빠른 언어로 백트래킹을 이용한거라 좋게보진 않는다.
DP의 핵심은 반복되는 구조를 찾아서 점화식을 만들어내는 거다.
다른 예로 1 3 1을 펠린드롬이라고 찾아냈다면
그 다음 2 1 3 1 2 의 경우에는 양 끝이 같은지 비교하고, 같으므로 내부로 들어가는데
내부의 1 3 1이 이미 메모 되어있기 때문에 바로 펠린드롬이라고 할 수 있게 된다.
결국 작은 부분부터 만들어나가면 이후의 범위가 커져도 작은 범위부터 다 확인하는 게 아니라
양 끝만 확인한 뒤에 메모되있는 기록만 찾는 것으로 단 2번만에 끝난다.
그리고 몇가지 초기값만 주면 끝난다.
1. 확인하고자 하는 범위의 길이가 0인경우 == 인덱싱 변수 시작과 끝이 같은 경우
2. 길이가 1인 경우
3. 길이가 2 이상인 경우
이렇게 나눌 수 있고 0인 경우는 즉 자기 자신을 말하는 거니까
전부 펠린드롬임으로 메모에 1처리 해주면 된다.
길이가 1인 경우는 바로 옆에 있는 경우니까 둘이 같은지만 비교해서 메모하면 된다.
3번에 해당하는 2 이상인 경우가 본격적인 DP가 동작하는 부분인데
이 부분은 위에서 언급한 것처럼 2번만에 끝나도록 하면 된다.


'''