class Wizytowka:
    def __init__ (self, name_1, surname, telephone, email):
        self.name_1=name_1
        self.surname=surname
        self.telephone=telephone
        self.email = email
wizytowka_1 = Wizytowka (name_1='Ola', surname='Fasola', telephone='+48602222222', email='ola@ola.pl')
wizytowka_2 = Wizytowka (name_1='Ala', surname='Makota', telephone='+48602222223', email='ala@ala.pl')
wizytowka_3 = Wizytowka (name_1='Iza', surname='Unia', telephone='+48602222224', email='iza@iza.pl')
all_wizytowki = [wizytowka_1, wizytowka_2, wizytowka_3]
# for i in all_wizytowki:
#     print( i.name_1, i.surname, i.email)

by_name_1=sorted(all_wizytowki, key=lambda Wizytowka: Wizytowka.name_1)
for i in by_name_1:
    print(i.name_1, i.surname, i.telephone, i.email)
by_surname=sorted(all_wizytowki, key=lambda Wizytowka: Wizytowka.surname)
for i in by_surname:
    print(i.surname, i.name_1, i.telephone, i.email)

