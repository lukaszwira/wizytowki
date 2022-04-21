from faker import Faker
fake = Faker("pl-PL")

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email   

    def contact(self):
        return f'Wybieram numer: {self.phone} i dzwonię do: {self.name} {self.surname}'
    @property
    def label_length(self):
        return f'ilość liter imienia i nazwiska: {len(self.name)} i {len(self.surname)}'

class BusinessContact(BaseContact):
    def __init__(self, company, occupation, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.occupation = occupation
        self.business_phone = business_phone
    def contact(self):
        return f'Wybieram numer służbowy: {self.business_phone} i dzwonię do: {self.name} {self.surname}'
    

def create_contacts(card_type, quantity):
    card_list = []
    while quantity: 
        quantity = quantity - 1

        if card_type == "base":
            card_list.append(BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email()))
        elif card_type == "business":
            card_list.append(BusinessContact(fake.company(), fake.job(), fake.phone_number(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.email()))

    return card_list

contacts = create_contacts("business", 5)

for contact in contacts:
    print(contact.contact())
