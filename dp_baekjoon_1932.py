import sys
size_of_triangle = int(sys.stdin.readline())
triangle = []
sum_cache = [[0]*i for i in range(1, size_of_triangle+1)]

#  삼각형 입력 받기
for i in range(size_of_triangle):
    triangle.append(list(map(int, sys.stdin.readline().split())))

#  sum_cache(dp)의 초기값 설정
sum_cache[0][0] = triangle[0][0]  # 7
sum_cache[1][0] = triangle[1][0] + sum_cache[0][0]  # 10
sum_cache[1][1] = triangle[1][1] + sum_cache[0][0]  # 15

#  합산을 메모하는데, 이전 레벨의 좌우 중에서 더 큰값을 골라서 합산
for level in range(2, size_of_triangle):
    for i in range(len(triangle[level])):
        if i == 0:
            sum_cache[level][i] = sum_cache[level - 1][i] + triangle[level][i]
        elif i == len(triangle[level])-1:
            sum_cache[level][i] = sum_cache[level - 1][i-1] + triangle[level][i]
        else:
            sum_cache[level][i] = triangle[level][i] + max(sum_cache[level - 1][i-1], sum_cache[level - 1][i])
        #print('log:', sum_cache)
print(max(sum_cache[size_of_triangle-1]))
'''
겉보기엔 백트래킹 문제처럼 보이지만 DP문제다.
각 층을 나타내는 변수 level 이 있고 그 층의 좌표를 나타내는 i 가 있다고 하자.
먼저 반복구조를 살펴보면 이런 코드가 나온다.
triangle[level - 1][i] + max(triangle[level][i], triangle[level][i+1]
이전 층의 i번째 값을 가지고 현재 층의 i번째와 i+1번째(좌우) 중에서 더 큰값을 고르면 된다.
이전 층까지의 값은 계속해서 합산 되어야 함으로 dp에 메모하고 있어야한다.
dp[level][i] = dp[level - 1][i] + max(triangle[level][i], triangle[level][i+1]
가독성을 위해 dp를 쓰긴 하지만 리스트명을 dp말고 sum_cache라고 하겠다.
대략 이런식으로 동작할 거 같은데, 러프하게 나타낸 거라서 코딩을 하면서 구체적인 수정을 하면된다.
그림을 그려보면 더 쉽게 이해할 수 있는데 여기에 최대한 짧고 비슷하게 나타내면 다음과 같다.
     7                          7
    3 8                    10       15
   8 1 0    -->        18    (11,16)     15
  2 7 4 4            20  (25,23)   (20,19)  19
'''