import sys
#sys.setrecursionlimit(1000000000)
# def backtracking():
#     if len(password)==L:
#         print("".join(map(str,password)))
#         return
#     for i in word:
#         if i not in password:
#             password.append(i)
#             backtracking()
#             password.pop()

def make_False(i,j):
    #possible_table[i][j]+=1
    temp_i=i
    temp_j=j
    while(0<=temp_i<N and 0<=temp_j<N):
        possible_table[temp_i][temp_j] +=1  # 왼쪽아래
        temp_i += 1
        temp_j -= 1
    temp_i = i
    temp_j = j
    while (0 <= temp_i < N and 0 <= temp_j < N):
        possible_table[temp_i][temp_j] +=1  # 오른쪽아래
        temp_i += 1
        temp_j += 1

    for k in range(i+1,N):
        possible_table[k][j] +=1  # 오른쪽아래

    #possible_table[i][j]-=1


def make_True(i, j):
    #possible_table[i][j]-=1
    temp_i = i
    temp_j = j
    while (0 <= temp_i < N and 0 <= temp_j < N):
        if possible_table[temp_i][temp_j] > 0:
            possible_table[temp_i][temp_j] -=1 # 왼쪽아래
        temp_i += 1
        temp_j -= 1
    temp_i = i
    temp_j = j
    while (0 <= temp_i < N and 0 <= temp_j < N):
        if possible_table[temp_i][temp_j]>0:
            possible_table[temp_i][temp_j] -=1  # 오른쪽아래
        temp_i += 1
        temp_j += 1

    for k in range(i+1,N):
        if possible_table[k][j] > 0:
            possible_table[k][j] -=1  # 오른쪽아래

    #possible_table[i][j] += 1

def backtracking(i,j):
    if i>=N :
        #print('!')
        global num
        num+=1
        return
    for j in range(N):
        #print(i,j)
        if possible_table[i][j]==0:
            #defore_False = [row[:] for row in possible_table]
            make_False(i,j)
            #print(possible_table)
            backtracking(i+1,j)
            #print('before make true',i,j,':',possible_table)
            make_True(i, j)
            #print('after make true',possible_table)
            #possible_table=[row[:] for row in defore_False]
            #make_True(i,j)

    return


N=int(sys.stdin.readline())
possible_table=[]
for i in range(N):
    possible_table.append([0] * N)

num=0
# for j in range(N):
#     possible_table = []

backtracking(0, 0)
    # for i in range(N):
    #     possible_table.append([0] * N)
    # backtracking(0,j)
print(num)
