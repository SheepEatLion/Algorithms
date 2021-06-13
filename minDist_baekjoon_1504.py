import sys
import heapq
import collections

V, E = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(list)
INF = int(1e9)
distance = [INF] * (V + 1)

for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

# 반드시 거쳐가야하는 노드
must_v1, must_v2 = map(int, sys.stdin.readline().split())


def dijkstra(distance, start):
    q = []
    heapq.heappush(q, (0, start))
    d = distance[:]
    d[start] = 0
    while q:
        cur_cost, cur_node = heapq.heappop(q)
        if d[cur_node] < cur_cost:
            continue

        for node in graph[cur_node]:
            cost = cur_cost + node[1]
            if cost < d[node[0]]:
                d[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    return d


d1 = dijkstra(distance, 1)
d2 = dijkstra(distance, must_v1)
d3 = dijkstra(distance, must_v2)

answer = min((d1[must_v1] + d2[must_v2] + d3[V]), (d1[must_v2] + d3[must_v1] + d2[V]))
if answer >= INF:
    print(-1)
else:
    print(answer)
'''
일반적인 다익스트라처럼 보이지만, 반드시 지정한 두 노드를 밟고 가야한다.
예제는 4개의 노드에 6개의 간선으로 주어졌는데, 이를 가지고 그림을 그려보면 쉽게 파악할 수 있는 게 있다.
1번 노드가 출발점이고 4번 노드가 도착점인데 2번과 3번 노드를 반드시 거쳐가야 한다.
그럼 다음과 같은 2개의 경우의 수가 나온다.
1 -> 2 -> 3 -> 4
1 -> 3 -> 2 -> 4
다익스트라는 한 노드에서 다른 모든 노드의 최단 거리를 구해준다.
이러한 특성을 기억하고 있다면 어렵지 않게 아이디어를 떠올릴 수 있다.
1을 출발점으로 하는 다익스트라
2를 출발점으로 하는 다익스트라
3을 출발점으로 하는 다익스트라
이렇게 3개의 경우를 구해주면 각 지점에서 다른 모든 지점으로 최단거리가 나오기 때문에
다 구해준 뒤에 min 메서드를 통해 이전의 2가지 경우의 수 중에서 어떤게 더 짧은 지 비교하면 된다.
참고로 연결되어 있지 않다면 INF 값 이상이 나오는데 그럴 경우 문제에서는 -1을 출력하라고 되어있다.
'''