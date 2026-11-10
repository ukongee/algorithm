    #매일다르게 조합
    #종류별로 최대 1가지 의상만 착용가능
    #전날과 겹치는거 있어도되는데 조합만 다르면됨
def solution(clothes):
    #[의상의 이름, 의상의 종류]입력
    #종류가 두가지면 
    cnt = {}
    a=1
    for i,j in (clothes):
        #key같은거있으면 value ++1
        if j in cnt.keys():
            cnt[j] +=1
        else:
            cnt[j] = 1
            
        #(vlue+1)끼리 곱하고 -1
    for i in (cnt.values()):
        a*= (i+1)
        
    answer= a-1

        
    
    return answer