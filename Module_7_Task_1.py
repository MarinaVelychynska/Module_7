class Card:
   def __init__(self, name, email, phone_number):
       self.name = name
       self.email = email
       self.phone_number = phone_number

   def __str__(self):
    return f"{self.name} {self.email} {self.phone_number}"

   def __repr__(self):
    return f"{self.name} {self.email} {self.phone_number}"

   @property
   def name_length(self):
    return len(self.name)

class BaseContact(Card):
    def __init__(self, name, email, phone_number):
       self.name = name
       self.email = email
       self.phone_number = phone_number
    
    def contact(self):
        print(f"Я телефоную по номеру {self.phone_number} та звязуюсь з {self.name}")

class BusinessContact(Card):
     def __init__(self, name, email, phone_number, job, company):
       self.name = name
       self.email = email
       self.phone_number = phone_number
       self.job = job
       self.company = company
       
     def __str__(self):
      return f"{self.name} {self.email} {self.phone_number} {self.job} {self.company}"

     def __repr__(self):
      return f"{self.name} {self.email} {self.phone_number} {self.job} {self.company}"

     def contact(self):
        print(f"Я телефоную по номеру {self.phone_number} та звязуюсь з {self.name}") 

from faker import Faker
faker = Faker()

def create_contact(quantity:int,type:str):

 type = input("Оберіть тип візитки:\n1. Особиста\n2. Робоча\n")
 
 cards = []
 
 for i in range(quantity):
    if type == "1": 
       object = (BaseContact(faker.name(), faker.email(), faker.phone_number()))
    
    elif type == "2":
      object = (BusinessContact(faker.name(), faker.email(), faker.job(), faker.company(), faker.phone_number()))

 cards.append(object)

if __name__ == "__main__": 
 quantity = int(input("Введіть кількість контактів: "))

 create_contact(quantity,type)
 print(create_contact)

 