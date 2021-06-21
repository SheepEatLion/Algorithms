def solution(s):
    stack = []
    for v in s:
        if not stack:
            stack.append(v)
        elif stack[-1] == v:
            stack.pop()
        elif stack[-1] != v:
            stack.append(v)
    if stack:
        return 0
    else:
        return 1

print(solution('baabaa'))
print(solution('cdcd'))
'''
짝지어 제거하기
입력받은 문자열에서 2개가 같은 문자라면 제거한다.
반복했을 때, 모든 문자가 제거 가능하다면 1을 출력하고 아니라면 0를 출력한다.
처음엔 while 문에 for 문으로 풀었지만, 시간초과가 났다.
다시보니 애니팡 처럼 스택구조로 문자를 하나씩 받으면서 일치할 경우 터뜨리는 식으로 진행할 수 있었다.
'''