#Task 7: Square and Cube of Numbers

def main(number):
    print("Number  Square  Cube")
    for i in range(1,number+1):
        print(f"{i:5}",end=" ")
        print(f"{i**2:5}",end=" ")
        print(f"{i**3:5}",end=" " )
        print()
        
main(int(input("Enter the number:")))