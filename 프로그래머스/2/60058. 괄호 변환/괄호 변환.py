'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 

2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 

3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
  
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
  '''
def solution(p):

    answer = ''
    
    def result(T):
        #if T=="":
            #return T

        u=''
        v=''
        for i in range(len(T)):
            if u.count('(')!=0 and u.count('(')==u.count(')'):
                v=T[i:len(T)]
                break
            else:
                u+=T[i]
        print('u,v=',u,v)
        #u가 올바른 문자열인지 확인
        stack=[]
        is_u=True
        for j in u:
            if j=='(':
                stack.append(j)
            else:
                if len(stack)==0:
                    is_u=False
                    break
                stack.pop()
        if len(stack)!=0:
            is_u=False
            
        #v가 올바른 문자열인지 확인
        stack=[]
        is_v=True
        for j in v:
            if j=='(':
                stack.append(j)
            else:
                if len(stack)==0:
                    is_v=False
                    break
                stack.pop()
        if len(stack)!=0:
            is_v=False
            
        # u가 올바른 문자열 이라면
        if is_u==True:
            print('u가 올바른 문자열',u,v)
            if is_v==False:
                return u+result(v)
            else:
                return u+v
        else: #u가 올바른 문자열이 아니라면
            temp=''
            temp+='('
            if is_v==False:
                #print('is_v',v)
                temp+=result(v)
            else:
                temp+=v
            #temp+=result(v) if is_v==False else u+v
            temp+=')'
            print('앞뒤 제거전',u)
            u=u[1:len(u)-1] #앞뒤 제거
            print('앞뒤 제거후',u)
            for k in u:
                if k==')':
                    temp+='('
                else:
                    temp+=')'
            print('temp',temp)
            return temp
        
        
                    
    
        
        # if u==올바른 문자열:
        #     return u
        # else:
            
#         else:
#             temp=''
#             temp+='('
#             temp+=result(v)
#             temp+=')'
#             u=u[2:len(u)-1] #앞뒤 제거
#             u=[::-1] #방향 전환
#             temp+=u
            
        
        # v가 올바른 문자열인지 확인 ->
    answer=result(p)
    
    
    
    return answer