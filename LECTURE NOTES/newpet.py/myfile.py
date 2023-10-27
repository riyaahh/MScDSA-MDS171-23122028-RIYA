class animals:
    def __init__(self):
        self.dict=[
            {
                "name":"cat",
                "colour":"white"
                "status":"unsold"
            },
            {
                "name":"dog",
                "colour":"black"
                "status":"unsold"
            }
        ]
#     def printL(self):
#         print(self.dict)
# object=animals()
# object.printL()

    def newStore(self):
        n=int(input("enter the number of animals"))
        for i in range(n):
            name=input("enter the name")
            colour=input("enter the colour")
            save={"name":name,"colour":colour}
            self.dict.append(save)
            print(self.dict)
    
    def searchIt(self):
        take=input("enter the animal to be searched")
        for i in self.dict:
            if take.strip().lower() in i.values():
                print(i.values())
                break
            else:
                print("invalid")

    def sellPets(self):
        sell=input("enter the name to be searched")
        for pets in self.dict:
            if sell in pets.values():
                pets["status"]:"sold"
                print(self.dict)
           
    
object=animals()
object.sellPets()

