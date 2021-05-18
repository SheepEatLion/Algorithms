import sys

n = int(sys.stdin.readline())
frends_info, cnt = [], []
for i in range(n):
    frends_info.append(sys.stdin.readline().strip())
    cnt.append(frends_info[i].count('Y'))  # 직접 아는 친구 구하기
#  모든 사람과 친구인 사람이 있다면 출력하고 바로 종료
for c in cnt:
    if n - c == 1:
        print(c)
        sys.exit()
#  건너 아는 친구 구하기
for i in range(n):
    for j in range(n):
        if i != j and frends_info[i][j] == 'N':
            for k in range(n):
                if frends_info[i][k] == 'Y':
                    if frends_info[k][j] == 'Y':
                        cnt[i] += 1
                        break
print(max(cnt))
'''
각 층에 속한 사람의 Y의 개수를 구하면 그 사람의 직접적인 친구의 수를 알 수 있다.
N을 만나면, Y에 있는 친구들 중에 그 N을 아는 사람이 있는지 확인해야 한다.
있다면 친구의 친구임으로 내가 아는 친구목록 cnt + 1 해준다.
처음엔 DFS 로 풀려고 했는데 시간도 넉넉하게 줬고 3중 FOR문으로 될거같아서 안했다.
근데 찾아보니 DFS 로 풀기보다도 플로이드 워셜로 풀 수 있다고 한다.
'''