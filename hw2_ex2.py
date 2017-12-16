# Created by inseong on 2017-10-28
import json

f = open("named_locs.json" , mode = 'r', encoding='utf-8')
jsonstr = f.read()
f.close()

data = json.loads(jsonstr)

def frequent_keywords():
    frequent_dic = {}
    for s in data:
        for keyword in s['keywords']:
            if keyword in frequent_dic:
                frequent_dic[keyword] += 1
            else:
                frequent_dic[keyword] = 1
    result = sorted(frequent_dic.items(), key = lambda x: x[1] , reverse = True)

    i = 0
    while i < len(result):
        j = i
        while j + 1 < len(result) and result[j][1] ==result[j + 1][1]:
            j += 1
        result[i:j + 1] = sorted(result[i:j + 1], key=lambda x: x[0])
        i = j + 1

    result = list(map(lambda x: x[0], result))

    return result


# if frequent_keywords() ==['Matjip', 'Seoul National Univ. Station', 'Sinchon', 'Sinchon station', 'station', \
#                          'Honbap', 'Hongik Univ.', 'Seoul National Univ.', 'Gopchang', 'Muhan Refill', 'Syarosugil', \
#                          'beautiful', 'cheap', 'date', 'japanese food', 'meat', 'night view', 'tripe', 'view', \
#                          'Braised Spicy Chicken with Vegetables', 'Chadolbagi', 'Ewha Womans Univ.', 'Galbi', 'Jjim Dak', \
#                          'Korean', 'Nakseongdae Station', 'Seoul', 'Sogang Univ.', 'Student Union', 'VR', 'Yonsei Univ.', \
#                          'beef', 'bread', 'breakfast', 'couple', 'cultural assets', 'drink', 'field experience', 'game', \
#                          'history', 'noodle', 'palace', 'play', 'ramen', 'snackfood', 'spicy', 'sushi', 'virtual reality', 'vr']:
#     print("good")
# else : print("again")