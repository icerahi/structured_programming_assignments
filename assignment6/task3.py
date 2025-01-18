#Task 3: Dynamic Matrix Multiplication

def matrix_multiplication():
    rows1,cols1 =map(int,input("Enter dimention for Matrix 1(rows Column:)").split())  
    matrix1 = []
    print(f"Enter the elements for Matrix 1 ({rows1}x{cols1}):")
    for i in range(rows1):
        row = list(map(int, input().split()))
        matrix1.append(row)

    rows2,cols2 =map(int,input("Enter dimention for Matrix 2(rows Column):").split())  

 
    if cols1 != rows2:
        print("Matrix multiplication is not possible. Number of columns in Matrix 1 must be equal to number of rows in Matrix 2.")
        return

    matrix2 = []
    print(f"Enter the elements for Matrix 2 ({rows2}x{cols2}):")
    for i in range(rows2):
        row = list(map(int, input().split()))
        matrix2.append(row)
 
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
 
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
 
    print("\nResulting Matrix:")
    for row in result:
        print(" ".join(map(str, row)))

matrix_multiplication()
