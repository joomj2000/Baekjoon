def solution(msg):
    answer = []
    dic = {}
    for i in range(1, 27):
        dic[chr(ord('A') + i - 1)] = i
    # print(dic)
    value = 27
    while msg:
        if len(msg)==1:
            answer.append(dic[msg])
            break
        i = 0
        j = 1
        # if j>=len(msg):
        #     break
        while msg[i:j] in dic:
            j += 1
            if j>len(msg):
                break
        #print(msg)
        #print(i, j)
        # msg=msg[j-1:]
        answer.append(dic[msg[i:j - 1]])
        dic[msg[i:j]] = value
        value += 1
        #i = j - 1
        #j = i + 1
        msg = msg[j - 1:]
        #print(dic)
        # answer

    return answer