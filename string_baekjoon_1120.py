import sys
a, b = sys.stdin.readline().split()
cnt = 0
#  길이가 같다면 바로 차이 연산
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)
    sys.exit()
#  길이가 같지 않을 경우
r = len(b) - len(a) + 1  # 8->6번 7->5번 6->4번
for i in range(r):
    temp = 0
    for j in range(len(a)):
        if a[j] == b[j+i]:
            temp += 1
    if temp > cnt:
        cnt = temp
    if cnt == len(a):
        print(0)
        sys.exit()
print(len(b) - (cnt + (len(b) - len(a))))


'''
문자열 A와 B가 주어진다.
A는 B보다 작거나 같다.
1번연산) A의 앞에 아무 알파벳이나 추가한다.
2번연산) A의 뒤에 아무 알파벳이나 추가한다.
두가지 연산을 통해 길이를 일치시킨 뒤에 A와 B의 문자 차이를 구하라.
단, 가능한 A와 B의 차이가 최소여야 한다.
= 먼저 길이가 같을 경우 바로 차이만 구할 수 있도록 하고 길이가 다를 경우엔 연산을 시작
= 아무 알파벳이나 추가할 수 있지만, 최소가 되려면 B에 있는 걸로 가져오는게 유리하다.
= 그렇게 전부 B에서 가져왔다고 가정하면, 사실 같기때문에 차이 갯수를 구할 필요가 없고
= 실제로 알파벳을 추가하는 연산도 할 필요 없다.
예를들어 ABB A'AAB'CC 라고 한다면, 기존의 A가 B에서 어디에 가장 많이 매칭되는 지만 파악하면 된다.
그 뒤에는 B의 길이 - (매칭된 횟수 + 매칭 부분을 제외한 B의 길이) = 차이
'''