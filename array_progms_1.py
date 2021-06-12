def solution(arr):
    x = arr[0]
    answer = [x]
    for i in range(1, len(arr)):
        if x != arr[i]:
            x = arr[i]
            answer.append(x)
    return answer

print(solution([1,1,3,3,0,1,1]))

'''
배열의 순서 유지하면서 중복제거하는 문제;
min, max 구하는 방식을 적용해서 풀었다.
초기 값(0번째) 먼저 주고 1번째부터 for 돌게 만들어서 이전의 타겟값 x와 달라지면 append 하고 x값 변경.
'''