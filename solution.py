Here is a Python console application that solves the problem:

```python
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


def isValid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def isCyclic(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == False:
                if isCyclicUtil(matrix, visited, i, j, -1, -1) == True:
                    return True
    return False


def main():
    matrix = [[1, 2, 3, 4],
              [5, 1, 2, 3],
              [6, 5, 1, 2],
              [7, 6, 5, 1]]
    print(isCyclic(matrix))


if __name__ == "__main__":
    main()
```

This Python console application uses Depth-First Search (DFS) to check if a cycle exists in the given matrix. The `isCyclicUtil` function is a helper function that performs the DFS on the matrix. The `isValid` function checks if a given cell is within the matrix boundaries. The `isCyclic` function initializes a visited matrix and checks each cell of the given matrix for a cycle. The `main` function is the entry point of the application.