def isPalindrome(text):
    text = text.lower()
    l = len(text)
    if l < 2:
        return True
    elif text[0] == text[l - 1]:
        return isPalindrome(text[1: l - 1])
    else:
        return False
text=input('enter your value: ')
print(text)
condition_ok = isPalindrome(text)
if condition_ok:
    print("Yes, it`s a palindrome") 
else:
    print("No, it`s not a palindrome")