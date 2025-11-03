# Create vegeteble list
vegetables = ["tomatoes", "potatoes", "onions"]

# Remove onions

vegetables.remove("onions")

# Add carrots & cucumbers if not already in the list

if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

vegetables.sort()

print("Updated Vegetable Inventory:", vegetables)