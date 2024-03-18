N=int(input())
time = list(map(int, input().split()))
time.sort()
result=0
for i in range(len(time)):
    result+=time[i]*(len(time)-i)
print(result)

