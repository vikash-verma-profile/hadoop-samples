class SARDog(Dog):     
 def __init__(self, name):         
  """Initialize the sardog."""         
  super().__init__(name) 
 def search(self):         
  """Simulate searching."""         
  print(self.name + " is searching.") 


my_dog = SARDog('Willie') 
print(my_dog.name + " is a search dog.") 
my_dog.sit() 
my_dog.search() 