import random


menucard1= [
    ['pizza',50],
    ['burger',70],
    ['cake',45],
    ['chocolate',90]
]


print(menucard1)

def order_id():
    order_id = ''.join([str(random.randint(0, 9)) for _ in range(5)])           
    return int(order_id)

#accept order
orderlist = []
def acceptOrder():
    item = input("Enter the item: ")
    quantity = input("Enter the quantity: ")
    order = {
    
        "item": item,
        "quantity": quantity
    }
    orderlist.append(order)


print(orderlist)

def priceOrder():
    
    print("total price of this order =",(quantity*price))

    


def viewOrder():
    for i in orderlist:{
        "orderid":order_id,
        "items":[
            {
                "itemnumber":

                "quantity":
            }
        ]
    } 
    print(orderlist)

print("enter your choice")
print("1.place order")
print("2.view order")
print("exit")

choice=input("enter the choice")
if choice=='1':
    acceptOrder()
if choice=='2':
    viewOrder()
else:
    exit()
   
