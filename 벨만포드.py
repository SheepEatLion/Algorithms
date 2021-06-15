import sys
input = sys.stdin.readline
INF = int(1e9)

def bellmanFord(start):
    dist[start] = 0  # 시작점 0으로 초기화

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]  # 입력시 a에서 b 까지의 가중치 c로 입력받았었음.
            next_node = edges[j][1]
            cost = edges[j][2]
            #  현재 위치가 무한대가 아니고 다음 위치 경로값이 현재 위치 + 가중치보다 크다면
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n-1:  # 사이클 체크
                    return True
    return False

#  변수 정의 및 초기화
n, m = map(int, input().split())  # n은 노드의 개수이고, m은 간선의 개수
edges = []  # 간선 정보를 담을 리스트
dist = [INF] * (n+1)  # 노드의 개수만큼 거리 리스트를 생성하는 동시에 무한대로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

#  알고리즘 수행
cycle = bellmanFord(1)  # 1번 노드를 시작노드로 한다.
if cycle:  # 사이클이 있으면 -1를 출력하고 종료
    print('-1')
else:  # 사이클이 없으면 경로 값들을 출력한다.
    for i in range(2, n+1):
        if dist[i] == INF:  # 만약 연결안된 노드가 있다면 -1로 출력
            print('-1')
        else:  # 이외에는 문제없이 그대로 출력
            print(dist[i])

