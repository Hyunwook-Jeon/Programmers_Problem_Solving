def solution(n, w, num):
    answer = 0
    if w == 1: 
        answer = n-num+1
    elif n%w == 0:
        answer = (n//w-(num-1)//w)
    else :
        a = n//w
        b = n%w
        arr =[]
        
        if a%2 ==1 : 
            for i in range(a+1):
                if i == a:
                    for j in range(b):  
                        arr.append(a-((n-((a-i)*w)-1)//w)+1)
                elif i%2 == 1:
                    for j in range(b):
                        arr.append(a-(n-((a-i)*w)-1)//w+1)
                    for k in range(w-b):
                        arr.append(a-(n-((a-i)*w)-1)//w)
                else :
                    for j in range(w-b):
                        arr.append(a-(n-((a-i)*w)-1)//w)
                    for k in range(b):
                        arr.append(a-((n-((a-i)*w)-1)//w)+1)
        else:
            for i in range(a+1):
                if i == a:
                    for j in range(b):  
                        arr.append(a-((n-((a-i)*w)-1)//w)+1)
                elif i%2 == 1:
                    for j in range(w-b):
                        arr.append(a-(n-((a-i)*w)-1)//w)
                    for k in range(b):
                        arr.append(a-(n-((a-i)*w)-1)//w+1)
                else :
                    for j in range(b):
                        arr.append(a-(n-((a-i)*w)-1)//w+1)
                    for k in range(w-b):
                        arr.append(a-((n-((a-i)*w)-1)//w))
        
        answer = arr[num-1]
            
    return answer