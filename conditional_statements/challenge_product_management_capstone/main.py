# Input variables
days_until_expiration = 7  # Example value
stock_level = 50  # Example value
product_type = "Non-Perishable"  # Can be "Perishable" or "Non-Perishable"

# Check if Parishable and assign discount based on how close to parish date
if product_type == "Perishable":
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    elif days_until_expiration >= 4 and days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    elif days_until_expiration > 6 and stock_level <= 50:
        print("10% discount applied")
    else:
        print("No discount.")
else:
    print("No discount available for non-perishable items.")
