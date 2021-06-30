

def demo_function():
print("I`m inside function")

a=1
def scope_demo():
    a=2
    print(a)
scope_demo()
print(a)

def shopping():
    shopping_items=[
        'jajka',
        'bułka',
        'chleb',
        'chałka'
    ]
    shopping_cart = 'Koszyk zawiera:'
    for i in shopping_items:
        shopping_cart+=i + '\n'
    return (shopping_cart)
print(shopping())
