foods = []
price = []
total = 0

while True:
    demand = str(input(f"Enter The Food You Need (enter q to quit) : "))
    if demand.lower() == 'q':
        break
    else:
        foods.append(demand)
        price_val = str(input("You Need ( L | M | S): "))
        if price_val == "L":
            price.append(100)
        elif price_val == "M":
            price.append(50)
        elif price_val == "S":
            price.append(20)
        else:
            print("Error")
        
print("\n","YOUR CART".center(40,"-"))
total = 0
for i , j in zip(foods,price):
    print(f"{i} =====> {j}$")
    total += j

print(f"Total price is {total}")