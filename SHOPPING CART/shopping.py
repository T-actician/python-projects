#==================SHOPPIG CART PROGRAM====================

foods = []
prices = []
total = 0
  
while True:
    food = input("\nEnter a food to buy (q to quit): ")  
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: Ksh"))
        foods.append(food)
        prices.append(price)
        total += price
    
print("\nShopping Cart:")
for x in range(len(foods)):
    print(f"{foods[x]}: Ksh{prices[x]:.2f}")
    
print(f"Total: Ksh{total:.2f}")

#==============DICTIONARY PROGRAM==================

menu = {
    "ugali_omena": 80,
    "ugali_matumbo": 100,
    "ugali_lambchops": 500,
    "ugali_kuku": 450,
    "rice_kuku": 400,
    "pizza": 500,
}

cart = []
total = 0

print("==============MENU==========")
for key, value in menu.items():
    print(f"{key:10}: Ksh{value: .2f}")
    
print("------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower().strip()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food) # value associated with food 
    print(food, end = " ")
    
print()      
print(f" Total is: Ksh {total:.2f}")