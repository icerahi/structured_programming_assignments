#4. Password Strength Checker

import string
def has_uppercase(password):
   return any(char.isupper() for char in password)
def has_lowercase(password):
   return any(char.islower() for char in password)
def has_digit(password):
   return any(char.isdigit() for char in password)
def has_special_character(password):
   special_characters = string.punctuation   
   return any(char in special_characters for char in password)
def password_strength_checker(password):
   criteria = {
       "uppercase": has_uppercase(password),
       "lowercase": has_lowercase(password),
       "digit": has_digit(password),
       "special_character": has_special_character(password),
       "length": len(password) >= 8,  
   }
   if all(criteria.values()):
       print("Password strength: Strong")
   else:
       print("Password strength: Weak")
       print("Suggestions to improve your password:")
       if not criteria["uppercase"]:
           print("- Add at least one uppercase letter.")
       if not criteria["lowercase"]:
           print("- Add at least one lowercase letter.")
       if not criteria["digit"]:
           print("- Add at least one digit.")
       if not criteria["special_character"]:
           print("- Add at least one special character (e.g., !@#$%^&*).")
       if not criteria["length"]:
           print("- Ensure the password is at least 8 characters long.")

password = input("Enter your password: ")
password_strength_checker(password)
