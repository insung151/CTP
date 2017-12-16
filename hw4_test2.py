# Created by Inseong on 2017-12-16

import json
import ctp.hw4_ex4
f = open("4-4.json", mode='r')
jsonstr = f.read()
f.close()
data = json.loads(jsonstr)
t = data["datalist"]
# print(t[0][0][0])
# print(t[0][0][1])
# print(t[0][1])
for i in range(len(t)):
    if i == 0:
        continue
    if ctp.hw4_ex4.similarity(t[i][0][0],t[i][0][1]) == t[i][1]:
        print("match")
    else:
        print("nope")