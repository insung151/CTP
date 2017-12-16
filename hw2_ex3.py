# Created by inseong on 2017-10-28

import json ,ctp17hw1
f = open("named_locs.json" , mode = 'r', encoding='utf-8')
jsonstr = f.read()
f.close()

data = json.loads(jsonstr)

def nearest(curLati, curLong, keyword):
    name = ""
    for s in data:
        if keyword in s['keywords']:
            minDist = ctp17hw1.dist(curLati, curLong, s['latitude'], s['longitude'])
            name = s['name']
            break

    for s in data:
        if keyword in s['keywords']:
            dist = ctp17hw1.dist(curLati, curLong, s['latitude'], s['longitude'])
            print(dist, s['name'])
            if dist < minDist :
                minDist = dist
                name = s['name']
    return name

# print(nearest(37.481197, 126.952670, "Honbap"))
# print(ctp17hw1.dist(37.481197, 126.952670,37.479211,126.953248))
# print(ctp17hw1.dist(37.481197, 126.952670,37.481320, 126.953418))
# print("========================")
# print(nearest(37.481197, 126.952670, "Muhan Refill"))
