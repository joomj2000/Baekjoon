def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            # 짝수는 그냥 다음 수가 1개 다름 
            answer.append(number + 1)
        else:# 홀수
            # 가장 오른쪽의 0을 찾고 그 비트를 1로, 바로 다음 비트를 0으로
            bit = '0' + bin(number)[2:]  # 앞에 0을 붙여줌으로써 모든 경우를 커버
            bit_list = list(bit)
            for i in range(len(bit_list) - 1, -1, -1):
                if bit_list[i] == '0':
                    bit_list[i] = '1'
                    bit_list[i + 1] = '0'
                    break
            answer.append(int(''.join(bit_list), 2))
    
    return answer
