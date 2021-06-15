import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)  # 간선이 여러개일 수 있음.

for inter in range(n):
    for start in range(n):
        for end in range(n):
            graph[start][end] = min(graph[start][end], graph[start][inter] + graph[inter][end])

for j in range(n):
    for k in range(n):
        if graph[j][k] == INF:
            print(0, end=' ')
        else:
            print(graph[j][k], end=' ')
    print()
'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''