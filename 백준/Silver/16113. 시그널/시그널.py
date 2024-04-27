import sys

N=int(sys.stdin.readline())
signal=list(sys.stdin.readline())
signal_matrix= [list(signal[i:i+N//5]) for i in range(0, len(signal), N//5)]

num_dict={
    0:['#','#','#','#','#','#','.','.','.','#','#','#','#','#','#'],
    1:['#','#','#','#','#'],
    2:['#','.','#','#','#','#','.','#','.','#','#','#','#','.','#'],
    3:['#','.','#','.','#','#','.','#','.','#','#','#','#','#','#'],
    4:['#','#','#','.','.','.','.','#','.','.','#','#','#','#','#'],
    5:['#','#','#','.','#','#','.','#','.','#','#','.','#','#','#'],
    6:['#','#','#','#','#','#','.','#','.','#','#','.','#','#','#'],
    7:['#','.','.','.','.','#','.','.','.','.','#','#','#','#','#'],
    8:['#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#'],
    9:['#','#','#','.','#','#','.','#','.','#','#','#','#','#','#']
}
check=[]
for i in range(N//5):
    temp=[]
    for j in range(5):
        temp.append(signal_matrix[j][i])
    #print(temp)
    if temp==['.','.','.','.','.']:
        for k,v in num_dict.items():
            #print(check)
            #print(v)
            if v==check:
                print(k,end='')
                check=[]
                break
    else:
        check.extend(temp)
for k,v in num_dict.items():
    #print(check)
    #print(v)
    if v==check:
        print(k,end='')

#print(signal_matrix)