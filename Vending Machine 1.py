#vending machine
items_available = [{"item_id": 00,"item_name": "Crossiant",'item_price': 7,'item_stock': 10,},
{"item_id": 11,"item_name": "Donut",'item_price': 6,'item_stock': 10,},{"item_id": 12,"item_name": "Chocolate Cookies",'item_price': 7,'item_stock': 10,},
{"item_id": 13,"item_name": "Muffin",'item_price': 6,'item_stock': 10,},{"item_id": 14,"item_name": "Coffee",'item_price': 7,'item_stock': 10,},
{"item_id": 15,"item_name": "Hot chocolate",'item_price': 8,'item_stock': 10,},{"item_id": 16,"item_name": "Mocha",'item_price': 10,'item_stock': 10,},
{"item_id": 17,"item_name": "Latte",'item_price': 12,'item_stock': 10,},{"item_id": 18,"item_name": "Iced Coffee",'item_price': 9,'item_stock': 10,},
{"item_id": 19,"item_name": "Iced Mocha",'item_price': 12,'item_stock': 10,},
{"item_id": 20,"item_name": "Iced Latte",'item_price': 15,'item_stock': 10,},{"item_id": 11,"item_name": "Iced Tea",'item_price': 10,'item_stock': 10,},
]
items_purchased = []
print("Welcome to the Vending Macine")
for i in items_available:
    print(f"Item: {i['item_name']} --- Price: {i['item_price']} --- Item ID: {i['item_id']} --- Item Stock: {i['item_stock']}")

to_buy = int(input("Enter the item code you want to purchase:"))

if to_buy < len(items_available):
    items_purchased.append(items_available[to_buy])
    
else: 
    print("The Product code is Invalid")

more_items = input("Enter Yes to add more items, No to quit")
if more_items == 'Yes':
    print(to_buy)


sum = 0
for i in items_purchased:
    sum += i["item_price"]

money = int(input("Enter the money"))
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
    
