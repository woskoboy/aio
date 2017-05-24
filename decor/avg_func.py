def averager():
    total = 0
    count = 0

    def avg(val):
        nonlocal total, count
        count += 1
        total += val
        return total / count

    return avg

avg = averager()
print(avg(10))
print(avg(11))
print(avg(12))

msg = [(avg.__code__.co_freevars[i],
        avg.__closure__[i].cell_contents)
       for i in range(len(avg.__closure__))]

print(msg)

