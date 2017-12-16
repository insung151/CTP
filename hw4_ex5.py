# Created by Inseong on 2017-11-30

def where_you_at(loc_list, t):
    s = 0
    e = len(loc_list)-1
    while e - s > 0:
        mid = (e + s + 1) // 2

        if loc_list[mid]['timestamp'] == t:
            return loc_list[mid]['name']

        if loc_list[mid]['timestamp'] < t:
            s = mid
        else:
            e = mid - 1
    return loc_list[s]['name']

#
# loc_list = [{'timestamp':4, 'name' : 'a'}, {'timestamp':9, 'name' : 'b'},{'timestamp':10, 'name' : 'c'},{'timestamp':17, 'name' : 'a'}]
# print(where_you_at(loc_list, 17))