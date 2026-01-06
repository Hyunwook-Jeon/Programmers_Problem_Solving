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

'''
추가공부 : sorted(wallet)--> 을 사용하면 오름차순 정렬이 가능함.
def solution(wallet, bill):
    answer = 0
    wallet = sorted(wallet)
    bill = sorted(bill)
    while wallet[0]<bill[0] or wallet[1]<bill[1]:
        bill[-1] //=2
        bill=sorted(bill)
        answer+=1        
    return answer
이런식으로 코드를 구성하면 훨씬 쉽게 작성할 수 있음.
'''
