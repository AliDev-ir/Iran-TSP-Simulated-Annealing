# Iran-TSP-Simulated-Annealing
Efficient TSP solver using Simulated Annealing for Iran's provincial centers. Python code for route optimization and visualization. Explore shortest routes!

# Iran TSP Solver with Simulated Annealing

## Overview
This Python project implements a solver for the Traveling Salesman Problem (TSP), tailored for efficiently visiting provincial centers in Iran. It utilizes the Simulated Annealing algorithm to find optimal routes while considering the shortest distance.

## About the Traveling Salesman Problem (TSP)
The Traveling Salesman Problem is a classic optimization problem in computer science and operations research. Given a list of cities and the distances between each pair of cities, the objective is to find the shortest possible route that visits each city exactly once and returns to the original city. The problem is NP-hard, meaning that there is no known polynomial-time algorithm that guarantees finding the optimal solution for all instances.

## Features
- Solves the TSP for visiting provincial centers in Iran.
- Utilizes Simulated Annealing algorithm for route optimization.
- Includes Python code for solving TSP, visualizing routes, and analyzing results.
- Supports visualization of the optimized routes.

## Simulated Annealing Algorithm
Simulated Annealing is a probabilistic optimization algorithm inspired by the process of annealing in metallurgy. It starts with an initial solution and iteratively explores neighboring solutions by making random changes. These changes are accepted or rejected based on a probability determined by the difference in solution quality and the current "temperature". Over time, the algorithm gradually reduces the temperature, allowing it to escape local optima and converge towards a global optimum.

## Solution Method
1. **Initial Solution**: The algorithm starts with a greedy initial solution where each provincial center is visited in the order of their proximity.
2. **Annealing Process**: It then applies the Simulated Annealing algorithm to iteratively improve the solution by exploring neighboring solutions and accepting or rejecting them based on the acceptance probability.
3. **Route Optimization**: Throughout the annealing process, the algorithm aims to minimize the total distance traveled while ensuring that each provincial center is visited exactly once.
4. **Visualization**: After optimization, the code provides visualization of the optimized routes using matplotlib, allowing users to visually inspect the solution.

## Usage
1. **Download or Clone Repository**:  
   - Download the repository as a zip file and extract it, or clone it using Git:
     ```
     git clone https://github.com/AliDev-ir/Iran-TSP-Simulated-Annealing.git
     ```

2. **Install Dependencies**:  
   - Navigate to the project directory and install the required dependencies using pip:
     ```
     cd Iran-TSP-Simulated-Annealing
     ```

3. **Required Software**:
   - Python (>=3.6)
   - xlrd
   - matplotlib

4. **Run the Solver**:  
   - Execute the main script `test.py` to run the solver:
     ```
     python test.py
     ```

5. **View Optimized Routes**:  
   - After running the solver, you can view the optimized routes using the visualization provided.

## Example
```
python test.py
```

## Dependencies
- xlrd: `pip install xlrd`
- matplotlib: `pip install matplotlib`

## Contributors
- [Ali Vaez](https://github.com/AliDev-IR)

## License
This project is licensed under the [GPLv3 License](LICENSE).


# Connection

Email : Ali@alidev.ir

Website : [AliDev.ir](https://www.AliDev.ir)

Telegram : [AliDev-IR](https://t.me/AliDev_IR)

Linkdin : [Ali Vaez](https://www.linkedin.com/in/ali-vaez-568436298)

Github : [AliDev-IR](https://github.com/AliDev-ir)

Instagram : [Ali_Vaez79](https://instagram.com/Ali_Vaez79)

