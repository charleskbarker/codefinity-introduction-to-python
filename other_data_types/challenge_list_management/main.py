# Generate Lists
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# Create Main list
deli_dept = [meat, cheese, condiment]

# Initial Output
print("Initial Deli List:", deli_dept)

# Restock

# if "Ham" in meat and meat[2] <100:
if meat[0] == "Ham" and meat[2] < 100:
    meat[2] = 100

# Add seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]

deli_dept.append(seasonal_meat)

# Remove condiment
deli_dept.remove(condiment)

# Sort list
deli_dept.sort()

# Final Output
print("Updated Deli List:", deli_dept)