import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

S_length = len(S)

while S_length != len(T):
    temp = T[-1]
    T = T[:-1]
    if temp == 'B':
        T = T[::-1]
if S == T:
    print(1)
else:
    print(0)

'''
1. 현재 문자열에 A를 붙이는 연산
2. 현재 문자열을 뒤집고 B를 붙이는 연산

B  기존 문자열
BA   1연산
ABB   2연산
ABBA(일치)   1연산
ABBA(목표)

A   (출발)
AB
BAB (틀림)
BBBA(목표)

XXXXXXB
XXXXXX [::-1]
XXXXXA
XXXXX
XXXXB
XXXX [::-1]
XXXB
XXB [::-1]
AB
각 연산을 시도해가면서 매칭하기엔 경우의 수가 너무 크기때문에
무언가 규칙이 있을거라 생각하고 예시를 나열해봄.
연산하는 과정에서 현재 문자열이 목표 문자열에 없다면 불가능한 것이고
있다면 계속 연산을 진행해도 괜찮다는 것을 발견함.
근데 2가지의 예제를 가지고 해본거라 무작정 시도하기엔 확신이 없었음.
게다가 최악의 경우 연산을 거의 끝까지 하다가 false가 날 수도 있는데
그러면 횟수당 연산이 2회기때문에 그럼 효율이 너무 안좋을 것 같았음.
다행히 입력이 아주 크진 않고 시간도 넉넉한 문제라서
그냥 그렇게 해볼까 하다가, 우연히 그냥 맨앞과 맨뒤의 값에 뭔가 있지 않을까 싶어짐.
그래서 먼저 맨 뒷값으로 쭉 나열해봤는데 목표값의 맨 뒤부터 출발하면
이미 특정 연산이 되어있는 거라서 횟수당 1회만 연산을 해도 괜찮다는 걸 알게됌.
따라서 평균적으로 이게 더 나은 알고리즘이라고 생각하고 구현함.
주어진 출발값(S)와 목표값(T)을 바꿔서
T에서 S를 찾아가는 방식으로 역 연산을 진행하여 해결.
'''
