#Task 2: Dynamic Array of Pointers

def dynamic_array_of_pointers():
    num_arrays = int(input("Enter the number of arrays: "))
    arrays = []  
    for i in range(num_arrays):
        size = int(input(f"Enter the size of array {i+1}: "))
        print(f"Enter {size} elements for array {i+1}:")
        array = list(map(int, input().split()))
        arrays.append(array)      
    for i, array in enumerate(arrays):
        print(f"Array {i+1}: {array}")
        print(f"Sum of Array {i+1}: {sum(array)}")

dynamic_array_of_pointers()
