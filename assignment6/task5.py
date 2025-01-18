#Task 5: Pointer-based Linked List Operations
from collections import deque

def main():
    linked_list = deque()

     
    n = int(input("Enter number of elements: "))
    print("Enter the elements:")
    elements=list(map(int,input().split()))
    for element in elements:
        linked_list.append(element)   

    
    print("\nLinked List:")
    print(" -> ".join(map(str, linked_list)) + " -> None")

    
    key_to_delete = int(input("\nEnter the value to delete from the linked list: "))
    
    if key_to_delete in linked_list:
        linked_list.remove(key_to_delete)  
 
    print("\nLinked List:")
    print(" -> ".join(map(str, linked_list)) + " -> None")

main()
