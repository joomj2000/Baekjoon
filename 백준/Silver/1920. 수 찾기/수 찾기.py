N = int(input())
A = set(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

for num in target:
    if num in A:
        print("1")
    else:
        print("0")
