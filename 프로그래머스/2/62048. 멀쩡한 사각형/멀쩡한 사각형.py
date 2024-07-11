import math

def solution(w,h):
    answer = 1
    all=w*h
    GCD=math.gcd(w,h)
    if GCD<=w and GCD<=h:
        w/=GCD
        h/=GCD
        not_available=(w+h-1)*GCD
    else:
        not_available=w+h-1
    answer=all-not_available
    
    return answer