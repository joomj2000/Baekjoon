'''
100 200 300 400 500 600 이런식으로 만들고 
list를 set으로 바꾼후 list의 원소의 개수와 set의 원소의 개수가 같으면 최소성 만족

만족안하는 애들끼리 조합 뽑기 2개 짜리 부터.. 


'''
from itertools import combinations
def solution(relation):
    colum_num=len(relation[0])
    index=[i for i in range(colum_num)]
    answer=set()
    relation = list(map(list, zip(*relation)))
    
    
    for k in range(1,colum_num+1): #조합 계산
        result=[]
        for comb in list(combinations(index,k)):
            is_subset=False
            result=list(zip(*[relation[l] for l in comb]))
            
            if len(result)==len(set(result)):
                for l in answer:
                    if set(l).issubset(comb):
                        is_subset=True
                        break
                if is_subset==False:
                    answer.add(comb)
            
                    
                        
    # for col in relation:
    #     if len(col)==len(set(col)):
    #         answer[0]+=1
    # print(answer)
    # for i in range(1,len(answer)):
    #     answer[i]-=answer[i-1]*(colum_num-i)
   # print(answer)
        

    return len(answer)
