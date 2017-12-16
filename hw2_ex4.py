# Created by inseong on 2017-10-28
import json, ctp17hw1

f = open("named_locs.json" , mode = 'r', encoding='utf-8')
jsonstr = f.read()
f.close()
data = json.loads(jsonstr)

def stop_by(curLati, curLong, desLati, desLong, keywords, maxLen):
    result = []
    for s in data:
        isAllContain = True
        for keyword in keywords:
            if not keyword in s['keywords']:
                isAllContain = False
                break
        if isAllContain and (ctp17hw1.dist(curLati, curLong, s['latitude'], s['longitude']) + \
                                     ctp17hw1.dist(s['latitude'], s['longitude'], desLati, desLong)) < maxLen:
            result.append(s['name'])
    return result


# print(stop_by(37.477155, 126.963423, 37.459250, 126.950786, ["Matjip", "Honbap"], 3500))