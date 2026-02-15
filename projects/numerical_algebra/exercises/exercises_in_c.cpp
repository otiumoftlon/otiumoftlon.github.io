#include <iostream>
#include <iomanip>
#include <vector>
#include <random>
#include <chrono>
#include <string>
#include <Eigen/Dense>

using Clock = std::chrono::high_resolution_clock;

int main()
{
    std::cout << "Matrix-Vector Multiplication (C++ | vector vs Eigen)\n";
    std::cout << std::string(100, '-') << "\n";
    std::cout << std::setw(8) << "n"
              << " | " << std::setw(18) << "Loops (vector)"
              << " | " << std::setw(18) << "Eigen"
              << " | " << std::setw(10) << "Speedup\n";
    std::cout << std::string(100, '-') << "\n";

        std::mt19937 gen(42);
    std::uniform_real_distribution<double> dist(0.0, 1.0);

    // Limit maximum size to avoid memory issues
    std::vector<int> sizes = {100, 200, 400, 800, 1600, 3200};

    for (int n : sizes)
    {
        // Allocate memory once and reuse
        std::vector<double> A(n * n);
        std::vector<double> x(n);
        std::vector<double> b_loop(n, 0.0);

        // Fill with random data
        for (auto &v : A)
            v = dist(gen);
        for (auto &v : x)
            v = dist(gen);

        // ------------------------
        // std::vector (row-major)
        // ------------------------
        auto t0 = Clock::now();

        for (int i = 0; i < n; ++i)
        {
            double sum = 0.0;
            for (int j = 0; j < n; ++j)
            {
                sum += A[i * n + j] * x[j];
            }
            b_loop[i] = sum;
        }

        auto t1 = Clock::now();
        double loop_time = std::chrono::duration<double>(t1 - t0).count();

        // ------------------------
        // Eigen (using same data)
        // ------------------------
        using MatrixRowMajor = Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>;

        // Map existing data to Eigen structures (zero-copy)
        Eigen::Map<MatrixRowMajor> Ae(A.data(), n, n);
        Eigen::Map<Eigen::VectorXd> xe(x.data(), n);
        Eigen::VectorXd be(n);

        t0 = Clock::now();
        be = Ae * xe;
        t1 = Clock::now();

        double eigen_time = std::chrono::duration<double>(t1 - t0).count();

        // Calculate speedup (Eigen vs loops)
        double speedup = loop_time / eigen_time;

        std::cout << std::setw(8) << n
                  << " | " << std::setw(18) << std::fixed << std::setprecision(8) << loop_time
                  << " | " << std::setw(18) << eigen_time
                  << " | " << std::setw(10) << std::setprecision(2) << speedup << "x\n";

        // Verify results match (optional sanity check)
        double max_diff = 0.0;
        for (int i = 0; i < n; ++i)
        {
            max_diff = std::max(max_diff, std::abs(b_loop[i] - be(i)));
        }
        if (max_diff > 1e-10)
        {
            std::cerr << "Warning: Results differ by " << max_diff << "\n";
        }
    }

    std::cout << std::string(100, '-') << "\n";

    return 0;
}