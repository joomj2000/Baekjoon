def solution(record):
    user_nickname={}
    result=[]
    for i in record:
        commands=i.split()
        if commands[0]!='Leave':
            user_nickname[commands[1]]=commands[2]
        
    answer = []
    
    for i in record:
        commands = i.split()
        if commands[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %user_nickname[commands[1]])
        elif commands[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %user_nickname[commands[1]])
        
    # for j in result:
    #     for k,v in user_nickname.items():
    #         j=j.replace(k,v)
    #     answer.append(j)
    # print(result)
        
    
    return answer