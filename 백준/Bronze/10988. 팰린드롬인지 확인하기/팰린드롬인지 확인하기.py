import sys

word=sys.stdin.readline().strip()
is_p=True
end=len(word)-1
for start in range(len(word)//2):
    if word[start]!=word[end]:
        print(0)
        is_p=False
        break
    else :
        end-=1

if is_p:
    print(1)