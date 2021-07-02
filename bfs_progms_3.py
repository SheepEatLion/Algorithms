import collections
def solution(begin, target, words):
    length = len(target)
    visited = []
    q = collections.deque()
    q.append((begin, 0))
    while q:
        curr_word, cnt = q.popleft()
        visited.append(curr_word)
        if curr_word == target:
            return cnt
        #  단어들에서 begin의 단어와 한 알파벳과 다를 경우를 탐색.
        for w in words:
            temp_cnt = 0
            if w not in visited:
                for i in range(length):
                    if w[i] == curr_word[i]:
                        temp_cnt += 1
                if temp_cnt == length - 1:
                    q.append((w, cnt + 1))
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
'''
[단어 변환] DFS/BFS 문제
출발 단어와 목표 단어를 가지고 큐브 맞추듯 단어를 변경해가며 목표 단어를 맞추는 문제
결국 모든 조건을 탐색해야하는데, 최소 몇 단계만 거치면 되는지를 구해야해서 BFS가 효과적이라고 판단함.
뭐든 찾아지는 순간, 가장 빠른 것이기때문에 바로 RETURN 해줄 수 있음.
만약 RETURN 없이 큐가 종료된다면 찾을 수 없는 것이므로 0을 리턴함.
주어진 단어들 중에서 하나로만 변경이 가능한데, 그 조건이 한 개의 알파벳만 다를 때이다.
따라서 FOR 문을 활용해 단어들을 꺼내서 알파벳을 인덱싱하고 1의 차이만 있다면 1개만 다른 것이므로
다음 탐색 대상으로 지정해주면 된다.
'''