N,K =map(int,input().split(' '))
people_list=[i for i in range(1,N+1)]
result=[]
index = 1
i=0
while len(people_list)>0:
    if i>=len(people_list):
        i=0
    if index%K==0 :
        result.append(people_list[i])
        people_list.pop(i)
        #print(index, people_list)
    else:
        i+=1
    index += 1


print("<",end='')
for i in result[:-1]:
    print(i,end=', ')
print(result[-1],end=">")

#
#
# def dequeue(Q,i):
#     i+1
#
# def main() :
#     # for i in range(N):
#     #     people_queue.append(i+1)
#     while(True):
#         index=0
#         for i in range(1,N+1):
#             index+=1
#             if index==K:
#                 print(K)
#                 index=0
#             else:
#                 enqueue(people_queue,i)
#
#         if people_queue.len==0:
#             break
#
#
# def enqueue(Q,N):
#     Q.append(N)

