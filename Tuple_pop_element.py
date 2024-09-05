def t_pop(tup,index): #removes tuple element from specified index and returns updated tuple
    if index < 0 or index >= len(tup):
        raise IndexError
    else:
        for i in range(len(tup)):
            if i == index:
                tup = tup[:i] + tup[i+1:]
                break
        return tup

tup = (1,3,5,7,9)
tup = t_pop(tup,3)
print(tup)
