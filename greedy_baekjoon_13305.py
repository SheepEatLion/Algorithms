import sys
int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
gas = list(map(int, sys.stdin.readline().split()))[:-1]
#  첫 도시에서 반드시 주유해야함.
g = gas[0]
answer = g * dist[0]
#  다음 도시부터 기름 값 비교하며 교체할지 말지 정하고 거리*기름값 더해주기.
for i in range(1, len(gas)):
    if g > gas[i]:
        g = gas[i]
    answer += g * dist[i]
print(answer)


'''
처음 생각했던 코드는 시간초과였다.
떠올린 아이디어는 다음과 같았다.

가장 저렴한 기름 값의 주유소를 만난다면, 거기서 남은 거리만큼을 다 채우고 출발하면 되지않을까?
그래서 마지막 도시에서는 주유를 하지 않으므로 슬라이싱해서 입력값들을 다 받은 뒤에
min() 메서드를 활용해서 최저값을 구하고 index() 메서드를 통해 몇번째 도시인지 알아낸다.
그 도시부터 이후는 그 값으로만 갈 것이므로 이후 거리들을 다 더한 뒤에 기름 값을 곱해준다.
그 다음, gas와 dist리스트를 index 위치를 기준으로 짜른 다음에 위에 과정을 반복한다.

import sys
int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
gas = list(map(int, sys.stdin.readline().split()))[:-1]

while True:
    try:
        min_price = min(gas)
        min_station = gas.index(min_price)
        answer += sum(dist[min_station:]) * min_price
        gas = gas[:min_station]
        dist = dist[:min_station]
        print(min_station)
    except:
        break
print(answer)

나와 비슷한 코드로 시간초과가 난 사람이 있어서 확인해보니
이렇게 코딩할 경우 O(n제곱)이 최악의 경우에 나온다고 한다.
예를 들어 도시가 10만개가 있는데 기름 값이 왼쪽부터 오름차순으로 내려간다면
한개씩 자르고 한개씩 더하고 곱하기 때문에 n제곱이 되는 게 맞았다.
sum 메서드가 느리기 때문.

'''
'''
그래서 두번째로 생각한 정답코드는 가장 위의 코드이다.
메서드를 가능한 쓰지 않으려고 했고, 첫 도시에서는 반드시 주유를 해야하니까
일단 초기값을 첫 도시를 기준으로 넣어준 다음에
차라리 for문을 gas 값을 기준으로 한번 쭉 돌리면서 더 저렴한 가격이 나오면 가격을 교체하고
그게 아니면 이전 가격을 유지하면서 계속 도로길이 만큼 곱해준 뒤 더해주면
한번에 O(n)으로 해결된다.
사실 이렇게 하면 언제나 O(n)이기 때문에 안정적이긴 하나 더 빠르긴 어렵다.
이 전에 내가 사용한 코드는 상수시간만에 끝낼 수도 있기 때문에 장단점이 있다고 보지만
정해진 효율성이 있는 코딩테스트에서는 확실히 안정성 있는 코드가 더 좋은 것 같다.
'''

'''
그리디는 매 선택의 순간마다 언제나 이기적인 선택을 하는 것이 최선의 결과가 된다는 가정하에 
만들어진 이론이다. 
그래서 어떤 문제가 주어졌을 때, 선택의 순간에서 옵션들이 몇가지인지 총 옵션의 개수를 파악하고
그 옵션들 중에서 현재 가장 좋은 옵션을 선택해도 그 다음 할 선택에서 영향을 안 끼치는지
확인해야한다.
대표적인 문제로는 거스름돈 문제가 있는데, 워낙 쉬운 개념인지라 풀긴 했지만 깃에 올리진 않는다.
다만 당연히 그리디도 어려운 문제가 존재함으로, 어려운 문제를 풀게되면 다시한번 그리디를 올리도록 하겠다!
'''