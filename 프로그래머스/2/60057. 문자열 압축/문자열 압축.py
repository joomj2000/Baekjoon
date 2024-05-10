def solution(s):
    answer = 0
    #stack=[s[0]]
    cnt=1
    result=[0]*(len(s)+1)
    
    for i in range(1,len(s)+1):
        str_result=''
        #for j in range(1,len(s)):
        stack=[s[0:i]]
        j=i
        while(j<len(s)+i):
            x1=stack.pop()
            #print(i,j,x1,s[j:j+i])
            if x1==s[j:j+i]:
                stack.append(x1)
                cnt+=1
            else:
                if cnt>1:
                    str_result+=str(cnt)+x1
                else:
                    str_result+=x1
                stack=[s[j:j+i]]
                cnt=1
            j+=i
        
        result[i]=len(str_result)
            
    answer=min(result[1:])
        
        
        
    
    return answer