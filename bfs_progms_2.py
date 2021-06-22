import collections

def solution(numbers, target):
    answer = 0
    q = collections.deque([(0, 0)])
    while q:
        result, level = q.popleft()
        print(q)
        print(result, level)
        if level >= len(numbers):
            if result == target:
                answer += 1
            continue
        q.append((result+numbers[level], level+1))
        q.append((result-numbers[level], level+1))
    return answer

print(solution([1, 1, 1, 1, 1], 3))