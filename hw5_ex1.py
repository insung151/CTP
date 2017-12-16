# Created by Inseong on 2017-12-08

CONST = 1000000

def  common_uncommon(lst, n):
    str_list = list(map(lambda x:x[2], lst))
    common = []
    uncommon = []
    for ele in lst:
        cnt = str_list.count(ele[2])
        if cnt >= n :
            minTime = ele[0]
            for i in list(filter(lambda x:x[2]==ele[2], lst)):
                minTime = min(minTime, i[0])
            str_list = list(filter(lambda  x:x!=ele[2], str_list))
            common.append((ele[2], minTime))
        elif cnt == 1:
            timeSum = 0
            minTime = ele[0]
            l = list(filter(lambda x:x[2]==ele[2], lst))
            for i in l:
                timeSum += (i[1]-i[0])
                minTime = min(minTime, i[0])
            uncommon.append((ele[2], cnt, timeSum, minTime))
            str_list = list(filter(lambda x: x != ele[2], str_list))
    common = list(map(lambda x:x[0],sorted(common, key=lambda x:x[1])))
    uncommon = sorted(uncommon, key = lambda x:x[1],reverse = True)
    i=0
    while i<len(uncommon):
        t = i
        while t+1<len(uncommon) and uncommon[t+1][1]==uncommon[i][1]:
            t+=1
        if t-i>0:
            uncommon[i:t+1] = sorted(uncommon[i:t+1],key=lambda x:x[2],reverse = True)
        i = t+1
    i=0
    while i < len(uncommon):
        t = i
        while t + 1 < len(uncommon) and uncommon[t + 1][1] == uncommon[i][1] and uncommon[t+1][2]==uncommon[i][2]:
            t += 1
        if t - i > 0:
            uncommon[i:t + 1] = sorted(uncommon[i:t + 1], key=lambda x: x[3])
        i = t + 1
    uncommon = list(map(lambda x:x[0], uncommon))
    return [uncommon, common]

