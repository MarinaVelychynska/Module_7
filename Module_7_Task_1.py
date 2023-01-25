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

card = BaseContact(name = faker.name(), email = faker.email(), phone_number = faker.phone_number())

card_2 = BusinessContact(name = faker.name(), email = faker.email(), job = faker.job(), company = faker.company(), phone_number = faker.phone_number())

card = []
card_2 = []

def create_contact(quantity:int,type):
 for i in range(quantity):

   card.append(BaseContact(name = faker.name(), email = faker.email(), phone_number = faker.phone_number()))

   card_2.append(BusinessContact(name = faker.name(), email = faker.email(), job = faker.job(), company = faker.company(), phone_number = faker.phone_number()))
 
 if type == "1": 
  for i in range(quantity):
   if quantity > 0:
    print (str(card[i]))

 elif type =="2":
  for i in range(quantity):
   if quantity > 0:
    print (str(card_2[i]))

if __name__ == "__main__": 
 type = input("Оберіть тип візитки:\n1. Особиста\n2. Робоча\n")
 quantity = int(input("Введіть кількість контактів: "))

 create_contact(quantity,type)