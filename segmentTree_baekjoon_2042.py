import sys

def init(start, end, node):
    if start == end:  #  현재 노드가 리프노드 라는 뜻이다.
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        init(start, mid, node*2)
        init(mid+1, end, node*2+1)
        tree[node] = tree[2*node] + tree[2*node+1]
'''
node 가 담당하는 구간을 start, end 라고 하고 합을 해야하는 구간이 left, right 
4가지 경우의 수가 있다.
1. left right 와 start end 가 겹치지 않는 경우
2. left right 가 start end 를 완전히 포함하는 경우
3. start end 가 left right 를 완전히 포함하는 경우
4. left right 와 start end 가 겹쳐 있는 경우
'''
def sum_tree(start, end, node, left, right):
    #  1번
    if left>end or right<start:
        return -1
    #  2번
    if left <= start and end <= right:
        return tree[node]
    #  3번, 4번
    mid = (start + end) // 2
    m1 = sum_tree(start, mid, 2*node, left, right)
    m2 = sum_tree(mid+1, end, 2*node+1, left, right)
    if m1 == -1: return m2
    if m2 == -1: return m1
    return m1 + m2

def update(start, end, node, index, val):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = val
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, val)
    update(mid+1, end, node * 2 + 1, index, val)
    tree[node] = tree[2*node] + tree[2*node+1]

n, m, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
log = 0
while 1 << log < n:
    log += 1
tree = [0] * (2 ** (log + 1))
init(0, n-1, 1)
for i in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(0, n-1, 1, b-1, c)
    else:
        print(sum_tree(0, n-1, 1, b-1, c-1))