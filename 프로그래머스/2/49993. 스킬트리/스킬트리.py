def solution(skill, skill_trees):
    answer = 0
    skill_len=len(skill)
    i=0

    for skill_tree in skill_trees:
        #print(f"s {skill_tree}")
        index=[-1]*skill_len
        i=0
        for skill_apha in skill:
            if skill_apha in skill_tree:
                print(skill_apha, skill_tree)
                index[i]=skill_tree.index(skill_apha)
            i+=1
            
        is_pos=True
        for i in range(skill_len):
            for j in range(i+1,skill_len):
                if (index[i]>index[j] and index[j]!=-1) or (index[i]==-1 and index[j]!=-1):
                    is_pos=False
                    break
        if is_pos:
            print(f"{skill_tree}:  {index}")
            answer+=1
                    
    print(answer)
        
        
        

    
    
    
    return answer