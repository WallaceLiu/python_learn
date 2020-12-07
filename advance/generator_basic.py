def dec():
    n = 0
    for i in range(10):
        yield n
        n += i


for i in dec():
    print(i)
