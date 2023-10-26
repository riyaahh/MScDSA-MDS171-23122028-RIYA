import petstore

obj=petstore.pets()
while True:
    print("1.add new pet")
    print("2.search pet")
    print("3.sell pets")
    print("4.list pets")
    print("5.exit")

    choice=input("enter your choice")
    if choice=="1":
        obj.storeNewpets()
    if choice=="2":
        obj.searchPets()
    if choice=="3":
        obj.sellPets()
    if choice=="4":
        obj.listPets()
    if choice=="5":
        exit
     

    
