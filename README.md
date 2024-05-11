# Question: How do you detect whether a given matrix has a cycle of connected same-valued cells? C# Summary

The provided C# code is a solution to detect whether a given matrix has a cycle of connected cells with the same value. The code defines a 2D matrix and checks for cycles using depth-first search (DFS). The DFS algorithm starts at each unvisited cell in the matrix and explores as far as possible along each branch before backtracking. The 'IsSafe' function checks if a cell is within the matrix boundaries and has not been visited before. The 'IsCycle' function checks if there is a cycle in the matrix by comparing the current cell with its adjacent cells. If an adjacent cell has the same value and is not the cell we came from, the function recursively checks for a cycle from this new cell. If a cycle is found, the function returns true. The 'HasCycle' function iterates over all cells in the matrix and calls the 'IsCycle' function for each unvisited cell. If a cycle is found, it returns true; otherwise, it returns false after checking all cells. The result is then printed to the console.

---

# Python Differences

Both the C# and Python versions solve the problem using a similar approach. They both use Depth-First Search (DFS) to traverse the matrix and check for cycles. The main difference lies in the syntax and some language-specific features.

1. Array Declaration: In C#, arrays are declared with a specific size and type. In Python, lists (which are used as arrays) are dynamically sized and can hold any type of data.

2. Function Definitions: In C#, functions are defined using the `static` keyword inside a class. In Python, functions are defined using the `def` keyword and can be defined anywhere in the code, not necessarily inside a class.

3. Boolean Expressions: In C#, boolean expressions are written as `!visited[i, j]` whereas in Python, they are written as `visited[i][j] == False`.

4. Ternary Operator: In C#, the ternary operator is used as `condition ? true : false`. Python uses a different syntax for the ternary operator: `true if condition else false`.

5. Print Statements: In C#, `Console.WriteLine()` is used to print to the console. In Python, the `print()` function is used.

6. Main Function: In C#, the main function is defined as `public static void Main()`. In Python, the main function is usually defined as a function named `main()`, and is called in a special line `if __name__ == "__main__": main()`.

7. Checking Equality: In C#, `==` is used to check equality. In Python, `==` is also used to check equality, but `is` can be used to check if two variables refer to the same object.

8. Return Statements: In C#, every path in a function must explicitly return a value if the function is not void. In Python, if no return statement is encountered, the function will return `None` by default.

---

# Java Differences

Both the C# and Java versions solve the problem using a similar approach. They both use a depth-first search (DFS) algorithm to traverse the matrix and check for cycles. The DFS algorithm is implemented using recursion in both versions. 

The main differences between the two versions are:

1. Input: The C# version has a hardcoded matrix, while the Java version reads the matrix from the console using a Scanner object.

2. Output: The C# version outputs "Matrix has a cycle" or "Matrix doesn't have a cycle", while the Java version outputs "Yes" or "No".

3. Method Names: The C# version uses the method names `IsSafe`, `IsCycle`, and `HasCycle`, while the Java version uses the method name `dfs`.

4. Safety Check: The C# version has a separate `IsSafe` method to check if a cell is within the matrix boundaries and has not been visited yet. The Java version includes this check directly in the `dfs` method.

5. Matrix Dimensions: The C# version uses `ROW` and `COL` to store the dimensions of the matrix, while the Java version uses `n` and `m`.

6. Visited Matrix: Both versions use a 2D boolean array to keep track of visited cells. In C#, this array is created in the `HasCycle` method, while in Java, it is created in the `main` method.

7. Language Features: The C# version uses the `GetLength` method to get the dimensions of the matrix, which is a feature specific to C#. The Java version uses the `.length` property to get the dimensions of the matrix, which is a feature specific to Java.

---
