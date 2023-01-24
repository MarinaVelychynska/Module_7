class Card:
   def __init__(self, name, surname, mail):
       self.name = name
       self.surname = surname
       self.mail = mail
   
   def __str__(self):
    return f"{self.name} {self.surname} {self.mail}"

card_1 = Card(name="Ian", surname="Corcoran", mail="IanJCorcoran@rhyta.com")
card_2 = Card(name="Olga", surname="Cape", mail="OlgaRCape@rhyta.com")
card_3 = Card(name="Daniel", surname="Lazarus", mail="DanielMLazarus@jourrapide.com")
card_4 = Card(name="William", surname="Espinoza", mail="WilliamDEspinoza@armyspy.com")
card_5 = Card(name="Tanja", surname="Guthrie", mail="TanjaJGuthrie@teleworm.us")

cards_list = [card_1, card_2, card_3, card_4, card_5]
for i in cards_list:
     print(i)

class BaseContact(Card):
    def __init__(self, phone_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.phone_number = phone_number
    
    def __str__(self):
     return f"{self.name} {self.surname} {self.mail} {self.phone_number}"
       
    @property
    def name_length(self):
        length = self.name+self.surname
        return len(length)


card_x = BaseContact(name="Ian", surname="Corcoran", mail="IanJCorcoran@rhyta.com", phone_number="+48656788221")

print(card_x)

class BusinessContact(Card):
    def __init__(self, job, company, company_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.job = job
        self.company = company
        self.company_number = company_number

    def __str__(self):
     return f"{self.name} {self.surname} {self.mail} {self.job} {self.company} {self.company_number}"
    
    @property
    def name_length(self):
        length = self.name+self.surname
        return len(length)

card_y = BusinessContact(name="Ian", surname="Corcoran", mail="IanJCorcoran@rhyta.com", job="Construction manager", company="Jay Jacobs", company_number="+48905376899")

print(card_y)

def contact(action):
    if action == "1": 
          print(f"Я набираю {card_x.phone_number} та зв'язуюсь з {card_x.name}, що має довжину імені та фаміліі {card_x.name_length} літер. ")

    elif action == "2":
       print(f"Я набираю {card_y.company_number} та зв'язуюсь з {card_y.name}, що має довжину імені та фаміліі {card_y.name_length} літер. ")

if __name__ == "__main__":
   action = input("Обрати тип контакту, з яким потрібен зв'язок:\n1. Особистий номер\n2. Робочий номер\n")

contact(action)