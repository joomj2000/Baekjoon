from collections import deque

def solution(cards):
    answer = 0
    cards=[0]+cards
    result=[]
    queue=deque()

    visited=set()

    def BFS(i):
        cnt=1
        queue.append(i)
        while queue:
            now=queue.popleft()
            visited.add(now)
            next=cards[now]
            if next not in visited:
                cnt+=1
                queue.append(next)
        return cnt



    for i in range(1,len(cards)):
        if i not in visited:
            result.append(BFS(i))
            
    result.sort()
            
        
        
    
    
    
    if len(result)==1:
        return 0
    

    return result[-1]*result[-2]