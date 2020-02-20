import numpy as np
sudoku_matrix = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                          [6, 0, 0, 1, 9, 5, 0, 0, 0],
                          [0, 9, 8, 0, 0, 0, 0, 6, 0],
                          [8, 0, 0, 0, 6, 0, 0, 0, 3],
                          [4, 0, 0, 8, 0, 3, 0, 0, 1],
                          [7, 0, 0, 0, 2, 0, 0, 0, 6],
                          [0, 6, 0, 0, 0, 0, 2, 8, 0],
                          [0, 0, 0, 4, 1, 9, 0, 0, 5],
                          [0, 0, 0, 0, 8, 0, 0, 7, 9]])
number_list = [x for x in range(1, 10)]


def possible_number(a, b, number):
    x1, y1 = (a // 3) * 3, (b // 3) * 3
    flag = False
    sub_array = sudoku_matrix[x1:(x1 + 3), y1:(y1 + 3)]
    if number not in sudoku_matrix[a]:
        if number not in sudoku_matrix[:, [b]]:
            for x in sub_array:
                if number in x:
                    flag = True
                    break
            if flag == False:
                return True
    return False


def solver():
    for a in range(0, 9):
        for b in range(0, 9):
            if sudoku_matrix[a][b] == 0:
                for number in number_list:
                    if possible_number(a, b, number):
                        sudoku_matrix[a][b] = number
                        solver()
                        sudoku_matrix[a][b] = 0
                return
    print(sudoku_matrix)


if __name__ == '__main__':
    solver()