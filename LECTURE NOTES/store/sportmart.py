class sportMart:
    def __init__(self):
        self.inventory={}
        self.orders={}
    def createInventory(self,Sno,Item,price,quantity):
        dict={
            "Sno":Sno,
            "item":Item,
            "price":price,
            "quantity":quantity
            
        }
        self.inventory['Sno']=dict

    def createOrderid(self,orderid,item,quantity):
        temp={
            "orderid":orderid,
            "item":item,
            "quantity":quantity
        }
        self.orders['orderid']=temp
        
    def printOrders(self):
        print(self.orders)
    def printInventory(self):
        print(self.inventory)

trinity=sportMart()
filename = "store\inventory.csv"
inventory=open(filename,"r")
inventory_header=inventory.readlines()
inventory_inventory=inventory.readlines()
for data in inventory_inventory:
            temp=data.strip().split(",")
            trinity.createInventory(temp[0],temp[1],temp[2],temp[3])

trinity.printOrders()

trinity = sportMart()
filename = "store\orders.csv" 
orders = open(filename , 'r')
orders_header = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(',')
    trinity.createOrderid(temp[0],temp[1],temp[2])
trinity.printInventory()

#

# def updateValues(self):

#         o=int(input("enter the orderid: "))
#         s=int(input("enter the sno"))
#         k=self.dict[s](['quantity'])-self.temp[o]['quantity']
#         self.inventory['Sno']['quantity']=k
#         print(self.inventory)
# updateValues()
        # trinity.printInventory()

# filename1 = "store\inventory.csv" 
# with open(filename1,"r") as csvfile:
#             file2=csvfile.readlines()
#             for data in file:
#                 temp=data.strip().split(",")
# trinity.createOrderid(temp[0],temp[1],temp[2])
# trinity.printOrders()
        
        
        
        
        
        
    # trinity.createInventory()
    # trinity.createOrderid()
    # trinity.printOrders()
    # trinity.printInventory()