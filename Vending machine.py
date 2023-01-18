items_available = [
    {
        "item_code": 0,
        "item_name": "Crossiant",
        'item_price': 7,
        'item_stock': 10,
    },
    {
        "item_code": 1,
        "item_name": "Donut",
        'item_price': 6,
        'item_stock': 10,
    },
    {
        "item_code": 2,
        "item_name": "Chocolate Cookies",
        'item_price': 7,
        'item_stock': 10,
    },
    {
        "item_code": 3,
        "item_name": "Muffin",
        'item_price': 6,
        'item_stock': 10,
    },
    {
        "item_code": 4,
        "item_name": "Coffee",
        'item_price': 7,
        'item_stock': 10,
    },
    {
        "item_code": 5,
        "item_name": "Hot chocolate",
        'item_price': 8,
        'item_stock': 10,
    },
    {
        "item_code": 6,
        "item_name": "Mocha",
        'item_price': 10,
        'item_stock': 10,
    },
    {
        "item_code": 7,
        "item_name": "Latte",
        'item_price': 12,
        'item_stock': 10,
    },
    {
        "item_code": 8,
        "item_name": "Iced Coffee",
        'item_price': 9,
        'item_stock': 10,
    },
    {
        "item_code": 9,
        "item_name": "Iced Mocha",
        'item_price': 12,
        'item_stock': 10,
    },
    {
        "item_code": 10,
        "item_name": "Iced Latte",
        'item_price': 15,
        'item_stock': 10,
    },
    {
        "item_code": 11,
        "item_name": "Iced Tea",
        'item_price': 10,
        'item_stock': 10,
    },
]

items_purchased = []
sum = 0
run = True
print("Welcome to the Vending Machine\n\n")


for i in items_available:
    print(f"Item: {i['item_name']} --- Price: {i['item_price']} --- Item Code: {i['item_code']} --- Item Stock: {i['item_stock']}")





while run:

    select = int(input("Enter the item code of the product you want to buy: "))

    if select < len(items_available):
            items_purchased.append(items_available[select])
            
    else:
        print("THE PRODUCT ID IS WRONG!")
        
    
    
    
    add_in_cart = str(input("Enter Y to add more items or N to quit"))
    if add_in_cart == "N":
            run = False


   
   
   

for i in items_purchased:
    print(i["item_name"],"",i['item_price'])

 


money = int(input("Enter your money"))
Total = 0



for i in items_purchased:
    Total += i["item_price"]
    
if Total == int(money):
    for i in items_purchased:
        print(f"Your {i['item_name']} has been dispensed, Please collect it")
            
elif Total < int(money):
    Balance1 = money - Total
    print("Here is your balance" , Balance1, "DHS")
    for i in items_purchased:
        print(f"Your {i['item_name']} has been dispensed, Please collect it")
            
elif Total > int(money):
    Balance2 = Total - money
    print("Enter" , Balance2, "DHS", "more")
    money = int(input("Enter the money"))
    if Balance2 == int(money):
            for i in items_purchased:
                print(f"Your {i['item_name']} has been dispensed, Please collect it")
                
    elif Balance2 < int(money):
        Balance3 = money - Balance2
        print("Here is your balance,", Balance3, "DHS")
        
    
else:
    print("Enter the money")
    money = int(input("Enter the money"))

print("Thank you for buying, Please visit again")