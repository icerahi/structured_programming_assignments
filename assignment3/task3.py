#Task 3: Multiples of a Number

def multiple_of_a_number(number,times):
     for i in range(1,times+1):
        print(number*i,end=" ")
        


multiple_of_a_number(int(input("Enter a number:")),int(input("Enter how many multiples:")))