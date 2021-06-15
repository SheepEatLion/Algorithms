import sys
import collections
inp = sys.stdin.readline
INF = int(1e9)

N, M = map(int, inp().split())
dist = [INF] * (N + 1)
graph = []

for _ in range(M):
    a, b, c = map(int, inp().split())
    graph.append((a, b, c))  # 벨만포드는 다익스트라와 달리 bfs 가 아닌 이중 for 문을 사용


def bellmanFord(s):
    dist[s] = 0
    for i in range(N):
        for j in range(M):
            cur = graph[j][0]
            next = graph[j][1]
            weight = graph[j][2]
            if dist[cur] != INF and dist[next] > dist[cur] + weight:
                dist[next] = dist[cur] + weight
                if i == N - 1:
                    return True
    return False


cycle = bellmanFord(1)
if cycle:
    print(-1)
else:
    for k in range(2, N + 1):
        if dist[k] == INF:
            print(-1)
        else:
            print(dist[k])