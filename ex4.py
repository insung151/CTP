# HW1 Exercise 4

import ctp17hw1
# now you can use ctp17hw1.dist()

def total_walked_dist(lst):
    walked_distant = 0
    for i in range(len(lst) - 1):
        distant = ctp17hw1.dist(lst[i]['latitude'], lst[i]['longitude'], lst[i + 1]['latitude'], lst[i + 1]['longitude'])
        if (distant / (lst[i + 1]['timestamp'] - lst[i]['timestamp'])) < 5:
            walked_distant += distant
    return walked_distant

# test example; should be erased before submitting.
# loc1 = {'latitude':1.2, 'longitude':3.4, 'timestamp':100}
# loc3 = {'latitude':9.1, 'longitude':2.3, 'timestamp':200}
# loc2 = {'latitude':5.6, 'longitude':7.8, 'timestamp':300}
# print(total_walked_dist([loc1, loc3, loc2]))