
import math

def solution(fees, records):
    answer = []
    car_dict={}
    for record in records:
        time, num, value=record.split()
        time=int(time.split(':')[0])*60+int(time.split(':')[1])
        print(time)
        if value=='IN':
            if num not in car_dict : #없던 번호이면 생성
                car_dict[num]=[[time,1439]]
            else:
                car_dict[num].append([time,1439])
        else:
            car_dict[num][-1][1]=time
    
    # 차량번호를 기준으로 정렬 
    sorted_car_dict = dict(sorted(car_dict.items()))        
    print(sorted_car_dict)
    for car,times in sorted_car_dict.items():
        result=fees[1]
        result_time=0
        for time in times:
            result_time+=(time[1]-time[0])
        if result_time>fees[0]:
            result+=math.ceil((result_time-fees[0])/fees[2])*fees[3]  
        
        answer.append(result)
        
    
    return answer