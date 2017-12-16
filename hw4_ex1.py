# Created by inseong on 2017-11-30

def is_valid1(loc):
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

