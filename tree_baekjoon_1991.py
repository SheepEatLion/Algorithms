import sys
import collections

#  전위: 루트 / 왼쪽자식 / 오른쪽자식
def pre(node):
    queue.append(node)
    visited.append(node)
    while queue:
        now = queue.popleft()
        for i in tree.get(now):
            if i not in visited:
                pre(i)
#  중위: 왼쪽자식 / 루트 / 오른쪽자식
def mid(node):
    queue.append(node)
    while queue:
        root = queue.popleft()
        if tree.get(root):
            for i, v in enumerate(tree.get(root)):
                #  왼쪽 자식이 있고 갈 수 있다면
                if i == 0 and v not in visited and v != '.':
                    mid(v)
                #  왼쪽 자식이 없고 루트가 미방문 상태라면
                elif i == 0 and v == '.' and root not in visited:
                    visited.append(root)

                #  루트를 넣어준 상태에서 오른쪽 자식이 있다면
                elif i == 1 and root in visited and v != '.':
                    mid(v)
                elif i == 1 and root not in visited:
                    visited.append(root)
                    if v != '.':
                        mid(v)
#  후위: 왼쪽자식 / 오른쪽 자식 / 루트
def last(node):
    queue.append(node)
    while queue:
        root = queue.popleft()
        if tree.get(root):
            for i, v in enumerate(tree.get(root)):
                if i == 0 and v != '.' and v not in visited:
                    last(v)
                elif i == 1 and v != '.' and v not in visited:
                    last(v)
            visited.append(root)



n = int(sys.stdin.readline())
tree = dict()
queue = collections.deque()
visited = collections.deque()
visited.append('.')
for _ in range(n):
    a, b, c = sys.stdin.readline().split()
    tree[a] = [b, c]

pre('A')
visited.popleft()
print(''.join(visited))
queue.clear()
visited.clear()
mid('A')
print(''.join(visited))
queue.clear()
visited.clear()
last('A')
print(''.join(visited))