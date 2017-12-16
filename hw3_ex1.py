# Created by inseong on 2017-11-14
import ctp17hw1

def count_near(loc_lst, k):
    cur = loc_lst[0]
    visit = [0]*len(loc_lst)
    visit[0] = 1
    for i in range(len(loc_lst)-1):
        if ctp17hw1.dist(cur[0], cur[1], loc_lst[i+1][0], loc_lst[i+1][1])<=k and visit[i+1]==0:
            visit[i+1] = 1
            visit = count_helper(loc_lst, i+1, visit, k)
    return sum(visit)-1

def count_helper(loc_lst, cur, visit, k):
    for i in range(len(loc_lst)-1):
        if ctp17hw1.dist(loc_lst[cur][0], loc_lst[cur][1], loc_lst[i+1][0], loc_lst[i+1][1]) <= k and visit[i+1] == 0:
            visit[i+1] = 1
            visit = count_helper(loc_lst, i+1, visit, k)
    return visit

# print(ctp17hw1.dist(0.4,0.5,0.4,0.6))
#
# print(count_near([(0.3,0.2),(0.4,0.),(0.3,0.3),(0.4,0.6)],25000))5