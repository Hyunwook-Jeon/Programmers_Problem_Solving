def solution(wallet, bill):
    answer = 0
    if wallet[0]<wallet[1]:
        a = wallet[0]
        wallet[0] = wallet[1]
        wallet[1] = a
    if bill[0]< bill[1]:
        b = bill[0]
        bill[0] = bill[1]
        bill[1] = b
    while wallet[0]<bill[0] or wallet[1]<bill[1]:
        bill[0] //=2
        answer+=1
        if bill[0]< bill[1]:
            c = bill[0]
            bill[0] = bill[1]
            bill[1] = c        
    return answer