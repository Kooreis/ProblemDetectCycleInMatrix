def isCyclicUtil(matrix, visited, x, y, parent_x, parent_y):
    rows, cols = len(matrix), len(matrix[0])
    visited[x][y] = True

    rowNbr = [-1, 0, 0, 1]
    colNbr = [0, -1, 1, 0]

    for k in range(4):
        if isValid(x + rowNbr[k], y + colNbr[k], rows, cols):
            if matrix[x + rowNbr[k]][y + colNbr[k]] == matrix[x][y]:
                if visited[x + rowNbr[k]][y + colNbr[k]]:
                    if x + rowNbr[k] != parent_x or y + colNbr[k] != parent_y:
                        return True
                else:
                    if isCyclicUtil(matrix, visited, x + rowNbr[k], y + colNbr[k], x, y):
                        return True
    return False