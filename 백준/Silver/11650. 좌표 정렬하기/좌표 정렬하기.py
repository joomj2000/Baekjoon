N=int(input())
coordinate=[]
for _ in range(N):
    x,y=map(int, input().split())
    coordinate.append([x,y])

for x,y in sorted(coordinate):
    print(f"{x} {y}")
