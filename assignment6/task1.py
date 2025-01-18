#Task 1: Dynamic String Manipulation

def dynamic_string_manipulation():
    string = input("Enter the initial string: ")
    to_append = input("Enter the string to append: ")
    string += to_append
    print(f"Modified string: {string}")
    print(f"Length of the string: {len(string)}")
    string = string.upper()
    print(f"Uppercase string: {string}")
  
dynamic_string_manipulation()
