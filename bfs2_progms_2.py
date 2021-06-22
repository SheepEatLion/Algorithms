import collections
def solution(maps):
    answer = 1e9
    n, m = len(maps), len(maps[0])
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = collections.deque([(0, 0, 1)])
    while q:
        i, j, c = q.popleft()
        if i == m-1 and j == n-1:
            if answer > c:
                answer = c
        for d in dirs:
            dx, dy = i+d[0], j+d[1]
            if dx < 0 or dx >= m or dy < 0 or dy >= n or maps[dy][dx] != 1:
                continue
            maps[dy][dx] = 2
            q.append((dx, dy, c+1))
    if answer < 1e9:
        return answer
    else:
        return -1


print(solution([[1,0,1,1,1,1],[1,0,1,0,1,1],[1,0,1,1,1,1],[1,1,1,0,1,1],[0,0,0,0,1,1]]))

'''
[게임 맵 최단거리] - BFS
0,0 위치에서 출발하여 n,m위치에 도달할 수 있는 최단거리를 찾는 문제.
0은 벽이고 1이 갈 수 있는 곳이다.
dirs 이용해서 동서남북 만들고 c는 카운트 변수다.
answer을 무한대로 초기화해서 최저값의 경로를 찾으면 변경할 수 있게 만들었다.
'''