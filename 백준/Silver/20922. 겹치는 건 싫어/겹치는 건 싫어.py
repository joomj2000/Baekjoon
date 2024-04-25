import sys
N,K=map(int,sys.stdin.readline().split())
num_list=list(map(int,sys.stdin.readline().split()))
#print(num_list)
num_dict={num_list[0]:1}
max_cnt=0
j=1
cnt=1
for i in range(N):
    while j<N:
        if num_dict.get(num_list[j],-1)+1>K:
            break
        num_dict[num_list[j]]=num_dict.get(num_list[j],0)+1
        cnt+=1
        j+=1

    #print('dict',num_dict,'cnt',cnt)
    if max_cnt<cnt:
        max_cnt=cnt
    num_dict[num_list[i]]-=1
    cnt-=1

print(max_cnt)




