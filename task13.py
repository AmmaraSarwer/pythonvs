# Declaring variables with different data types
integer_var = 10  # Integer
float_var = 20.5  # Float
string_var = "Hello, Python!"  # String
boolean_var = True  # Boolean
complex_var = 3 + 4j  # Complex Number
list_var = [1, 2, 3, 4, 5]  # List
tuple_var = (10, 20, 30)  # Tuple
set_var = {1, 2, 3, 4, 5}  # Set
dict_var = {"name": "Alice", "age": 25}  # Dictionary
none_var = None  # NoneType

# Displaying variables with their data types
variables = [integer_var, float_var, string_var, boolean_var, complex_var, 
             list_var, tuple_var, set_var, dict_var, none_var]

for var in variables:
    print(f"Value: {var}, Type: {type(var)}")