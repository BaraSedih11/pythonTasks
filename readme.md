# Linear Algebra and Matrix Operations in Python

This repository contains Python code for performing linear algebra operations and matrix manipulations. The tasks include creating a class for products, implementing matrix multiplication, finding determinants, solving linear systems, and more.

## Task 1: Total and Average Sales Calculation

The script `sales_calculator.py` contains a Python program that calculates the total sales and average sales for a given week's sales amounts.

## Task 2: Product Class and Basket Discount

The script `product_operations.py` defines a `Product` class with attributes like name, price, and quantity. Additionally, it includes functions to calculate the total cost of a given basket of products and apply a discount.

## Task 5: Linear Algebra Functions

The script `linear_algebra.py` includes Python functions for matrix multiplication, determinant calculation for 2x2 and 3x3 matrices, and inverse calculation for a 3x3 matrix.

## Task 6: Solving Linear Systems

The script `linear_system_solver.py` implements functions to solve a system of linear equations in matrix form (Ax = b). It uses the functions from Task 5 for matrix operations.

### Example Usage

```python
# Example linear system
coefficients_matrix = [[1, 2, 3], [2, 5, 3], [2, 0, 8]]
constants_vector = [10, 15, 20]

# Solve the system
solution_vector = solve_linear_system(coefficients_matrix, constants_vector)

# Print the solution
print("Solution vector x:")
for i, value in enumerate(solution_vector):
    print(f"x{i + 1} = {value[0]:.2f}")
```

Feel free to explore each task's script for more details and examples.

## How to Run
Ensure you have Python installed, then run each script individually using a Python interpreter.

```bash
python sales_calculator.py
python product_operations.py
python linear_algebra.py
python linear_system_solver.py
```
## Dependencies
No external dependencies are required. The scripts use standard Python libraries.
