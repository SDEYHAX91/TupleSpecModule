def uniq_tuple(tup): #Returns tuple with no duplicate elements
    tup1 = ()
    for i in tup:
        if i not in tup1:
            tup1 += (i,)
    return tup1

tup = (2,4,6,8,3,6,9,4,8)
print(uniq_tuple(tup))
