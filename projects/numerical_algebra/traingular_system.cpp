#include <iostream>
#include <vector>
#include <Eigen/Dense> // Required for the Eigen version

/**
 * METHOD 1: Using Standard C++ Vectors
 * This is similar to Python lists. It's great for understanding the logic
 * without needing external libraries.
 */
void solveWithStandardVector()
{
    std::cout << "--- Method 1: std::vector ---" << std::endl;

    // Defining the Matrix L (4x4)
    std::vector<std::vector<double>> L = {
        {2, 0, 0, 0},
        {-1, 2, 0, 0},
        {3, 1, -1, 0},
        {4, 1, -3, 3}};

    // Defining vector b
    std::vector<double> b = {2, 3, 2, 9};
    int n = b.size();
    std::vector<double> y(n, 0.0); // Initialize y with zeros

    // Forward Substitution Logic
    for (int i = 0; i < n; ++i)
    {
        double sum = b[i];
        for (int j = 0; j < i; ++j)
        {
            sum -= L[i][j] * y[j];
        }

        if (L[i][i] == 0)
        {
            std::cerr << "Error: Division by zero!" << std::endl;
            return;
        }
        y[i] = sum / L[i][i];
    }

    // Printing the result
    std::cout << "Solution y: ";
    for (double val : y)
    {
        std::cout << val << " ";
    }
    std::cout << "\n\n";
}

/**
 * METHOD 2: Using Eigen
 * This is the professional way in Robotics/AI. It uses optimized
 * linear algebra operations.
 */
void solveWithEigen()
{
    std::cout << "--- Method 2: Eigen Library ---" << std::endl;

    // Define Matrix and Vector using Eigen types
    Eigen::MatrixXd L(4, 4);
    L << 2, 0, 0, 0,
        -1, 2, 0, 0,
        3, 1, -1, 0,
        4, 1, -3, 3;

    Eigen::VectorXd b(4);
    b << 2, 3, 2, 9;

    // Forward substitution using Eigen's built-in triangular solver
    // This is much faster and more stable than manual loops.
    Eigen::VectorXd y = L.triangularView<Eigen::Lower>().solve(b);

    std::cout << "Solution y:\n"
              << y << "\n\n";
}

int main()
{
    // Calling both implementations
    solveWithStandardVector();
    solveWithEigen();

    return 0;
}