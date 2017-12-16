# HW1 Exercise 3

import ctp17hw1
# now you can use ctp17hw1.dist()

def total_dist(lst):
    distant = 0
    for i in range(len(lst) - 1):
        distant += ctp17hw1.dist(lst[i]['latitude'], lst[i]['longitude'], lst[i + 1]['latitude'], lst[i + 1]['longitude'])
    return distant

# test example; should be erased before submitting.
# loc1 = {'latitude':1.2, 'longitude':3.4, 'timestamp':100}
# loc3 = {'latitude':9.1, 'longitude':2.3, 'timestamp':200}
# loc2 = {'latitude':5.6, 'longitude':7.8, 'timestamp':300}
# print(total_dist([loc1, loc3, loc2]))
# print(ctp17hw1.dist(loc1['latitude'], \
# 					loc1['longitude'], \
# 					loc2['latitude'], \
# 					loc2['longitude']))