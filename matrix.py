import sys


def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")
    choice = int(input("Your choice: "))
    return choice


def matrix_init():
    # here
    choice = menu()

    # call the appropriate method depending on choice
    if choice == 1:
        matrix_addition()
    elif choice == 2:
        matrix_multiply_constant()
    elif choice == 3:
        matrix_multiplication()
    elif choice == 0:
        sys.exit()


def matrix_creator(matrix_dimensions):

    int_coordinates = [int(x) for x in matrix_dimensions.split(" ")]

    rows = []
    rows_list = []
    print("Enter matrix:")
    for x in range(int_coordinates[0]):
        row_data = input()
        rows_list.append(row_data.split())
        int_coordinates[0] += 1

    for y in rows_list:
        rows_int = [int(x) for x in y]
        rows.append(rows_int)
    # print(rows)
    return rows


def matrix_addition():
    matrix_dimension_1 = input("Enter size of first matrix: ")
    mat1 = matrix_creator(matrix_dimension_1)

    matrix_dimension_2 = input("Enter size of second matrix: ")
    mat2 = matrix_creator(matrix_dimension_2)
    print("The result is: ")

    if len(mat1) != len(mat2):
        print("ERROR")
    else:
        for i, j in zip(mat1, mat2):
            if len(i) != len(j):
                print("ERROR")
            else:
                result = [a + b for a, b in zip(i, j)]
                for a in result:
                    print(a, end=" ")
                print()


def matrix_multiply_constant():
    matrix_dimensions = input("Enter size of matrix")
    mat = matrix_creator(matrix_dimensions)

    constant = int(input("Enter constant: "))
    for i in mat:
        result = [a * constant for a in i]
        for a in result:
            print(a, end=" ")
        print()


def matrix_multiplication():
    matrix_dimension_1 = input("Enter size of first matrix: ")
    mat1 = matrix_creator(matrix_dimension_1)

    matrix_dimension_2 = input("Enter size of first matrix: ")
    mat2 = matrix_creator(matrix_dimension_2)


while True:
    matrix_init()
    print()

