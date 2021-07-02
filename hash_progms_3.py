import collections
def solution(genres, plays):
    answer = []
    cache = collections.defaultdict(list)  # 장르 : [고유번호, 재생횟수]
    genre_order = collections.defaultdict(int)  # 장르 : 전체재생횟수
    order = collections.defaultdict()  # 전체재생횟수 : 장르
    #  첫번째 딕셔너리와 두번째 딕셔너리 생성
    for i in range(len(genres)):
        cache[genres[i]].append([i, plays[i]])
        genre_order[genres[i]] += plays[i]
    #  두번째 딕셔너리를 기반으로 세번째 딕셔너리 생성 -> key 와 value 를 뒤바꾼 구조임.
    for k in genre_order:
        order[genre_order[k]] = k
    key_list = sorted(order)  # Key 가 int 가 됐으므로 key 기반 정렬이 가능해짐.
    #  첫번째 딕셔너리안에 value 에서 재생횟수를 기반으로 정렬, 같다면 고유번호 기반 정렬
    for g in cache:
        cache[g].sort(key=lambda x: (x[1]), reverse=True)
    #  정렬된 장르 순서를 담고 있는 key_list 에서 하나씩 장르를 꺼내서 order 에 키값으로 주어, 고유번호 부분을 꺼내서 answer 에 추가. (이미 재생횟수 기반으로 정렬한 거라서 바로 꺼낼 수 있음)
    while key_list:
        od = order[key_list.pop()]
        if len(cache[od]) == 1:
            answer.append(cache[od][0][0])
        else:
            answer.append(cache[od][0][0])
            answer.append(cache[od][1][0])
    return answer


print(solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

'''
[베스트 앨범] hash
문제설명:
    노래는 인덱스(고유번호)로 구분
    각 노래들의 재생 횟수를 더해서 가장 횟수가 높은 장르의 곡들을 먼저 수록
    해당 장르 내에서는 재생 횟수가 높은 노래를 먼저 수록
    한 장르에서 최대 2곡까지 수록할 수 있고 1곡밖에 없다면 1곡만 수록
    만약 재생횟수가 같은 노래가 있다면 고유번호가 낮은 것을 우선 수록
풀이과정:
    해쉬를 어디에 적용해야 할지 고민을 많이 한 문제
    결국 고유번호 배열, 장르 배열, 재생횟수 배열 이렇게 3가지 배열이 있는 것이고
    해쉬도 3개가 만들어져야함.
    그리고 최고 많이 재생된 장르, 최고 많이 재생된 노래 들이라서 정렬을 선택했는데
    노래의 재생횟수는 중첩이 가능해서 같은 경우 고유번호가 낮아야한다.
    이를 위해 고유번호와 재생횟수를 함께 배열화 해서 하나의 딕셔너리에 장르별로(키) 묶어두고
    람다로 정렬 진행, 다만 리벌스로 정렬해야 같은 경우 고유번호가 낮은게 앞으로 감.
    또, 최대 많이 재생된 장르도 해쉬로 만들어두면 쉽게 될 것 같지만
    해쉬 구조 자체를 정렬해야해서 힘듬.
    그래서 해쉬가 만들어진 후에는 역으로 int: string 형태로 또 하나의 해쉬를 만들어서 해결했음.
'''