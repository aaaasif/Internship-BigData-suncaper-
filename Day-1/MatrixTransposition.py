def transpose_matrix(matrix): #Q4 Tanspose matrix
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

# Test the function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)