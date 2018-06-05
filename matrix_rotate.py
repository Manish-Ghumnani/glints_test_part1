def rotate_matrix(matrix, m, n, r):
    while r > 0:
        row_init = 0
        row_end = m-1
        col_init = 0
        col_end = n-1

        copy_matrix = [[0] * n for k in range(m)]

        while col_end > col_init:
            # for all elements in the first row or where row 0
            for i in range(col_init, col_end):
                copy_matrix[row_init][i] = matrix[row_init][i+1]

            # for all elements in column zero but after row 0
            for j in range(row_init+1, row_end+1):
                copy_matrix[j][row_init] = matrix[j-1][row_init]

            # for all elements in the last row after the first column
            for a in range(col_init+1, col_end+1):
                copy_matrix[row_end][a] = matrix[row_end][a-1]

            # for all elements in the column except the last row
            for b in range(row_init, row_end):
                copy_matrix[b][col_end] = matrix[b+1][col_end]

            # increment the init and end counters to solve for the 'inner' 2d matrix
            # and repeat until col_end and col_init meet
            row_init += 1
            col_init += 1
            row_end -= 1
            col_end -= 1

        r -= 1
        # copy to work on the rotated matrix
        matrix = copy_matrix
    print_matrix(copy_matrix, m, n)


def print_matrix(mat, m, n):
    for i in range(0, m):
        print()
        for j in range(0, n):
            print(mat[i][j], end=" ")


if __name__ == '__main__':
    m, n, r = map(int, input().split())
    mat = [[0]*n for k in range(m)]
    for i in range(0,m):
        mat[i] = list(map(int, input().rstrip().split()))
    rotate_matrix(mat, m, n, r)
