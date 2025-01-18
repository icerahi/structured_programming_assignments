#Task 6: Password Validator

def check_upper(text):
    for char in text:
        if char.isupper():
            return True
    return False

def check_lower(text):
    for char in text:
        if char.islower():
            return True 
    return False
                
def check_digit(text):
    for char in text:
        if char.isdigit():
            return True 
    return False

def password_validator(password):
    if(len(password)>=8) and check_upper(password) and check_lower(password) and check_digit(password):
        print("Password is valid.")
    else:
        print("Your password in invalid!")
            
password_validator(input("Enter your password: "))
       