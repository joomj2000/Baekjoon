'''
1. queue를 이용해서 문자열 회전시키기
2. 문자열이 올바른지 확인하기 
2-1 . stack이용?

'''
from collections import deque

def solution(s):
    answer = 0
    queue=deque(s)

    for i in range(len(s)):
        # 1. 문자열 회전 
        v=queue.popleft()
        queue.append(v)
        check=deque()
        check=queue.copy()

        # 2. 문자열이 맞는지 확인 

        stack=[]
        
        while(check):
            c=check.popleft()
            #print(c)
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
                
            else:
                if c==')' and len(stack)!=0 and stack[-1]=='(':
                        stack.pop()
                elif c==']' and len(stack)!=0 and stack[-1]=='[':
                        stack.pop()
                elif c=='}' and len(stack)!=0 and stack[-1]=='{':
                        stack.pop()
                else:
                    stack=['1']
                    break
                
        if len(stack)==0 and len(check)==0:
            answer+=1
            
        
    
    
    
    
    return answer