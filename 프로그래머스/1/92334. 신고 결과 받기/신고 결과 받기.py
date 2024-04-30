def solution(id_list, report, k):
    bad_user_cnt={}
    user_dict={}
    answer = [0]*len(id_list)
    cnt=0
    temp=0
    for i in id_list:
        bad_user_cnt[i]=set()
        user_dict[i]=temp
        temp+=1
        
    for j in report:
        reporter,bad_user=j.split(' ')
        bad_user_cnt[bad_user].add(reporter)
    for x in bad_user_cnt:
        if len(bad_user_cnt[x])>=k:
            for l in bad_user_cnt[x]: 
                answer[user_dict[l]]+=1
            
    
    return answer