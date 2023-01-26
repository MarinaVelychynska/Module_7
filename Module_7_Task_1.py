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

card = Card(name = faker.name(), email = faker.email(), phone_number = faker.phone_number())
card = []

def create_contact(quantity:int):
 for i in range(quantity):

   card.append(Card(name = faker.name(), email = faker.email(), phone_number = faker.phone_number()))

 for i in range(quantity):
  if quantity > 0:
    print (str(card[i]))

if __name__ == "__main__": 
 quantity = int(input("Введіть кількість контактів: "))

 create_contact(quantity)
    