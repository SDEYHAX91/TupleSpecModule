print("FUNCTION/PROGRAM TO REPLACE AN ELEMENT IN A TUPLE WITh INDEX")

def replace_tuple_el2(tup,val):
    i = int(input("Enter required index: "))
    if i < 0 or i >= len(tup):
        print("Index out of range.")
    else:
        tup = tup[:i] + (val,) +tup[i+1:]
    print("Updated tuple = ",tup)
    
n = int(input("Enter size: "))
lst = [int(input(f"Enter for element {i+1} = ")) for i in range(n)]
tup = tuple(lst)
print("Original tuple = ",tup)
val = int(input("Enter value to replace: "))

replace_tuple_el2(tup,val)
