# HW1 Exercise 1

def make_timestamped_loc(latitude, longitude, timestamp):
    dic = {}
    dic['latitude'] = latitude
    dic['longitude'] = longitude
    dic['timestamp'] = timestamp
    return dic

# test example; should be erased before submitting.
# print(make_timestamped_loc(37.481236, 126.952733, 1483196400))