
#값들 초기화?
def solution(survey, choices):
    d={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    answer=''
    #servey에서 순회하면서 하나씩 뽑음 for i in (servey)
    #zip으로 묶어서 딕셔너리로 만듦 "AN"=5, "CF"=3
    
    #값이 1,2,3,4,5,6,7
    for i in range(len(survey)):
        if choices[i] < 4:
            d[survey[i][0]] += abs(choices[i]-4)
        elif choices[i] == 4:
            continue
        else:
            d[survey[i][1]] += abs(choices[i]-4)
            
            
    #4를 기준으로 if <4이면 키의 i[0]에 더해주기
    #1이면3, 2이면2, 3이면1
    
    #if >4이면 키의 i[1]에 더해주기
    #5면1, 6이면2, 7이면3
    
  
    for a,b in ['RT','CF','JM','AN']:
        if d[a]>=d[b]:
            answer+= a
        else:
            answer+=b
    #네가지 ex)RCJA
    #각 지표에서 큰값으로 결정해서 나오면됨
    return answer