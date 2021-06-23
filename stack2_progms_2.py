def solution(s):
    stack = []
    for v in s:
        #  열린 괄호가 들어왔을 때
        if v == '(':
            stack.append(v)
        #  닫힘 괄호가 들어왔을 때
        else:
            if stack:  # 스택의 탑이 열린 괄호인지 확인한다.(여기선 열린것만 입력받으므로 안해도됨)
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


print(solution('(()('))
'''
[올바른 괄호] - 스택문제
스택을 활용한 괄호 문제는 2가지를 고려해야한다.
1) 스택이 비었을 때 닫힌 괄호가 들어왔다면 거짓이다. (순서가 맞지 않을 경우)
2) 스택이 남은 채로 종료되었다면 거짓이다. (갯수가 맞지 않을 경우)
'''