#include <iostream>
#include <vector>
#include <Eigen/Dense> // Required for the Eigen version

/**
 * METHOD 1: Using Standard C++ Vectors
 * This is similar to Python lists. It's great for understanding the logic
 * without needing external libraries.
 */

#include <iostream>
#include <vector>
#include <functional>

void solveTriangularRecursive()
{
    std::cout << "--- Method 1: std::vector ---\n";

    std::vector<std::vector<double>> L = {
        {2, 0, 0, 0},
        {-1, 2, 0, 0},
        {3, 1, -1, 0},
        {4, 1, -3, 3}};

    std::vector<double> b = {2, 3, 2, 9};
    int n = b.size();

    // Must start from b
    std::vector<double> y = b;

    // Recursive lambda
    std::function<void(int)> helper = [&](int k)
    {
        if (k == n)
            return;

        double value = y[k] / L[k][k];
        y[k] = value;

        for (int j = k + 1; j < n; ++j)
        {
            y[j] -= L[j][k] * value; // <-- fixed index
        }

        helper(k + 1);
    };

    helper(0);

    std::cout << "Solution y: ";
    for (double val : y)
        std::cout << val << " ";
    std::cout << "\n\n";
}

int main()
{
    solveTriangularRecursive();
    return 0;
}
