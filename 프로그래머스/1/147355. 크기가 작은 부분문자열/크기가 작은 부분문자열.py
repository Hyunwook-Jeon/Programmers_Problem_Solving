def solution(t, p):
    answer = 0
    a = len(t)
    b = len(p)
    
    for i in range(a-b+1):
        num_t=0
        for j in range(b):
            num_t+=int(t[i+b-1-j])*(10**j)
        if num_t <= int(p):
            answer+=1
    return answer