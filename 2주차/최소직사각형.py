def solution(sizes):
    
    x_box, y_box = 0,0
    for i in sizes:
        x, y = i[0], i[1]
            
        if x <= y:
            x_ = y
            y_ = x

        else:
            x_ = x
            y_ = y
            
        # x_box에 max 값 update
        x_box = max(x_box, x_)
        y_box = max(y_box, y_)
        
    return x_box * y_box
        
