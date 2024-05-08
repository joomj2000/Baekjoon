def solution(friends, gifts):
    answer = [0]*len(friends) #friends 순서로 선물을 받을 리스트
    
    #이름을 인덱스로 저장한 딕셔너리 (0부터)
    friends_dict={}
    for i in range(len(friends)):
        friends_dict[friends[i]]=i
    
    #선물 지수 표
    present=[0]*len(friends)
    #print(present)
    #선물 주고 받은 표만들기
    graph=[[0]*len(friends) for _ in range(len(friends))]
    for gift in gifts:
        graph[friends_dict[gift.split()[0]]][friends_dict[gift.split()[1]]]+=1
        present[friends_dict[gift.split()[0]]]+=1
        present[friends_dict[gift.split()[1]]]-=1
    
    for p1 in range(len(friends)):
        for p2 in range(p1,len(friends)):
            #print(graph[p1][p2])
            if p1==p2:
                continue
            if graph[p1][p2]>graph[p2][p1]:
                answer[p1]+=1
            elif graph[p1][p2]<graph[p2][p1]:
                answer[p2]+=1
            else:
                if present[p1]>present[p2]:
                    answer[p1]+=1
                elif present[p2]>present[p1]:
                    answer[p2]+=1
                    
                
                
        
    print(answer)
    
    
    
    return max(answer)