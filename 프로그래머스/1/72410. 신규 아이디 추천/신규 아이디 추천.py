def solution(new_id):
    answer = ''
    #1단계
    new_id=new_id.lower()
    Two_answer=""
    for i in range(len(new_id)): # 2단계
        if 'z'>=new_id[i]>='a' or '9'>=new_id[i]>='0' or new_id[i]=='-' or  new_id[i]=='_' or  new_id[i]=='.':
            Two_answer+= new_id[i]
            
    # 3단계
    Three_answer=""
    for j in range(len(Two_answer)):
        if len(Three_answer)!=0 and Three_answer[-1]=='.' and Two_answer[j]=='.':
            continue
        if len(Three_answer)==0 and Two_answer[j]=='.': #4단계(처음 마침표 제거)
            continue
        else:
            Three_answer+=Two_answer[j]
    answer= Three_answer      
    if len(Three_answer)!=0 and Three_answer[-1]=='.': # 4단계 (끝 마침표 제거)
        answer=Three_answer[:len(Three_answer)-1]
        #print(Three_answer)
    #print(Three_answer[])
    
    if answer=='': # 5단계
        answer="a"
    
    if len(answer)>=16: #6단계
        answer=answer[:15]
        if answer[-1:]=='.':
            answer=answer[:len(answer)-1]
    #if len(answer)!=0 and answer[-1]=='.': 
        #answer=answer[:len(answer)-1]
    #answer=list(answer)
    while len(answer)<=2: #7단계
        #print(1)
        #print(answer[-1:])
        answer+=answer[-1:]
        #answer+=answer[:-1]
        
        

    #print(answer)
            
    return answer