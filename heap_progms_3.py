import heapq
def solution(operations):
    answer = []
    for commend in operations:
        c = commend.split(' ')
        if c[0] == 'I':
            #주어진 숫자 삽입
            heapq.heappush(answer, int(c[1]))
        elif c[0] == 'D':
            if answer:
                if int(c[1]) < 0:
                    #최솟값 삭제
                    heapq.heappop(answer)
                else:
                    #최댓값 삭제
                    answer.remove(max(answer))
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))