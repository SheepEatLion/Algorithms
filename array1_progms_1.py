def solution(a, b):
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    m = 0
    for i in range(a):
        m += month[i]
    total_day = b + m
    d = total_day % 7
    return day[d-1]
'''
2016년 달력에서 a와 b에 각각 월 일이 주어지면 무슨 요일인지 출력하는 문제.
1월 1일은 금요일부터 시작했다.
1월 1일이 금요일 = 1월 8일도 금요일
2월 15일이 주어졌다고 치면 31일 + 15일 = 46일 
윤년이니까 2월이 29일까지 있음.
'''