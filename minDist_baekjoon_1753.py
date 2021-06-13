import sys
import heapq
import collections

v, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = collections.defaultdict(list)
INF = int(1e9)
distance = [INF] * (v+1)

for _ in range(E):
    u, k, w = map(int, sys.stdin.readline().split())
    graph[u].append((k, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cur_cost, cur_node = heapq.heappop(q)
        if distance[cur_node] < cur_cost:
            continue

        for node in graph[cur_node]:
            cost = cur_cost + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(start)
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])