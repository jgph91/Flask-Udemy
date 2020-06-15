class Dog():

    #Always true
    species='mammal'
    #Class object attributes
    def __init__(self,input_breed,name):
        self.breed = input_breed
        self.name = name
    

x = Dog('labrador','Jose')
new_dog = Dog('Golden','Cindy')
print(x.name)
print(x.breed)
print(x.species)
print(new_dog.name)