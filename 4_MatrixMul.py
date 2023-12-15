import threading

def matrix_multiply_row(row_a, matrix_b, result_row, col_count):
    for j in range(col_count):
        result_row[j] = sum(row_a[k] * matrix_b[k][j] for k in range(len(row_a)))

def matrix_multiply_parallel(matrix_a, matrix_b):
    row_count_a = len(matrix_a)
    col_count_a = len(matrix_a[0])
    row_count_b = len(matrix_b)
    col_count_b = len(matrix_b[0])

    if col_count_a != row_count_b:
        raise ValueError("Matrix dimensions are not compatible for multiplication")

    result_matrix = [[0 for i in range(col_count_b)] for j in range(row_count_a)]
    threads = []

    for i in range(row_count_a):
        thread = threading.Thread(target=matrix_multiply_row, args=(matrix_a[i], matrix_b, result_matrix[i], col_count_b))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result_matrix

matrix_a = [[1, 2], [3, 4], [5, 6]]
matrix_b = [[7, 8]]

result = matrix_multiply_parallel(matrix_a, matrix_b)

print("The req Matrix multiplication is: ")

for row in result:
    print(row)
