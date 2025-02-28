# Define Boolean variables
is_raining = True
is_cold = False
has_umbrella = True

# Evaluate logical conditions
should_take_umbrella = is_raining and not has_umbrella
should_wear_jacket = is_cold or is_raining
can_go_outside = not (is_raining and not has_umbrella)

# Output the results
print("Logical Operators Demonstration:\n")
print(f"Is it raining? {is_raining}")
print(f"Is it cold? {is_cold}")
print(f"Do I have an umbrella? {has_umbrella}\n")

print(f"Should I take an umbrella? {should_take_umbrella}")
print(f"Should I wear a jacket? {should_wear_jacket}")
print(f"Can I go outside? {can_go_outside}")
