#  Initialize two variables
a = 5
b = 10

#  Print before swapping
print("Before Swapping:")
print(f"a = {a}, b = {b}")

# swapping variable using type casting
a = str(a)  
b = str(b)
a, b = int(b) , int(a)

#  Printing after swapping
print("After Swapping")
print(f"a = {a}, b = {b}")
