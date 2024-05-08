Here is a Java console application that solves the problem:

```java
import java.util.Scanner;

public class Main {
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int n, m;
    static int[][] matrix;
    static boolean[][] visited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        matrix = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }

        boolean cycle = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j]) {
                    if (dfs(i, j, -1, -1, matrix[i][j])) {
                        cycle = true;
                        break;
                    }
                }
            }
        }

        System.out.println(cycle ? "Yes" : "No");
    }

    static boolean dfs(int x, int y, int px, int py, int color) {
        visited[x][y] = true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (!(nx == px && ny == py) && matrix[nx][ny] == color) {
                    if (visited[nx][ny] || dfs(nx, ny, x, y, color)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}
```

This program reads a matrix from the console and checks if there is a cycle of connected same-valued cells in it. The matrix is represented as a 2D array of integers. The program uses depth-first search (DFS) to traverse the matrix. If it encounters a cell that has already been visited and has the same value as the current cell, it means that a cycle has been found. The program outputs "Yes" if a cycle is found and "No" otherwise.