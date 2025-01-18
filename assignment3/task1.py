#Task 1: Multiplication Table Generator

def main():
    print("   ",end="")
    for i in range(1,11):
        print(f"{i:3}",end=" ")
    print()
    for i in range(1,11):
        print(f"{i:2}",end=" ")
        for j in range(1,11):
            print(f"{i*j:3}",end=" ")
        print()
    
if __name__ == "__main__":
    main()
    
