def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_mm,video_ss = map(int,video_len.split(':'))
    pos_mm,pos_ss = map(int,pos.split(':'))
    start_mm,start_ss = map(int,op_start.split(':'))
    end_mm,end_ss = map(int,op_end.split(':'))
    for i in range(len(commands)):
        if start_mm*60+start_ss<=pos_mm*60+pos_ss<=end_mm*60+end_ss:
            pos_mm = end_mm
            pos_ss = end_ss
        if commands[i] == "next":
            pos_ss += 10
            if pos_ss >=60 :
                pos_ss-=60
                pos_mm +=1
            if pos_mm>video_mm:
                pos_mm,pos_ss = video_mm,video_ss
            elif pos_mm==video_mm and pos_ss>=video_ss:
                pos_mm,pos_ss = video_mm,video_ss
                
        elif commands[i] == "prev":
            pos_ss -= 10
            if pos_ss <0:
                pos_ss+=60
                pos_mm-=1
                if pos_mm < 0:
                    pos_mm =0
                    pos_ss =0
        if start_mm*60+start_ss<=pos_mm*60+pos_ss<=end_mm*60+end_ss:
            pos_mm = end_mm
            pos_ss = end_ss
    if len(str(pos_mm))==1:
        pos_mm = '0'+str(pos_mm)
    else:
        pos_mm = str(pos_mm)
    if len(str(pos_ss))==1:
        pos_ss = '0'+str(pos_ss)
    else:
        pos_ss = str(pos_ss)
    answer = pos_mm+":"+pos_ss
        
    return answer