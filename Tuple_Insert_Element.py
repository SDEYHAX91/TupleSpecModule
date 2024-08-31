print("FUNCTION/PROGRAM TO INSERT AN ELEMENT IN A TUPLE")

def insert_tuple_el(tup):
    el = int(input("Enter element to be inserted: "))
    x = int(input("Enter position: "))
    pos = x - 1
    
    if pos < 0 or pos >= len(tup):
        print("Invalid position.")
    else:
        tup = tup[:pos] + (el,) + tup[pos:]

    print("Updated Tuple = ",tup)
    
n = int(input("Enter size = "))
lst = [int(input(f"Enter element {x+1}: ")) for x in range(n)]
tup = tuple(lst)
print("Original tuple = ",tup)

insert_tuple_el(tup)

