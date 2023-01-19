product_available = [
    {
        "product_code": 0,
        "product_name": "Crossiant",
        'product_price': 7,
        'product_stock': 10,
    },
    {
        "product_code": 1,
        "product_name": "Donut",
        'product_price': 6,
        'product_stock': 10,
    },
    {
        "product_code": 2,
        "product_name": "Chocolate Cookies",
        'product_price': 7,
        'product_stock': 10,
    },
    {
        "product_code": 3,
        "product_name": "Muffin",
        'product_price': 6,
        'product_stock': 10,
    },
    {
        "product_code": 4,
        "product_name": "Coffee",
        'product_price': 7,
        'product_stock': 10,
    },
    {
        "product_code": 5,
        "product_name": "Hot chocolate",
        'product_price': 8,
        'product_stock': 10,
    },
    {
        "product_code": 6,
        "product_name": "Mocha",
        'product_price': 10,
        'product_stock': 10,
    },
    {
        "product_code": 7,
        "product_name": "Latte",
        'product_price': 12,
        'product_stock': 10,
    },
    {
        "product_code": 8,
        "product_name": "Iced Coffee",
        'product_price': 9,
        'product_stock': 10,
    },
    {
        "product_code": 9,
        "product_name": "Iced Mocha",
        'product_price': 12,
        'product_stock': 10,
    },
    {
        "product_code": 10,
        "product_name": "Iced Latte",
        'product_price': 15,
        'product_stock': 10,
    },
    {
        "product_code": 11,
        "product_name": "Iced Tea",
        'product_price': 10,
        'product_stock': 10,
    },
]

product_purchased = []

run = True
print("Welcome to the Vending Machine\n\n")


for i in product_available:
    print(f"Name: {i['product_name']} --- Price: {i['product_price']} --- Code: {i['product_code']} --- Stock: {i['product_stock']}")





while run:

    select = int(input("Enter the product code you want to buy: "))

    if select < len(product_available):
            product_purchased.append(product_available[select])
            
    else:
        print("Error Code, Try again")
        
        
    
    
    
    add_in_cart = str(input("Enter Y to add more items or N to quit: "))
    if add_in_cart == "N":
            run = False


   
   
   
print("Product name", "---", "Product price")
for i in product_purchased:
    
    print(i["product_name"],"---",i['product_price'])

 


money = int(input("Enter your money: "))
Total = 0

for i in product_purchased:
    Total += i["product_price"]
    
if Total == int(money):
    for i in product_purchased:
        print(f"Your {i['product_name']} has been dispensed, Please collect it")
            
elif Total < int(money):
    Balance1 = money - Total
    print("Here is your balance" , Balance1, "DHS")
    for i in product_purchased:
        print(f"Your {i['product_name']} has been dispensed, Please collect it")
            
elif Total > int(money):
    Balance2 = Total - money
    print("Enter" , Balance2, "DHS", "more")
    money = int(input("Enter the money"))
    if Balance2 == int(money):
            for i in product_purchased:
                print(f"Your {i['product_name']} has been dispensed, Please collect it")
                
    elif Balance2 < int(money):
        Balance3 = money - Balance2
        print("Here is your balance,", Balance3, "DHS")
        
    
else:
    print("Enter the money")
    money = int(input("Enter the money"))

print("Thank you for buying, Please visit again")