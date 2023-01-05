items_in_machine = [
    {
        "item_id": 0,
        "item_name": "Crossiant",
        'item_price': 7,
        'item_stock' : 10,
    },
    {
        "item_id": 1,
        "item_name": "Donut",
        'item_price': 6,
        'item_stock' : 10,
    },
    {
        "item_id": 2,
        "item_name": "Chocolate Cookies",
        'item_price': 7,
        'item_stock' : 10,
    },
    {
        "item_id": 3,
        "item_name": "Muffin",
        'item_price': 6,
        'item_stock' : 10,
    },
    {
        "item_id": 4,
        "item_name": "Coffee",
        'item_price': 7,
        'item_stock' : 10,
    },
    {
        "item_id": 5,
        "item_name": "Hot chocolate",
        'item_price': 8,
        'item_stock' : 10,
    },
    {
        "item_id": 6,
        "item_name": "Mocha",
        'item_price': 10,
        'item_stock' : 10,
    },
    {
        "item_id": 7,
        "item_name": "Latte",
        'item_price': 12,
        'item_stock' : 10,
    },
    {
        "item_id": 8,
        "item_name": "Iced Coffee",
        'item_price': 9,
        'item_stock' : 10,
    },
    {
        "item_id": 9,
        "item_name": "Iced Mocha",
        'item_price': 12,
        'item_stock' : 10,
    },
    {
        "item_id": 10,
        "item_name": "Iced Latte",
        'item_price': 15,
        'item_stock' : 10,
    },
    {
        "item_id": 11,
        "item_name": "Iced Tea",
        'item_price': 10,
        'item_stock' : 10,
    },
]


items_purchased = []

reciept = """
\t\tPRODUCT -- PRICE
"""

sum = 0

run = True

print("Welcome to the Vending Machine\n\n")


for i in items_in_machine:
    print(f"Item: {i['item_name']} --- Price: {i['item_price']} --- Item ID: {i['item_id']} --- Item Stock: {i['item_stock']}")


def machine(items_in_machine, run, items_purchased):
    while run:

        to_buy = int(input("\n\nEnter the item code of the product you want to buy: "))

        if to_buy < len(items_in_machine):
            items_purchased.append(items_in_machine[to_buy])
            
        else:
            print("THE PRODUCT ID IS WRONG!")
        
        
        

        add_items = str(input("press any key to add more items and press q to quit.. "))

        if add_items == "q":
            run = False
        
        

    to_get_receipt = int(input(("1. print the reciept? 2. only print the total sum .. ")))
    if to_get_receipt == 1:
        print(create_reciept(items_purchased, reciept))
    elif to_get_receipt == 2:
        print(sum(items_purchased))
    else:
        print("INVALID ENTRY")


def create_reciept(items_purchased, reciept):

    for i in items_purchased:
        reciept += f"""
        \t{i["item_name"]} -- {i['item_price']}
        """

    reciept += f"""
        \tTotal --- {sum(items_purchased)}
        
    
        
        """
   
    return reciept

def sum(items_purchased):
    sum = 0

    for i in items_purchased:
        sum += i["item_price"]

    return sum




if __name__ == "__main__":
    machine(items_in_machine, run, items_purchased)
   

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