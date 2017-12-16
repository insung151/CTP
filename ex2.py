# HW1 Exercise 2

def sort_locs(lst):
    lst = sorted(lst, key = lambda x : x.get('timestamp'))
    return lst

# test example; should be erased before submitting.
loc1 = {'latitude':1.2, 'longitude':3.4, 'timestamp':100}
loc2 = {'latitude':5.6, 'longitude':7.8, 'timestamp':300}
loc3 = {'latitude':9.1, 'longitude':2.3, 'timestamp':200}
print(sort_locs([loc1, loc2, loc3]))

