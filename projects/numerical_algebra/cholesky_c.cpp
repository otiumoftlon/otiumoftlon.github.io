#include <iostream>
#include <vector>
#include <Eigen/Dense>
#include <Eigen/Cholesky>

void printMatrixInfo(const Eigen::MatrixXd &matrix)
{
    std::cout << "Matrix contents:\n"
              << matrix << std::endl;

    // Perform Cholesky Decomposition (LL^T)
    Eigen::LLT<Eigen::MatrixXd> llt(matrix);

    // Check if the decomposition was successful (i.e., matrix is Positive Definite)
    if (llt.info() == Eigen::Success)
    {
        std::cout << "Cholesky Decomposition (L):\n"
                  << llt.matrixL().toDenseMatrix() << std::endl;
    }
    else
    {
        std::cout << "Matrix is not positive definite, Cholesky decomposition not possible." << std::endl;
    }
}

int main()
{
    // Define your matrices
    Eigen::Matrix3d A;
    A << 9, 3, 3,
        3, 10, 7,
        3, 5, 9;

    Eigen::Matrix3d B;
    B << 4, 2, 6,
        2, 2, 5,
        6, 5, 29;

    Eigen::Matrix3d C;
    C << 4, 4, 8,
        4, -4, 1,
        8, 1, 6;

    Eigen::Matrix3d D;
    D << 1, 1, 1,
        1, 2, 2,
        1, 2, 1;

    // Use a std::vector to store the matrices for iteration
    std::vector<Eigen::MatrixXd> matrices = {A, B, C, D};

    for (size_t i = 0; i < matrices.size(); ++i)
    {
        std::cout << "--- Matrix " << i + 1 << " ---" << std::endl;
        printMatrixInfo(matrices[i]);
        std::cout << std::endl;
    }

    return 0;
}