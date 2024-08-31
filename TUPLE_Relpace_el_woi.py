print("FUNCTION/PROGRAM TO REPLACE AN ELEMENT IN A TUPLE WITHOUT INDEX")

def replace_tuple_el(tup,val):
    x = int(input("Enter element to be replaced: "))
    
    if x not in tup:
        print("Element intended to be replaced is not in tuple.")
    else:
        for j in range(len(tup)):
            if tup[j] == x:
                tup = tup[:j] + (val,) + tup[j+1:]
                break
    print("Updated tuple = ",tup)
    
n = int(input("Enter size: "))
lst = [int(input(f"Enter for element {i+1} = ")) for i in range(n)]
tup = tuple(lst)
print("Original tuple = ",tup)
val = int(input("Enter value to replace: "))

replace_tuple_el(tup,val)
