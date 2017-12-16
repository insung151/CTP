# Created by inseong on 2017-10-28

def make_named_loc(lati, long, name, keywords):
    result = {}
    result['latitude'] = lati
    result['longitude'] = long
    result['name'] = name
    result['keywords'] = keywords
    return result

# print(make_named_loc(90.0, 0.0, "북극", ["빙하", "북극곰"]))