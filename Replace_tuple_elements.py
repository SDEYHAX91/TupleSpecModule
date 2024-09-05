def t_replace(tup, index, element):  # Replaces tuple element at specified index with specified element and returns updated tuple
    if index < 0 or index >= len(tup):
        raise IndexError("Index out of range")
    
    # Replace the element at the specified index
    tup = tup[:index] + (element,) + tup[index+1:]
    
    return tup

tup = (3, 5, 9, 12, 15)
tup = t_replace(tup, 1, 6) 
