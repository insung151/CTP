# Created by inseong on 2017-11-30

def  sanitize_and_sort(loc_lst):
    result = list(filter(lambda x: is_valid2(x), loc_lst))
    result = sorted(result, key=lambda x : x['timestamp'])
    return result

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

# loc= {'latitude':90.0, 'longitude': -5.1 , 'name' :"ag", 'keywords' : ["agd","ab"], 'timestamp' :4}
# loc2 = {'latitude':90.0, 'longitude': -5.1 , 'name' :"ag", 'keywords' : ["agd","ab"], 'timestamp' :4.1}
# loc3 = {'latitude':90.0, 'longitude': -5.1 , 'name' :"ag", 'keywords' : ["agd","ab"], 'timestamp' :1}
# print(sanitize_and_sort([loc, loc2, loc3]))