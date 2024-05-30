def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def sum_of_pos_elements(row):
    return sum(x for x in row if x > 0)

file_path = '1.txt'
matrix = read_matrix_from_file(file_path)

min_column = min(matrix, key=sum_of_pos_elements)
print(min_column)
