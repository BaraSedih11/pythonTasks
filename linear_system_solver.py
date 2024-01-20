from linear_algebra import determinant_3x3, inverse_3x3, matrix_multiply

def solve_linear_system(coefficients, constants):
    A = coefficients
    b = [[constant] for constant in constants]  # Convert constants to a column matrix

    # Check if the system is solvable
    if determinant_3x3(A) == 0:
        raise ValueError("The system of equations is not solvable (determinant of coefficients matrix is zero).")

    # Calculate the inverse of the coefficients matrix
    A_inv = inverse_3x3(A)

    # Calculate the solution vector x
    x = matrix_multiply(A_inv, b)

    return x

# Given system of equations
coefficients_matrix = [[1, 2, 3], [2, 5, 3], [2, 0, 8]]
constants_vector = [10, 15, 20]

solution_vector = solve_linear_system(coefficients_matrix, constants_vector)

print()

print("Solution vector x:")
for i, value in enumerate(solution_vector):
    print(f"x{i + 1} = {value[0]:.2f}")