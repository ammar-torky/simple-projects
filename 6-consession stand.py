foods = {
    "Pizza" : 5,
    "Popcorn" : 4,
    "Lemon" : 3,
    "Water" : 2,
    "Chipsy" :  5
    }

cart = []
total = 0

print("MENU".center(10 , "-"))

for key , value in foods.items():
    print(f"{key:7} : {value:>1}$")

print("-" * 10, "\n")

while True:
    demand = input("Enter What You Need (q to quit) : ").capitalize()
    if demand.lower() == "q":
        break
    elif foods.get(demand) is not None : 
        cart.append(demand)
        total 
print()      
if len(cart) != 0 :
    print("your demands is".center(20 , "-"))        
    for counter , food in enumerate(cart):
        print(f"{counter+1}- {food} costs {foods.get(food)}$")
        total += foods.get(food)
    print(f"total price is : {total}$")
else:
    print("your cart is empty")