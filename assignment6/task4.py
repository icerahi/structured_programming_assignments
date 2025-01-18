#Task 4: Dynamic Array Resizing
 
def dynamic_array_resizing():
    initial_size = int(input("Enter the initial size of the array: "))
    array = []
    print(f"Enter {initial_size} elements for the array:")
    
    elements = list(map(int,input().split()))
    for element in elements:
        array.append(element)

    print("\nOriginal Array:")
    print(array)

    new_size = int(input("\nEnter the new size of the array: "))
    if new_size < initial_size:
        array = array[:new_size]  
    else:
        additional_elements = new_size - initial_size
        print(f"Enter {additional_elements} elements to fill the new size:")
        additional_elements = list(map(int,input().split()))

        for element in additional_elements:
 
            array.append(element)

 
    print("\nResized Array:")
    print(array)

dynamic_array_resizing()
