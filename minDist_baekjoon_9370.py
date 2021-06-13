import sys
import heapq
import collections


def dijkstra(distance, start):
    q = []
    heapq.heappush(q, (0, start))
    dist = distance[:]
    dist[start] = 0
    while q:
        cur_cost, cur_node = heapq.heappop(q)

        for node in graph[cur_node]:
            cost = cur_cost + node[1]
            if cost < dist[node[0]]:
                dist[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    return dist


tc = int(sys.stdin.readline())
for _ in range(tc):
    N, M, T = map(int, sys.stdin.readline().split())  # 노드, 간선, 목적지후보 개수
    S, G, H = map(int, sys.stdin.readline().split())  # 출발점, 반드시 지나친 노드
    # 그래프 생성
    graph = collections.defaultdict(list)
    INF = int(1e9)
    distance = [INF] * (N + 1)
    candidate_endpoint = []
    endpoint = []
    for _ in range(M):
        U, V, W = map(int, sys.stdin.readline().split())  # U에서 V까지 W비용
        graph[U].append((V, W))
        graph[V].append((U, W))
    for _ in range(T):
        candidate_endpoint.append(int(sys.stdin.readline()))  # 목적지 후보 노드
    # 각각의 출발점에서 최단거리를 구한다.
    d1 = dijkstra(distance, S)
    d2 = dijkstra(distance, G)
    d3 = dijkstra(distance, H)
    # 출력
    for c in candidate_endpoint:
        path = min((d1[G] + d2[H] + d3[c]), (d1[H] + d3[G] + d2[c]))
        if path == d1[c]:
            endpoint.append(c)
    print(*sorted(endpoint))
'''
이 문제는 골드2 단계로 1504번 문제보다 난이도가 높지만 핵심로직은 같다.
정해진 간선(2개의 노드)를 반드시 통과하게끔 최단경로를 설정하는 것이 같고
다른 점은 그렇게 구한 최단경로가 일반적인 다익스트라에서의 최단경로와 같은지 확인해서
같다면 출력해주고 같지 않다면 버린다.
출력할 때는 오름차순 정렬하여 언패킹 해준다.
'''