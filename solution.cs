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