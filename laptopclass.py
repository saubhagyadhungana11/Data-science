# Write a Python program to create a class Laptop with the properties id, name, and ram. Then,
# # create three objects of this class and print all their details

class laptop:
    def __init__(self,id,name,ram):
        self.id = id
        self.name = name
        self.ram = ram 
        
    def details(self):
        return self.id, self.name, self.ram
    
d1 = laptop(101,"Acer nitro",16)
print(d1.details())




