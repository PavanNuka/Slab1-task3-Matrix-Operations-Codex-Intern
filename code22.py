import numpy as np

def get_matrix_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print(f"Enter the elements row by row (separated by spaces):")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print(f"Each row must have {cols} elements. Please try again.")
            return get_matrix_input()
        matrix.append(row)
    return np.array(matrix)

def matrix_operations():
    print("Welcome to the Matrix Operations Tool!")
    print("1. Add two matrices")
    print("2. Subtract two matrices")
    print("3. Multiply two matrices")
    print("4. Transpose a matrix")
    print("5. Calculate determinant of a matrix")
    print("6. Exit")
    
    while True:
        choice = input("\nChoose an operation (1-6): ")
        
        if choice == '1':
            print("\nMatrix Addition")
            print("Enter the first matrix:")
            matrix1 = get_matrix_input()
            print("Enter the second matrix:")
            matrix2 = get_matrix_input()
            if matrix1.shape == matrix2.shape:
                result = matrix1 + matrix2
                print("Resultant Matrix:\n", result)
            else:
                print("Matrix dimensions must match for addition.")

        elif choice == '2':
            print("\nMatrix Subtraction")
            print("Enter the first matrix:")
            matrix1 = get_matrix_input()
            print("Enter the second matrix:")
            matrix2 = get_matrix_input()
            if matrix1.shape == matrix2.shape:
                result = matrix1 - matrix2
                print("Resultant Matrix:\n", result)
            else:
                print("Matrix dimensions must match for subtraction.")

        elif choice == '3':
            print("\nMatrix Multiplication")
            print("Enter the first matrix:")
            matrix1 = get_matrix_input()
            print("Enter the second matrix:")
            matrix2 = get_matrix_input()
            if matrix1.shape[1] == matrix2.shape[0]:
                result = np.dot(matrix1, matrix2)
                print("Resultant Matrix:\n", result)
            else:
                print("The number of columns of the first matrix must equal the number of rows of the second matrix.")

        elif choice == '4':
            print("\nMatrix Transpose")
            print("Enter the matrix:")
            matrix = get_matrix_input()
            result = matrix.T
            print("Transposed Matrix:\n", result)

        elif choice == '5':
            print("\nMatrix Determinant")
            print("Enter the square matrix:")
            matrix = get_matrix_input()
            if matrix.shape[0] == matrix.shape[1]:
                result = np.linalg.det(matrix)
                print(f"Determinant: {result}")
            else:
                print("Determinant can only be calculated for square matrices.")

        elif choice == '6':
            print("Exiting the Matrix Operations Tool. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    matrix_operations()
