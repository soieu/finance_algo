#날짜 입력 시 > 요일 출력해주는 함수

import datetime as dt
def solution(a, b):
    data = dt.datetime(2016,a,b)
    week = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'} #함수값-요일출력값 딕셔너리 생성
    return week[data.weekday()]

#함수 weekday : 해당 날짜에 대한 요일값 출력(0월요일 ~ 6일요일)