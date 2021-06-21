import collections
def solution(progresses, speeds):
    answer = []
    p = collections.deque(progresses)
    s = collections.deque(speeds)
    while p:
        cnt = 0
        if p[0] >= 100:  # 첫번째 작업이 100이 되면
            while p:  # 순서대로 작업을 확인하면서 100이상인 것들은 배포한다.
                if p[0] < 100:
                    break
                p.popleft()
                s.popleft()
                cnt += 1
            answer.append(cnt)  # 배포한 작업의 수를 저장한다.
        #  전체 작업들을 각각의 스피드에 맞게 1일 진행한다.
        for i in range(len(p)):
            p[i] += s[i]
    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
'''
[기능개발] 스택/큐 문제
현재까지 진행된 각 작업들의 진행도가 주어진다.
각 작업들의 진행속도가 주어진다.
100% 진행이 되었더라도 앞의 기능이 아직 배포되지 않았다면 기다려야한다.

프로세스의 [0]번째 인덱스를 계속 확인하고 100이 되면 0번부터 연속적으로 100이상이 된 값들을 내보내고
내보낸 갯수를 cnt 해서 answer 리스트에 append 한다.
'''