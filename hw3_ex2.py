# Created by inseong on 2017-11-15

import ctp17hw1

def shortest_route(loc_lst, my_loc):
    visit = [0]*len(loc_lst)
    result = -1
    for i in range(len(loc_lst)):
        l = dfs(visit, i, loc_lst, my_loc) + ctp17hw1.dist(loc_lst[i][0],loc_lst[i][1],my_loc[0],my_loc[1])
        if result == -1:
            result = l
        else:
            result = min(l, result)
    return result

def dfs(visit, start, loc_lst, my_loc):
    result = -1
    visit[start] = 1

    if sum(visit) == len(visit):
        visit[start] = 0
        return ctp17hw1.dist(loc_lst[start][0],loc_lst[start][1],my_loc[0],my_loc[1])


    for i in range(len(loc_lst)):
        if visit[i] == 0:
            l = ctp17hw1.dist(loc_lst[start][0],loc_lst[start][1],loc_lst[i][0],loc_lst[i][1])+\
                         dfs(visit, i, loc_lst, my_loc)
            if result == -1:
                result = l
            else:
                result = min(l, result)
    visit[start] = 0
    return result

print(shortest_route([(1.9653665587363849, 0.7723675616973618), (0.32384093263953084, 1.7674877091436358), (1.6184797557083082, 1.846095269619388), (1.113590592344326, 1.0302964721851797), (1.6309947945007637, 0.5159775509463409), (0.783131353207484, 1.42945124597273), (0.7309129098864924, 0.18955181317847036), (1.6958708180629105, 0.5832518153304984), (0.7326686607022435, 0.9657554447699066),(0.1,0.4)], (0,0)))
# print(ctp17hw1.dist(0, 0, 0.3, 0.3)+ctp17hw1.dist(0.3, 0.3, 0.4, 0.5)+ctp17hw1.dist(0.4, 0.5, 0.6, 0.7)+ctp17hw1.dist(0.3, 0.2, 0.6, 0.7)+\
#       ctp17hw1.dist(0.3, 0.2, 0, 0))
# print(len([(1.9653665587363849, 0.7723675616973618), (0.32384093263953084, 1.7674877091436358), (1.6184797557083082, 1.846095269619388), (1.113590592344326, 1.0302964721851797), (1.6309947945007637, 0.5159775509463409), (0.783131353207484, 1.42945124597273), (0.7309129098864924, 0.18955181317847036), (1.6958708180629105, 0.5832518153304984), (0.7326686607022435, 0.9657554447699066)]))