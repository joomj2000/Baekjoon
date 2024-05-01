import sys

def BreakEgg(i):
    if i==N:
        break_egg=sum(1 for egg in eggs if egg[0] <= 0)
        #print(eggs)
        global max_num_egg
        if max_num_egg<break_egg:
            max_num_egg=break_egg
        return
    if eggs[i][0]<=0:
        BreakEgg(i + 1)
        return

    # 깰 계란이 남아있는지 확인
    check=True
    for k in range(N):
        if k==i:
            continue
        if eggs[k][0]>0:
            check=False
            break
    if check: # 자기뺴고 다 깨져있는 경우
        max_num_egg=max(max_num_egg,N-1)
        return

    for j in range(N):
        #print(i,j)
        if i != j and eggs[j][0] > 0:
            eggs[j][0] -= eggs[i][1]
            eggs[i][0] -= eggs[j][1]
            BreakEgg(i+1)
            eggs[j][0] += eggs[i][1]
            eggs[i][0] += eggs[j][1]
        # if j==N-1:
        #     BreakEgg(i+1)
    #i+=1



N=int(sys.stdin.readline())
eggs=[]
max_num_egg=0
for _ in range(N):
    eggs.append(list(map(int,sys.stdin.readline().split())))

# for i in range(N):
#     for j in range(N):
#         if i==j and eggs[j][0]>0:
#             BreakEgg(i,j)

BreakEgg(0)
print(max_num_egg)
