# Created by Inseong on 2017-12-15

import ctp17hw1


def suggest_similar(lst, loc_lst, d, k):
    const = 1
    result = []
    str_list = list(map(lambda x:x[2], lst))
    filtered_list = filtering(str_list, loc_lst)
    for name in str_list:
        if str_list.count(name) == 1:
            cur_loc = find_loc(name, loc_lst)
            for loc in filtered_list:
                print(name, loc[2])
                print(ctp17hw1.dist(cur_loc[0]/const, cur_loc[1]/const, loc[0]/const, loc[1]/const))
                print(similarity(cur_loc, loc))
                if ctp17hw1.dist(cur_loc[0]/const, cur_loc[1]/const, loc[0]/const, loc[1]/const)<d and similarity(cur_loc, loc) >=k:
                    if not loc[2] in result:
                        result.append(loc[2])
    return result

def find_loc(name, loc_lst):
    for i in loc_lst:
        if i[2] == name:
            return i

def filtering(str_lst, loc_lst):
    filtered_list = loc_lst[:]
    for i in str_lst:
        filtered_list = list(filter(lambda x:x[2]!=i, filtered_list))
    return filtered_list

def similarity(loc1, loc2):
    if len(loc1) == 0 and loc2 == 0:
        return -1.0
    keywords1 = loc1[3][:]
    keywords2 = loc2[3][:]
    union = []
    for i in keywords1:
        if i in keywords2:
            keywords2.remove(i)
        union.append(i)
    union += keywords2
    # print(union)
    intersection = []
    keywords1 = loc1[3][:]
    keywords2 = loc2[3][:]
    for i in keywords1:
        if i in keywords2:
            a = keywords1.count(i)
            b = keywords2.count(i)
            for _ in range(b):
                keywords2.remove(i)
            intersection += [i]*min(a, b)
    # print(intersection)
    print (intersection, union)
    print(len(intersection)/len(union))

    return len(intersection)/len(union)

print(1/2)


print(ctp17hw1.dist(1.1,1.1,1.7,1.7))
loc_list = [(1.1,  5.0 , "seoul",  ["agd","ab"]), \
            (1.7,  5.0, "newyork", ["agd", "ab"]),
            (90.0,  5.0, "cafe", ["agd", "ab"]),
            (90.0,  5.0, "home", ["agd", "ab"]),
            (90.0,  5.0, "bus", ["agd", "ab"]),
            (1.6,  5.0, "lib", ["agd", "ab"]),
            (1.4, 5.0, "usa", ["agd","ab"]),
            (1.7, 5.0 , "europe", ["agd"])]
print(suggest_similar([(1,5,"home"),(7,9,"home"), (11,17,"school"),(20, 25, "school"),(26,40,"cafe"),(41,57,"lib"),(58,59,"bus"),\
                       (59,60,"seoul"),(61,62,"seoul"),(63,64,"seoul")],loc_list,40000,0.2))