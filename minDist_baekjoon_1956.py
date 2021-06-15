import sys
INF = int(1e9)
V, E = map(int, sys.stdin.readline().split())
graph = [[INF] * V for _ in range(V)]
for i in range(V):
    graph[i][i] = 0
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = INF
for i in range(V):
    for j in range(i+1, V):
        if graph[i][j] != INF and graph[j][i] != INF:
            answer = min(answer, graph[i][j] + graph[j][i])
if answer == INF:
    print(-1)
else:
    print(answer)
'''
플로이드 워셜로 풀 수 있는 문제.
사이클을 찾으려면 시작점 a에서 도착점 b로 테이블을 인덱싱하고 INF 상태가 아니라면 다시 자신에게 돌아올 수 있는 상태이므로 
사이클이 존재한다는 뜻
'''