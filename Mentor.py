# # # def fahr_to_celcius(temp):
# # #     return (((temp-32)*5/9))
# # # print('freezing point of water', fahr_to_celcius(32), 'c')
# # # print('boiling point of water', fahr_to_celcius(212), 'c')

# # # Stwórz funkcję, w której dodasz dwie liczby i wyświetl to na ekranie. 
# # # Jak ją nazwiesz? Funkcję stworzysz z użyciem def. W ciele umieść operację i funkcję print.

# # def sum_of_nr(x,y):
# #     return (x+y)
# # print ('wynik to:', sum_of_nr(45,5))

# # a = 1

# # def scope_demo():
# #     a = 2
# #     print(a)

# # scope_demo()
# # print(a)

# # def shopping():
# #     shopping_items = [
# #         "jajka",
# #         "bułka",
# #         "ser feta",
# #         "masło",
# #         "pomidor"
# #     ]
# #     shopping_cart = "Koszyk zawiera: "
# #     for item in shopping_items:
# #         shopping_cart += item + '\n'
# #     return shopping_cart

# # print(shopping())

# def day_times():
#     return 'morning', 'afternoon', 'evening','night'
# # times=day_times()
# # print(times)
# # print(type(times))
# first, second, third, fourth = day_times()
# print('trzeci element to %s:' %third) 

# def customized_hello(first_name, last_name, new_name):
#     print('Hello Mr %s %s %s' % (first_name, last_name, new_name))
# customized_hello ('John', 'nOWAK', 'kowalski')

# def customized_hello(first_name, last_name):
#     print("Hello Mr %s %s" % (first_name, last_name))

# customized_hello("Jan", "NOWAK")

# def customized_hello(first_name, last_name, gender_prefix='Mr'):
#     print(f"Hello {gender_prefix} {first_name} {last_name}!")

# customized_hello("Clara", "Cleese")


# shopping_items=[
# 'pomidor',
# 'ogórek',
# 'sałata',
# 'buraki',
# 'cebula',
# 'brukiew'

# ]
# def shopping(items):
#     shopping_cart='Koszyk zawiera:'
#     for i in items:
#         shopping_cart += i +'\n'
#     return shopping_cart
# basket = shopping(shopping_items)
# print(basket)

# shopping_items=[
# 'pomidor',
# 'ogórek',
# 'sałata',
# 'buraki',
# 'cebula',
# 'brukiew'

# ]


# def shopping(payment='card', shop='local'):
#     print(f"Płatność: {payment}, miejsce: {shop}")

# shopping()

# def count_them_all (*args):
#     positional_args= len (args)
#     print (f'I have {positional_args} positional arguments')
# count_them_all(1,2,3,4,5)

# def count_them(*args, **kwargs):
#     named_args_count = len(kwargs)
#     positional_args= len (args)
#     print(f"I have received {named_args_count} named arguments")
#     print (f'I have {positional_args} positional arguments')

# count_them(1, 2, "A", a=4,b=5)


# shopping_items=[
#     ('ziemniak', 2.5, 0.51),
#     ('cebula', 3, 1.60),
#     ('ser', 0.8, 15.50)
# ]
# sorted_items = sorted(shopping_items, key=lambda given_tuple: given_tuple[1])
# print(sorted_items)
# def get_index_1(given_tuple):
#     return given_tuple[1]
# sorted_items = sorted(shopping_items, key=get_index_1)
# print(sorted_items)

# string= input ('enter a string:''):
# for i in string:
#     print (i)
# if (string ==string[::-1]):
#     print ('palindrome')
# else:
#     print('not a palindrome')

# string=input(("Enter a string:"))
# for char in string:
#       print(char)
# if(string==string[::-1]):
#       print("The string is a palindrome")
# else:
#       print("Not a palindrome")

def checker(string):
  collection=list(string)
  length = len(collection)
  isPalindrom = True
  for i in range(length):
     if collection[i] != collection[length-i-1]:
         isPalindrom = False
         break;

     if isPalindrom :
         print('String is Palindrome')
     else:
         print('String is not Palindrome')
    
name=input("Enter a string: ") 
checker(name)



