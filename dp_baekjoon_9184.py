import sys
memo = dict()
while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if A == -1 and B == -1 and C == -1:
        break
    print('w({}, {}, {}) = '.format(A, B, C), end='')
    def w(a, b, c):
        if (a, b, c) in memo:
            return memo[(a, b, c)]
        if a<=0 or b<=0 or c<=0:
            memo[(a, b, c)] = 1
            return memo[(a, b, c)]
        if a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)
        if a < b < c:
            memo[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return memo[(a, b, c)]
        else:
            memo[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
            return memo[(a, b, c)]
    print(w(A, B, C))

'''
정해진 재귀함수를 dp로 바꾸는 문제이다.
먼저 1, 1, 1의 예시를 보면 다음과 같이 동작한다.
w(0, 1, 1) + w(0, 0, 1) + w(0, 1, 0) - w(0, 0, 0)
w(0, 1, 1) return 1
w(0, 0, 1) return 1
전부 1로 리턴되어 3-1이 됨으로 답은 2가 출력된다.
처음 이 문제를 봤을 때는 방향을 잡지 못했다.
재귀를 dp로 바꿔야 한다고 생각해서 모든 재귀를 다 dp로 어떻게 바꿔야할 지 너무 애매했기 때문이다.
그래서 어쩔 수 없이 다른 분들의 코드를 참고했다.
보니까 전부 dp로 옮기는 게 아니라, 재귀반, dp반 형식으로 이루어져야 하는 거였다.
다시 말해, dp에서의 메모이제이션이라는 특성을 가져와서 재귀는 계속 반복하되 메모를 해나가면서 반복하게 된다.
그리고 재귀가 일어날때 마다 가장 먼저 그 값이 이미 메모 해둔 값인지를 확인한다.
그러면 결국 입력데이터가 쌓일 수록 메모또한 증가하고 해당 메모를 만나면 더 이상 재귀를 하지 않고 정답을 알고 있기 때문에
해당 값을 그대로 리턴하게 되면서 가면 갈수록 재귀를 하는 횟수가 줄어들게 된다.
dp 문제를 풀이할 생각에 dp 로 다 구현해야한다는 고정관념이 있던 것 같다.
이 문제는 재귀를 유지하면서 dp의 특성을 활용해 동작 시간을 최소로 줄여보는 것이 목표였다.
'''