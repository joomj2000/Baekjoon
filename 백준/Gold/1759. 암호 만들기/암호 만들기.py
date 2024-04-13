import sys

def backtracking():
    if len(password)==L:
        cnt=0
        for i in vowel:
            cnt+=password.count(i)
        if cnt>0 and L-cnt>1:
        #if password in 'a' or 'e' or 'i' or 'o' or 'u'
            print("".join(map(str,password)))
        return
    for i in word:
        if i not in password:
            if len(password)==0 or password[-1]<i:
                password.append(i)
                backtracking()
                password.pop()


L,C=map(int,sys.stdin.readline().split())
word=list(sys.stdin.readline().split())
word.sort()
password=[]
vowel='aeiou'
backtracking()
# num=[]
# backtracking()
# print('')