def is_ok(answer):
    for x,y,s in answer:
       # x,y,s=wall
        if s==0: #기둥
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif s == 1:  # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True
        #     if y!=0:
        #         if ([x,y+1,1] not in wall) and ([x,y,1] not in wall): # 보와 연결
        #             return True
        #         if  ([x-1,y+1,1] in wall) or ([x-1,y,1] in wall):
        #             return True
        #         if ([x,y-1,0] in wall): # 기둥위
        #             return True
        # else: #
        #     if ([x+1,y-1,0] in wall) or ([x,y-1,0] in wall): # 기둥과 연결
        #         return True
        #     if  ([x-1,y,1] in wall) and ([x+1,y,1] in wall):
        #         return True
        # return False

        
def solution(n, build_frame):
    answer = [[]]
    #matrix=[[0]*(n+1) for _ in range(n+1)]
    #print(matrix)
    #h=heapq()
    wall =[]
    
    
    for bf in build_frame:
        x=bf[0]
        y=bf[1]
                
        if bf[3]==1: # 설치 
            wall.append([x,y,bf[2]])
            if is_ok(wall) is False:
                wall.remove([x,y,bf[2]])
                    
                
            
        else: #제거 
            # 제거
            wall.remove([x,y,bf[2]])
            if is_ok(wall) is False:
                wall.append([x,y,bf[2]])
            
    
    wall.sort()
    print(wall)
            
            
            
        
        
    
    
    
    
    return wall