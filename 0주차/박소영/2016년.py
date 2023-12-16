def solution(a, b):
    answer = ''
    weekday = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    month_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    past_days = 0
    
    # a월까지의 일수를 더해서 a월 1일까지 지난 날들을 구한다
    for days in range(a-1):
        past_days += month_days[days];
        
    
    
    # 1월 1일에서 a월 b일까지의 지난날들을 구한다.
    past_days += b-1
    print(past_days)
    
    # 요일 구하기
    answer = weekday[(past_days+5) % 7]
    
    return answer
