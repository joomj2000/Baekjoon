def solution(n, times):
    answer = 0
    max_time=max(times)*n
    
    start=1
    end=max_time
    while(start<=end): #이진 탐색
        mid=(start+end)//2
        result=0
        
        for i in times:
            result+=mid//i
        print(result)
            
        if result>=n:
            end = mid - 1
        else :
            start = mid + 1
    
    print(start)
    
    
    
    return start