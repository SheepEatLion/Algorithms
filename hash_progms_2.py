def solution(record):
    answer = []
    id_hash = {}
    for i in range(len(record)):
        state = record[i].split(' ')
        if state[0] == 'Enter':
            id_hash[state[1]] = state[2]  # 유저 아이디 등록 (아이디 : 닉네임)
            answer.append("{}님이 들어왔습니다.".format(state[1]))  # 아이디로 저장
        elif state[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(state[1]))
        elif state[0] == 'Change':
            id_hash[state[1]] = state[2]
    #  여기서 answer 에 들어간 유저 아이디들을 가장 최신의 닉네임으로 전부 변경
    for j in range(len(answer)):
        front, back = answer[j].split('님')
        answer[j] = answer[j].replace(front, id_hash.get(front))
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

'''
[오픈채팅방] -  2019 카카오 블라인드 리크루잇 문제
닉네임의 변경이 빈번하게 일어나고, 실제 아이디값과 닉네임이 매칭되어 있는 구조이기 때문에
해쉬 자료구조를 사용해서 아이디와 닉네임을 매칭시켜두고 모든 입력을 아이디 기준으로 받은 뒤에
마지막에 각 아이디의 가장 최신 닉네임으로 전부 변경해주면 1번의 변경으로 해결가능.
'''