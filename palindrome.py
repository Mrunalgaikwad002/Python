def is_palindrome(string):
    string = string.lower().replace("", "")
    return string == string[::-1]


text = input("enter a string: ")
if is_palindrome(text):
    print("it is a palindrome")
else:
    print("it is not palindrome")




