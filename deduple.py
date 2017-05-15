def deduple(lst, func=None):
    res = set()
    for item in lst:
        val = item if func is None else func(item)
        if val not in res:
            yield item
            res.add(val)
    return res

lst = [1,5,2,1,9,1,5,10]
dl = list(deduple(lst))
print(dl)

lst = [{'x':1,'y':2}, {'x':1,'y':3}, {'x':1,'y':2}, {'x':2,'y':4}]
dl = list(deduple(lst, func=lambda item: (item['x'], item['y'])))
print(dl)

dl = list(deduple(lst, func=lambda item: (item['x'])))
print(dl)
