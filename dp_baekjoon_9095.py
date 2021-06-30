import sys
tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())
    memo = [0, 1, 2, 4]
    if n == 1 or n == 2 or n == 3:
        print(memo[n])
    else:
        for i in range(4, n+1):
            memo.append(memo[i-1] + memo[i-2] + memo[i-3])
        print(memo[-1])

'''
1 2 3 더하기 문제
어떤 수가 주어지면 1과 2와 3을 가지고 더해서 그 수를 만들 수 있는 방법이 몇가지 인지 찾아내면 된다.
기본적으로 1은 한가지, 2는 두가지, 3은 4가지를 가지고 있다.
이것들을 초기값으로 정해주고
각 입력숫자 별로 경우의 수가 몇가지 인지 나열해보면
1 : 1
2 : 2
3 : 4
4 : 7
이런식으로 나오고 실제 각각의 경우의 수가 어떤 식으로 구현되는지 (1+1+2 등)
확인해보면 4부터는 이전의 값들을 더한 값이 나오는 걸 확인할 수 있다.
따라서 점화식은 다음과 같이 나온다.
D(n) = D(n-1) + D(n-2) + D(n-3) //// n 이 4 이상일때
'''