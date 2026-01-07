def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        score = 0
        for j in range(len(name)):
            for k in range(len(photo[i])):
                if name[j] == photo[i][k]:
                    score += yearning[j]
        answer.append(score)
    return answer