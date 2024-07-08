'''
가장 많이 나온것 -> 가장 적게 나온것 (딕셔너리 이용)
'''

def solution(s):
    answer = []
    #print(s)
    dic={}
    num=0
    while num<len(s):
        temp=''

        while s[num]!='{' and s[num]!='}' and s[num]!=',':
            temp+=s[num]
            num+=1
            
        if temp!='':
            if int(temp) not in dic:
                dic[int(temp)]=1
            else:
                dic[int(temp)]=dic[int(temp)]+1
            #dic(int(s))=dic(int(s)).get(0)+1
        num+=1
    
    #for k,v in dict:
    #dict
    
    #print(dic)
    for i in range(len(dic)+1): #0 1 2 3 
        for k,v in dic.items():
            if v== len(dic)-i+1:
                answer.append(k)
    
    return answer