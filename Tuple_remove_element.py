def t_remove(tup, element):  # Removes the first occurrence of the element in the tuple and returns the updated tuple
    if element not in tup:
        raise ValueError(f"{element} not found in tuple")

    for i in range(len(tup)):
        if tup[i] == element:
            tup = tup[:i] + tup[i+1:]
            break
    return tup

tup = (3, 6, 9, 12, 15, 18)
tp = t_remove(tup, 89)
print(tp)
