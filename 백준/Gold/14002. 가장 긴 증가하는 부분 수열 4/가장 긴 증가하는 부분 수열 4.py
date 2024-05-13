import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
dp = [1] * (n+1)
dp_result=[[i] for i in sequence]
#print(dp_result)
for i in range(len(sequence)):
    temp_dp_result = []
    for j in range(i): #이전까지의 수가 현재보다 작으면 dp테이블 값 조회
        if sequence[j] < sequence[i]:
            #dp[i] = max(dp[i], dp[j]+1)
            if dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
                temp_dp_result=[]
                #print(temp_dp_result)
                for l in dp_result[j]:
                    #print(dp_result[j])
                    temp_dp_result.append(l)
    dp_result[i].extend(temp_dp_result)
    #print(dp_result)


print(max(dp))
for result in dp_result:
    if max(dp)==len(result):
        print(*sorted(result))
        break
#print(dp_result)
