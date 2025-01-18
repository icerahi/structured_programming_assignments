#Task 5: Reverse a String

def reverse_string(string):
    result=""
    for i in string:
        result=i+result 
    print(result)
    
reverse_string(input("Enter a string:"))