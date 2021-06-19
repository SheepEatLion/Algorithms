
def solution(S):
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    sep_S = S.split('\n')
    result, result2 = [], []
    year, month, day = [], [], []
    for v in sep_S:
        temp = v.split(' ')
        for i in range(len(temp)):
            if temp[i] != '':
                result.append(temp[i])
    for j in range(0, len(result), 7):
        if result[j] == 'admin':
            if 'x' in result[j+1]:
                if int(result[j+5]) < 14 * pow(2, 20):
                    day.append(result[j+2])
                    month.append(result[j+3])
                    year.append(result[j+4])

    if not day:
        return 'NO FILES'
    min_index = 0
    for k in range(1, len(year)):
        if year[k] < year[min_index]:
            min_index = k
            continue
        if year[k] == year[min_index]:
            if months[month[k]] < months[month[min_index]]:
                min_index = k
            elif months[month[k]] > months[month[min_index]]:
                continue
            else:
                if int(day[k]) < int(day[min_index]):
                    min_index = k
                elif int(day[k]) > int(day[min_index]):
                    continue
    return day[min_index] + ' ' + month[min_index] + ' ' + year[min_index]

print(solution('admin  -wx 29 Sep 1983        833 source.h\nadmin  r-x 23 Jun 2003     854016 blockbuster.mpeg\nadmin  --x 02 Jul 1997        821 delete-this.py\nadmin  -w- 15 Feb 1971      23552 library.dll\nadmin  --x 15 May 1979  645922816 logs.zip\njane   --x 04 Dec 2010      93184 old-photos.rar\njane   -w- 08 Feb 1982  681574400 important.java\nadmin  rwx 26 Dec 1952   14680064 to-do-list.txt'))
# admin 찾고 --x 찾아야함.



'''
def solution(U, L, C):
    N = len(C)
    first, second = [], []
    for i in range(N):
        if C[i] == 0:
            first.append('0')
            second.append('0')
        elif C[i] == 2:
            first.append('1')
            second.append('1')
            U -= 1
            L -= 1
        elif C[i] == 1:
            if U > L:
                first.append('1')
                second.append('0')
                U -= 1
            else:
                first.append('0')
                second.append('1')
                L -= 1
    if U != 0 or L != 0:
        answer = 'IMPOSSIBLE'
    else:
        answer = ''.join(first) + ',' + ''.join(second)
    return answer

print(solution(2, 3, [0, 0, 1, 1, 2]))
'''

'''
def solution(S, C):
    seq_S = S.split(', ')
    answer = ''
    for i in range(len(seq_S)):
        answer += seq_S[i] + ' <'
        temp = seq_S[i].split(' ')
        tmp = ''
        result = ''
        for j in range(len(temp)):
            if temp[j] != temp[-1]:
                a = temp[j][0].lower()
                answer += a
                result += a
            else:
                find_hp = temp[-1].count('-')
                for k in range(8 - len(tmp) + find_hp):
                    if k >= len(temp[-1]):
                        break
                    if temp[-1][k] != '-':
                        tmp += temp[-1][k].lower()
                        result += temp[-1][k].lower()
                    else:
                        continue
        if result in answer:
            tmp += str(answer.count(result) + 1)
        if i == len(seq_S) - 1:
            tmp += '@' + C + '.com>'
        else:
            tmp += '@' + C + '.com>, '
        answer += tmp
    return answer


print(solution('John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker', 'Example'))

신입사원들 이름 받아서 규칙에 맞게 회사 메일 생성해주기.
First, Middle(if), Last 로 구성. 이니셜로 되어있고 최대 8글자에서 짤림
'''