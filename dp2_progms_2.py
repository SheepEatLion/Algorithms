def solution(board):
    answer = 0
    row, col = len(board), len(board[0])
    table = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]

    for i in range(row):
        for j in range(col):
            table[i+1][j+1] = board[i][j]

    for i in range(1, row+1):
        for j in range(1, col+1):
            if table[i][j] != 0:
                table[i][j] = min(table[i-1][j], table[i][j-1], table[i-1][j-1]) + 1
                if answer < table[i][j]:
                    answer = table[i][j]
    return answer * answer


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
'''
[가장 큰 정사각형 찾기] dp 문제
주어진 2차원 배열에서 가장 큰 정사각형을 찾아내는 문제다.
아이디어가 안떠올라서 블로그 참고했다.
(1,1) 지점을 기준으로 잡았다고 가정할때, 정사각형이 되려면 (0,0) (1,0) (0,1) 지점이 1 이어야한다.
따라서 dp 를 활용해 3곳을 비교하여 그 중의 최솟값 + 1 을 현재 지점에 더해주면 된다.
그리고 애초에 직사각형의 형태로 입력되는 경우 (4,1) 를 막기 위해 일종의 패딩을 입히듯 테이블을 만들어야한다.
--
처음엔 0과 1이 쓰여진 맵 형태만 보고 dfs 로 생각했는데,,
오히려 잘못된 방향으로 생각하고 나니 제대로 된 아이디어를 떠올리기가 어려워졌다.
'''