import sys
import collections

def dijkstra(s):
    q = collections.deque()
    q.append((0, s, 0))
    distance[s][0] = 0
    while q:
        time, cur_node, money = q.popleft()
        if distance[cur_node][money] < time:
            continue
        for node in graph[cur_node]:
            time_cost, money_cost = time + node[2], money + node[1]
            if money_cost > M:
                continue
            if time_cost < distance[node[0]][money_cost]:
                distance[node[0]][money_cost] = time_cost
                q.append((time_cost, node[0], money_cost))


tc = int(sys.stdin.readline())
for _ in range(tc):
    N, M, K = map(int, sys.stdin.readline().split())  # 공항의 수, 총 지원비용, 티켓정보의 수
    INF = int(1e9)
    graph = collections.defaultdict(list)
    distance = [[INF] * (M+1) for _ in range(N+1)]

    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())  # 출발, 도착, 비용, 소요시간
        graph[u].append((v, c, d))

    dijkstra(1)

    answer = min(distance[N])
    if answer != INF:
        print(answer)
    else:
        print('Poor KCM')

'''
M원 이하로 돈을 사용하면서 소요시간 d가 가장 짧은 경로를 찾는 문제
1
3 100 3
1 2 1 1
2 3 1 1
1 3 3 30
'''