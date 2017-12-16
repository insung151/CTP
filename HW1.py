# import ctp17hw1
#
#
# # Exercise 1
# def make_timestamped_loc(lati, long, time) :
#     dic = {}
#     dic['latitude'] = lati
#     dic['longitude'] = long
#     dic['timestamp'] = time
#     return dic
#
# # Exercise 2
# def sort_locs(l) :
#     l = sorted(l, lambda x : x['timestamp'])
#     return l
#
# # Exercise 3
# def total_dist(l) :
#     distant = 0
#     for i in range(len(l)-1):
#         distant += ctp17hw1.dist(l[i]['latitude'], l[i]['longitude'], l[i+1]['latitude'], l[i+1]['longitude'])
#     return distant
#
# # Exercise 4
# def total_walked_dist(l) :
#     walked_distant = 0
#     for i in range(len(l) - 1):
#         distant = ctp17hw1.dist(l[i]['latitude'], l[i]['longitude'], l[i + 1]['latitude'], l[i + 1]['longitude'])
#         if (distant / (l[i+1]['timestamp'] - l[i]['timestamp'])) >
#     return distant
