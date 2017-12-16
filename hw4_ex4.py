# Created by inseong on 2017-11-30


def similarity(loc1, loc2):
    if not (is_valid2(loc1) and is_valid2(loc2)):
        return -1.0
    keywords1 = loc1['keywords'][:]
    keywords2 = loc2['keywords'][:]
    union = []
    for i in keywords1:
        if i in keywords2:
            keywords2.remove(i)
        union.append(i)
    union += keywords2
    # print(union)
    intersection = []
    keywords1 = loc1['keywords'][:]
    keywords2 = loc2['keywords'][:]
    for i in keywords1:
        if i in keywords2:
            a = keywords1.count(i)
            b = keywords2.count(i)
            for _ in range(b):
                keywords2.remove(i)
            intersection += [i]*min(a, b)
    # print(intersection)
    return len(intersection)/len(union)

def is_valid2(loc):
    if not isvalid(loc):
        return False
    if loc['timestamp'] < 0:
        return False
    if not (-180 <= loc['longitude'] and  loc['longitude'] <=180 and -90 <=loc['latitude'] and loc['latitude'] <= 90):
        return False
    return True


def isvalid(loc):
    checkList = ['latitude', 'longitude', 'timestamp', 'name', 'keywords']
    # key 값이 5개가 아니면 false
    if len(loc.keys() )!= 5:
        return False
    # key가 제대로 있는지 확인
    for i in checkList:
        if not i in loc.keys():
            return False;
    # 타입이 올바른지 확인
    if type(loc[checkList[0]]) != float:
        return False
    if type(loc[checkList[1]]) != float:
        return False
    if type(loc[checkList[2]]) != int :
        return False
    if type(loc[checkList[3]]) != str:
        return False
    if type(loc[checkList[4]]) != list:
        return False
    for i in loc[checkList[4]]:
        if type(i) != str:
            return False
    return True

# print(similarity({'keywords' : ['치킨','피자','치킨','피자']}, {'keywords':['피자','피자']}))