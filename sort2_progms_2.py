import bisect
def solution(citations):
    citations.sort()
    #  [0, 1, 3, 5, 6]
    for h in range(citations[-1], -1, -1): # 6, 5, 4, 3, 2, 1, 0
        #  h보다 큰 수가 h개 이상 있는지 확인
        if h in citations:
            if len(citations[bisect.bisect_left(citations, h):]) >= h:
                return h
        else:
            if len(citations[bisect.bisect_right(citations, h):]) >= h:
                return h
'''
[H-Index] 정렬 문제
논문 n 편 중에서, h번 이상 인용된 논문이 h편 이상이라면 그 h의 최대값을 리턴하는 문제.
즉, h보다 큰 수가 h개 이상 있는 지 확인해야한다.
미리 정렬을 해두면 더 빠르게 탐색할 수 있다.
그리고 직관적으로 낮은 숫자일 확률이 적기 때문에 역순으로 for 탐색을 시작한다.
bisect 라이브러리를 사용했는데, 꼭 안해도 괜찮다.
그냥 for 문에다가 cnt 변수로 하나씩 체크해줘도 된다.
'''