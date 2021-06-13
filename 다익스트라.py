import heapq
import sys
inp = sys.stdin.readline()
INF = int(1e9)

# 노드의 개수와 엣지의 개수를 입력받는다.
n, e = map(int, inp.split())
# 출발점을 정해준다.
start = int(inp)
# 그래프를 만든다.
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 간선 정보를 입력받는다.
for _ in range(e):
    a, b, c = map(int, inp.split()) # a 노드에서 b 노드로 가는 비용 c
    graph[a].append((b, c))

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 실행
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("무한대, 연결되어 있지 않음.")
    else:
        print(distance[i])