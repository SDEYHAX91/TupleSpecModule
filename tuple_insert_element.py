def t_insert(tup,index,element): #Insert specified element at specified index in a tuple and returns updated tuple
    if index < 0 or index > len(tup):
        raise IndexError
    else:
        for i in range(len(tup)):
            if index == i:
                tup = tup[:i] + (element,) +tup[i:]
                break
    return tup

tup = (2,13,24,35,46,57)
t = t_insert(tup,5,20)
print(t)
