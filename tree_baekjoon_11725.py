import sys
import collections
#sys.setrecursionlimit(100001)


#  bfs로 동작하는 코드: 정확성은 맞지만 시간초과
def bfs_find_root():
    while queue:
        root = queue.popleft()
        for child in tree[root]:
            if not visited[child]:
                output[child] = root
                queue.append(child)
                visited[child] = True

'''
#  dfs로 동작하는 코드
def dfs_find_root(root):
    for child in tree[root]:
        if output[child] == 0:
            output[child] = root
            dfs_find_root(child)
'''
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
output = [0 for _ in range(n+1)]
visited = [False for i in range(n+1)]
queue = collections.deque()
queue.append(1)
output[1] = 1
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
bfs_find_root()
#dfs_find_root(1)
for i in range(2, n+1):
    print(output[i])

'''
        1
    4       6
  2   7   1x    3
4x    4x       x6   5

2번 노드부터 부모 노드 순서
4 6 1 3 1 4

import sys
sys.setrecursionlimit(100000) 
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
parents = [0 for _ in range(n+1)]
parents[1] =1

def dfs(curr, tree, parents):
    for node in tree[curr]:
        if parents[node] == 0:
            parents[node] = curr
            dfs(node, tree, parents)
dfs(1, tree, parents)
for i in range(2, n+1):
    print(parents[i])
'''