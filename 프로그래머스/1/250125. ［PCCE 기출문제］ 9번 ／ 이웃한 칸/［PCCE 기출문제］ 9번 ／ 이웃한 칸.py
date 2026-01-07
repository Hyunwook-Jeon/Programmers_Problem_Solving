def solution(board, h, w):
    height = len(board)
    length = len(board[0])
    answer = 0
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    for i in range(4):
        h_check=h+dh[i]
        w_check=w+dw[i]
        if 0<=h_check<height and 0<=w_check<length:
            if board[h][w]==board[h_check][w_check]:
                answer+=1
    return answer