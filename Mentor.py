# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfileTest.log")
# import operator
# operators = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
# }

# operator.add(a, b)
# operator.floordiv(a, b)
# operator.mul(a, b)
# operator.sub(a, b)
def add (x,y,z):
    return x+y+z
def substraction (x,y):
    return (x-y)
def multiply (x,y):
    return (x*y)
def divide (x,y):
    return (x/y)
while True:
    decision = input('Podaj działanie, posługując się odpowiednią liczbą: \n 1 - Dodawanie \n 2 - Odejmowanie \n 3 - Mnożenie \n 4 - Dzielenie \n Twój wybór: ')
    if decision in ('1', '2', '3', '4'):
        nr_1 = float(input('podaj pierwszy składnik: '))
        nr_2 = float(input('podaj drugi składnik: '))
        nr_3 = float(input('podaj trzeci składnik: '))
        if decision =='1':
            print(nr_1, '+', nr_2, '+', nr_3, '=', add(nr_1, nr_2, nr_3))
            # suma = add(nr_1, nr_2)
            # logging.info('Rezultatem dodawania jest %s' % (suma))
        elif decision =='2':
            print(nr_1, '-', nr_2,'=', substraction(nr_1,nr_2))
        elif decision =='3':
            print(nr_1, '*', nr_2,'=', multiply(nr_1,nr_2))  
        elif decision =='4':
            # print(nr_1, '/', nr_2,'=', divide(nr_1,nr_2))
            if nr_2 == 0:
                print('ERROR (ze szkolnej ławy pamiętaj cholero nie dziel przez zero :)!)')
            else:
                print(nr_1, '/', nr_2,'=', divide(nr_1,nr_2))
        break
    else:
        print('Invalid decision')
    exit()