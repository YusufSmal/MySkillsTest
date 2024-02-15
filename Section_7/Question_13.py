def is_palindrome(s):
  s = s.lower()
  s = ''.join(char for char in s if char.isalnum())
  return s == s[::-1]

user_input = input("Enter a string please: ")

if is_palindrome(user_input):
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")
