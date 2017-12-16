# Created by Inseong on 2017-12-08

CONST = 1000000

def  common_uncommon(lst, n):
    str_list = list(map(lambda x:x[2], lst))
    common = []
    uncommon = []
    for ele in lst:
        cnt = str_list.count(ele[2])
        if cnt >= n :
            timeSum = 0
            minTime = ele[0]
            l = list(filter(lambda x:x[2]==ele[2], lst))
            for i in l:
                timeSum += (i[1]-i[0])
                minTime = min(minTime, i[0])
            common.append((ele[2],cnt, timeSum, minTime))
            str_list = list(filter(lambda  x:x!=ele[2], str_list))

        elif cnt == 1:
            uncommon.append((ele[2], ele[0]))
            str_list = list(filter(lambda x: x != ele[2], str_list))
    uncommon = list(map(lambda x:x[0],sorted(uncommon, key=lambda x:x[1])))
    common = sorted(common, key = lambda x:x[1],reverse = True)
    i=0
    while i<len(common):
        t = i
        while t+1<len(common) and common[t+1][1]==common[i][1]:
            t+=1
        if t-i>0:
            common[i:t+1] = sorted(common[i:t+1],key=lambda x:x[2],reverse = True)
        i = t+1
    i=0
    while i < len(common):
        t = i
        while t + 1 < len(common) and common[t + 1][1] == common[i][1] and common[t+1][2]==common[i][2]:
            t += 1
        if t - i > 0:
            common[i:t + 1] = sorted(common[i:t + 1], key=lambda x: x[3])
        i = t + 1
    common = list(map(lambda x:x[0], common))
    return [common, uncommon]


print(common_uncommon([(1,5,"home"),(7,9,"home"), (11,17,"school"),(20, 25, "school"),(26,40,"cafe"),(41,57,"lib"),(58,59,"bus"),\
                       (59,60,"seoul"),(61,62,"seoul"),(63,64,"seoul")],2))