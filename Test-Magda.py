question=input('podaj swoje imię: ')
print('Witaj', question)

print ('Witaj, ten program pomoże Ci sprawdzić, czy jesteś pełnolteni/a')
adult = None
sex = input ('Podaj proszę swoją płeć [M/K]: ')
if sex == 'M':
    age=int(input('Twój wiek?'))
    adult = age>=18
elif sex == 'K':
    print ('Kobiet się o wiek nie pyta, więc zrobię to delikatnie:')
    over18yes_no= input('Czy miałaś już 18-tkę? [T/N]?')
    adult=(over18yes_no == 'T')
else:
    print('nie ma takiej płci!')
    exit (1)
print ('już wiem, Twoja pełnoletność w boolean to %s ' %str (adult))


