'''
가장 작은 숫자보다 큰 값이 남을 경우가 이득?
-> 가장 작은 값으로 나누어서 몫이 가장 큰 것들중 가장 큰 수 선택
그게 없으면 그냥 가장 큰 수가 이득

'''

import sys
N=int(sys.stdin.readline())
price={}
min_p=100

temp=list(map(int,sys.stdin.readline().split()))
#print(temp)
for i in range(len(temp)):
    price[i]=temp[i]
    if min_p>temp[i]:
        min_p=temp[i]
M=int(sys.stdin.readline())
#print(price,min_p)
answer=[]

# for k, v in price.items():
#     if k!=0 and (M - v) // min_p >= check:
#         check = (M - v) // min_p
#         room_num = k
#         to_pay = v
# answer.append(room_num)



while(M>=min_p): # 가장 작은 수도 살수 없을때까지 반복
    check=0
    room_num=-1
    for k,v in price.items():
        if answer==[] and k==0:
            continue
        if (M-v)//min_p>=check:
            check=(M-v)//min_p
            room_num=k
            to_pay=v
    if room_num ==-1:
        answer.append(0)
        break
    answer.append(room_num)
    M-=to_pay
   # print(M)


for ans in answer:
    print(ans,end='')
#print(''.join(*answer))
