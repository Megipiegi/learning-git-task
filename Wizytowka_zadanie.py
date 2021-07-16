class Basecontact:
    def __init__ (self, name_1, surname, telephone, email):
        self.name_1=name_1
        self.surname=surname
        self.telephone=telephone
        self.email = email
    def __str__ (self):
        return f'{self.name_1} {self.surname} {self.telephone} {self.email}'
Basecontact_1 = Basecontact (name_1='Ola', surname='Fasola', telephone='+48602222222', email='ola@ola.pl')
Basecontact_2 = Basecontact (name_1='Ala', surname='Makota', telephone='+48602222223', email='ala@ala.pl')
Basecontact_3 = Basecontact (name_1='Iza', surname='Unia', telephone='+48602222224', email='iza@iza.pl')
All_Basecontact=[Basecontact_1, Basecontact_2, Basecontact_3]
print('Basecontacts:')
for i in All_Basecontact:
    print (i)
class BusinessContact(Basecontact):
    def __init__(self, position, company_name, business_phone,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position=position
        self.company_name=company_name
        self.business_phone=business_phone
    def __str__ (self):
        return f'{self.name_1} {self.surname} {self.telephone} {self.email} {self.position} {self.company_name} {self.business_phone}'
Businesscontact_1 = BusinessContact (name_1='Ola', surname='Fasola', telephone='+48602222222', email='ola@ola.pl', position = 'Manager', company_name = '"Manageme"', business_phone ='+48792888886' )
Businesscontact_2 = BusinessContact (name_1='Ala', surname='Makota', telephone='+48602222223', email='ala@ala.pl', position = 'Team Leader', company_name = '"Manageme"', business_phone ='+48792888887' )
Businesscontact_3 = BusinessContact (name_1='Iza', surname='Unia', telephone='+48602222224', email='iza@iza.pl', position = 'Secretary', company_name = '"Manageme"', business_phone ='+48792888888' )
All_Businesscontact = [Businesscontact_1, Businesscontact_2, Businesscontact_3]
print('Businesscontacts:')
for i in All_Businesscontact:
    print (i)
    def contact (telephone, name, surname):
        return (f'Wybieram numer {telephone} i dzwonię do: {name} {surname}')
print (contact)




# Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.


