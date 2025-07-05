#Create a shopping cart programme that will continuousely ask the user for food product and the price of that product.
#Have an exit clause if the user wishes to stop adding more things to their cart
#At the end show the food items and their total cost to the user

Food=[]
Price=[]
Total=0


while True:
    food=input("Enter item to cart or press q to quit: ")
    if food == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        Food.append(food)
        Price.append(price)



print("-------YOUR FINAL ITEMS IN YOUR CART--------")

for food in Food:
    print(food, end= " ")
    
for price in Price:
    Total += price
    
print("\n")
print(f"Your total is : R{Total}")
