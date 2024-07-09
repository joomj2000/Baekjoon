'''
100이하니까 시간초과 안나지 않을까? -> 모든 경우의 수 확인 

+>->*
+>*>-
->*>+
->+>*
*>+>-
*>->+

숫자 연산자 분리?
for문 돌면서 해당 연산자 계산 -> 이때 숫자가 담긴 리스트 업데이트 


'''
import re
from itertools import permutations
def solution(expression):
    # seq=['+-*','+*-',
    #      '-*+','-+*',
    #     '*+-','*-+']
    seq=[]
    set_seq=set()
    
    
    # 수식 확인 
    for i in expression:
        if i =='+':
            seq.append('+')
            set_seq.add('+')
        elif i =='*':
            seq.append('*')
            set_seq.add('*')
        elif i =='-':
            seq.append('-')
            set_seq.add('-')
        # if '-' in expression:
        #     seq.append('-')
        # if '+' in expression:
        #     seq.append('+')
        # if '*' in expression:
        #     seq.append('*')
        
   # print(seq)
    # # 숫자만 추출 
    result = re.split(r'[-+*]', expression)
    
    # 가능한 연산 조합 
    permutations_list= list(permutations(set_seq,len(set_seq)))
    
    
    #print(expression)
    print('seq',seq)
    print('check',permutations_list)
    answer=0
    
    for per in permutations_list: #가능한 조합리스트
        temp_num=result[:]
        temp_op=seq[:]
        for p in per:
            s=0
            #for s in range(len(seq)):
            while(temp_op):
                if s>=len(temp_op):
                    break
    
               # for s in range(len(seq)):
                if temp_op[s]==p:
                    if p=='-':
                        temp_num[s]=int(temp_num[s])-int(temp_num[s+1])
                        temp_num.pop(s+1)
                        temp_op.pop(s)
                        s=0
                        #temp_num.append(result[s] -result[s+1])     
                    elif p=='+':
                        temp_num[s]=int(temp_num[s])+int(temp_num[s+1])
                        temp_num.pop(s+1)
                        temp_op.pop(s)
                        s=0
                        #temp_num.append(result[s]+result[s+1]) 
                    elif p=='*':
                        temp_num[s]=int(temp_num[s])*int(temp_num[s+1])
                        temp_num.pop(s+1)
                        temp_op.pop(s)
                        s=0
                        #temp_num.append(result[s]*result[s+1]) 
                
                else:
                    s+=1
                    # else:
                    #     temp_num.append(result[s])
                    #     temp_op.append(seq[s])
            #result=temp_num
            #seq=temp_op
            #print(temp_num,temp_op)
        #print(temp_num)
        if abs(temp_num[0])>answer:
            answer=abs(temp_num[0])
        #print(result)
            
            
    
#     for i in seq: 
#         for j in range(len(seq)):
#             if i==j:
                
#         while i[0] in seq:
            
            
            
    
    #answer = 0
    
    return answer