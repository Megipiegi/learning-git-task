# def say_hello():
#     greeting = "Hello stranger!"
#     return greeting

# def say_louder (func):
#     def wrapper ():
#         result = func()
#         return result.upper ()
#     return wrapper

# @say_louder
# def say_hello ():
#     greeting = 'Hello stranger!'
#     return greeting

# say_hello ()

# say_hello = say_louder (say_hello)
# say_hello()


# def funkcja_wielkie_litery (text):
#     return text.upper()
# def funkcja_male_litery (text):
#     return text.lower()
# def nowa_funkcja (func):
#     greeting = func('coś tam')
#     print(greeting)
#     nowa_funkcja(funkcja_wielkie_litery)
#     nowa_funkcja (funkcja_male_litery)    

# def create_adder (x):
#     def adder (y):
#         return (x+y)
#     return adder
# add_15=create_adder(15)
# print(add_15(10))


# import time
# import math

# def calculate_time (func):
#     def moja_funkcja (*args, **kwargs):
#         begin=time.time()
#         func(*args, **kwargs)
#         end=time.time()
#         print('Total time taken in: ', func.__name__, end - begin )
#     return moja_funkcja
# @calculate_time
# def factorial (num):
#     time.sleep(4)
#     print (math.factorial(num))
# factorial(10)




