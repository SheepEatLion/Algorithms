import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
inorder = [0] + list(map(int, sys.stdin.readline().split()))
postorder = [0] + list(map(int, sys.stdin.readline().split()))
pos = [0] * (n+1)
#  inorder 를 기준으로 pos 배열 생성 / pos 배열은 다른 배열의 값을 인덱스로 가짐.
for i in range(1, n+1):
    pos[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return
    root = postorder[postEnd]
    print(root, end=' ')
    root_inorder = pos[root]
    left = root_inorder - inStart
    preorder(inStart, root_inorder-1, postStart, postStart+left-1)
    preorder(root_inorder+1, inEnd, postStart+left, postEnd-1)

preorder(1, n, 1, n)
'''
인오더 ( 왼 루트 오 )
포스트오더 ( 왼 오 루트 )
를 입력 받아서 프리오더 ( 루트 왼 오) 를 출력해야한다.
트리를 구할 땐, 전순위 중순위 or 중순위 후순위가 있으면 구할 수 있음.
이 문제는 후자의 경우에 해당한다.
포스트오더의 끝점을 인덱싱하면 그게 곧 루트가 되는데
이때 인덱싱한 결과가 루트의 인덱스가 아니라 루트 값 이라서
인오더에서 이 값으로 인덱싱해서 루트의 위치(인덱스)를 알아내야 하기때문에
pos 배열을 만들어야 하는 것이고,
그렇게 되면 계속해서 포스트오더의 인덱싱 범위를 움직여가면서
루트(부모)가 어떤 것(값)인지 찾아낼 수 있고 이렇게 찾아낸 값을 포스 배열에 넣어서
인오더에서의 루트(부모)의 위치를 알아낼 수 있다.
알아낸 뒤에는 루트를 기준으로 좌 우를 나누면 서브트리를 얻을 수 있고
얻은 서브트리에서 위 과정을 반복하면 된다.
즉, 재귀형태이자 분할정복의 형태라고 할 수 있다.
'''