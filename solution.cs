```C#
using System;
using System.Collections.Generic;

public class Program
{
    static int[] dx = { -1, 0, 1, 0 };
    static int[] dy = { 0, 1, 0, -1 };
    static int ROW, COL;

    public static void Main()
    {
        int[,] matrix = {
            { 1, 2, 3, 4 },
            { 5, 1, 2, 3 },
            { 6, 5, 1, 2 },
            { 7, 6, 5, 1 }
        };

        ROW = matrix.GetLength(0);
        COL = matrix.GetLength(1);

        bool hasCycle = HasCycle(matrix);

        Console.WriteLine(hasCycle ? "Matrix has a cycle" : "Matrix doesn't have a cycle");
    }

    static bool IsSafe(int[,] matrix, int x, int y, bool[,] visited)
    {
        return (x >= 0 && x < ROW && y >= 0 && y < COL && !visited[x, y]);
    }

    static bool IsCycle(int[,] matrix, int x, int y, int prevX, int prevY, bool[,] visited)
    {
        visited[x, y] = true;

        for (int k = 0; k < 4; k++)
        {
            int newX = x + dx[k];
            int newY = y + dy[k];

            if (IsSafe(matrix, newX, newY, visited))
            {
                if (matrix[newX, newY] == matrix[x, y])
                {
                    if (!(newX == prevX && newY == prevY) && IsCycle(matrix, newX, newY, x, y, visited))
                    {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    static bool HasCycle(int[,] matrix)
    {
        bool[,] visited = new bool[ROW, COL];

        for (int i = 0; i < ROW; i++)
        {
            for (int j = 0; j < COL; j++)
            {
                if (!visited[i, j] && IsCycle(matrix, i, j, -1, -1, visited))
                {
                    return true;
                }
            }
        }

        return false;
    }
}
```