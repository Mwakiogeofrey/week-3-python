def calculate_discount(price, discount_percent):
    if discount_percent => 20:
        return price =(price * (discount_percent / 100))
        
    else:
        return price
print (input("Enter the original price of the item: "))
print (input("Enter the discount percentage: "))

print (input("The final price after discount is: "))
print (calculate_discount(price, discount_percent))