N,M = map(int,input().split(' '))
no_listen=set([input() for _ in range(N)])
no_look=set([input() for _ in range(M)])

no_listen_and_look=sorted(list(no_look & no_listen))

print(len(no_listen_and_look))

for i in no_listen_and_look:
    print(i)