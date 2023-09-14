N = 5
matrix = [[x for x in range(y*N, (y+1)*N)] for y in range(N)]

row, col = 3, 2

drows = [-1, +1, 0, 0]
dcols = [0, 0, -1, +1]

print(matrix[row][col])
for idx in range(4):
    new_r = row + drows[idx]
    new_c = col + dcols[idx]

    if 0 <= new_r < N and 0 <= new_c < N and matrix[new_r][new_c]:
        print(matrix[new_r][new_c])

