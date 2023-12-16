from datetime import datetime
def solution(a, b):
    
    # 방법 1. 라이브러리 import 
    week_nm = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    dt = datetime(2016, a, b).weekday()
    return (week_nm[dt])
    
#     # 방법 2. 일수 합
#     week_nm = ['FRI','SAT','SUN','MON','TUE','WED','THU']
#     days_cnt = [31,29,31,30,31,30,31,31,30,31,30,31]
    
#     # 전 달 일수 합
#     sum1 = (sum(days_cnt[:a-1]) + b) % 7
#     return (week_nm[sum1-1])