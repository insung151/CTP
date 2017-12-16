# Created by inseong on 2017-11-15

def sub_areas(loc_lst, k):
    return sub_helper(loc_lst, (0, 90), (60,150), k)

def sub_helper(loc_lst, s, e, k):
    if len(loc_lst) == 0:
        return 0
    if len(loc_lst) <= k:
        return 1
    else:
        mid = ((s[0]+e[0])/2 , (s[1]+e[1])/2)
        a = []
        b = []
        c = []
        d = []
        for loc in loc_lst:
            if mid[0] > loc[0] and mid[1] > loc[1]:
                a.append(loc)
            elif mid[0] > loc[0] and mid[1] <= loc[1]:
                b.append(loc)
            elif mid[0] <= loc[0] and mid[1] > loc[1]:
                c.append(loc)
            # mid[0] < loc[0] and mid[1] < loc[1]
            else :
                d.append(loc)
        return sub_helper(a, (s[0],s[1]), (mid[0], mid[1]),k) + sub_helper(b, (s[0],mid[1]), (mid[0],e[1]) ,k) \
               + sub_helper(c, (mid[0], s[1]), (e[0],mid[1]), k) + sub_helper(d, (mid[0], mid[1]), (e[0], e[1]),k)

# print(sub_areas([(44, 102), (0, 101), (48, 115), (19, 120), (51, 104), (45, 127), (40, 110), (22, 113), (14, 148), (7, 102)], 2))