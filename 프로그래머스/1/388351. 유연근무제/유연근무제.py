def solution(schedules, timelogs, startday):
    answer = 0
    cnt = 0
    cnt_day = startday
    time_sch = []
    min_sch =[]
    time_logs=[]
    min_logs=[]
    for i in range(len(schedules)):
        time_sch.append(schedules[i]//100)
        min_sch.append(schedules[i]%100)
        for j in range(len(timelogs[i])):
            time_logs.append(timelogs[i][j]//100)
            min_logs.append(timelogs[i][j]%100)
    for i in range(len(schedules)):
        cnt_day = startday
        cnt =0
        for j in range(len(timelogs[i])):
            if (time_sch[i]-time_logs[i*7+j])*60+(min_sch[i]-min_logs[i*7+j]+10)>=0 and 1<= cnt_day <=5 :
                cnt += 1
                if cnt == 5:
                    answer +=1
            cnt_day += 1
            if cnt_day == 8:
                cnt_day = 1
        
    return answer