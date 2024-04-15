import sys

def fast_power(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        # 지수가 홀수인 경우
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        # base를 제곱
        base = (base * base) % modulus
    return result

A, B, C = map(int, sys.stdin.readline().split())
result = fast_power(A, B, C)
print(result)
