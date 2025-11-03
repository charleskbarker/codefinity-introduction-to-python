seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

#Define Overstock
overstock_risk = seasonal == True and current_stock > high_stock_threshold

#Define Discount
discount_eligible = not selling_well and not on_sale

make_discount = overstock_risk or discount_eligible

#Output
print("Should the item be discounted?", make_discount)