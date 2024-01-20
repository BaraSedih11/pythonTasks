def matrix_multiply(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def determinant_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    det = a * determinant_2x2([[e, f], [h, i]]) - b * determinant_2x2([[d, f], [g, i]]) + c * determinant_2x2(
        [[d, e], [g, h]])

    return det


def inverse_3x3(matrix):
    det = determinant_3x3(matrix)

    if det == 0:
        raise ValueError("The matrix is not invertible (determinant is zero).")

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    adjugate = [
        [e * i - f * h, c * h - b * i, b * f - c * e],
        [f * g - d * i, a * i - c * g, c * d - a * f],
        [d * h - e * g, b * g - a * h, a * e - b * d]
    ]

    inverse = [[adjugate[row][col] / det for col in range(3)] for row in range(3)]

    return inverse


# Example usage:
matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result_multiply = matrix_multiply(matrix_A, matrix_B)
print("Matrix Multiplication Result:")
for row in result_multiply:
    print(row)

result_det_2x2 = determinant_2x2([[1, 2], [3, 4]])
print("\nDeterminant of 2x2 Matrix:", result_det_2x2)

result_det_3x3 = determinant_3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Determinant of 3x3 Matrix:", result_det_3x3)

result_inverse_3x3 = inverse_3x3([[4, 7, 2], [2, 6, 1], [5, 8, 3]])
print("\nInverse of 3x3 Matrix:")
for row in result_inverse_3x3:
    print(row)
