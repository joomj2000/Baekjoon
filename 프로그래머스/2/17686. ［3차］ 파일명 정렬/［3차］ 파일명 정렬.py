import re
def solution(files):
    file_list=[[] for _ in range(len(files))]
    cnt=0
    for file in files:
        match = re.search(r'\d+', file)
        if match:
            # Extract the parts based on the match position
            start, end = match.span()
            part1 = file[:start]
            part2 = file[start:end]
            part3 = file[end:]
            file_list[cnt].append(part1)
            file_list[cnt].append(part2)
            file_list[cnt].append(part3)
            cnt+=1
            #return part1, part2, part3
            
    #file_list.sort(key=lambda x: x[0],x[1])
    #print(file_list)
    sorted_data = sorted(file_list, key=lambda x: (x[0].lower(), int(x[1])))

    answer = []
   # print(sorted_data)
    for data in sorted_data:
        temp=''
        for i in data:
            temp+=i
        answer.append(temp)
        #print(str(*data))
    
    return answer