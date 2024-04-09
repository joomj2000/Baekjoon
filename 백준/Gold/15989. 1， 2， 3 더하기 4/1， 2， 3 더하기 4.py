import sys

d=[1]*10001 #dp 테이블 초기화 = 1로만 나타낼 수 있을때 경우의 수

T=int(sys.stdin.readline()) # 테스트 개수

for i in range(2,10001): #2가 추가되었을때 경우의 수
    d[i]+=d[i-2]
for i in range(3,10001): #3이 추가되었을때 경우의 수
    d[i]+=d[i-3]

for _ in range(T):
    n=int(sys.stdin.readline())
    print(d[n]) # n을 1,2,3의 합으로 나타내는 방법의 총 수 출력