# Simulated Annealing for Traveling Salesman Problem (TSP)

This project demonstrates the use of the Simulated Annealing algorithm to solve the Traveling Salesman Problem (TSP). The TSP is a well-known optimization problem where the goal is to find the shortest possible route that visits each city exactly once and returns to the origin city.

## Features

- Randomly generates cities on a 2D plane.
- Uses Simulated Annealing to optimize the route.
- Plots the optimized route.
- Adjustable parameters for fine-tuning the algorithm.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## How to Run

1. Install the required libraries:

   ```bash
   pip install numpy matplotlib
   ```

2. Copy the script and run it in your Python environment.

3. Adjust parameters if needed:
   - `num_cities`: Number of cities.
   - `initial_temp`: Initial temperature for simulated annealing.
   - `cooling_rate`: Cooling rate for temperature reduction.
   - `max_iter`: Maximum number of iterations.

## Results

The program outputs:
- Best route found.
- Total distance of the best route.
- A plot showing the optimized route.

## Example Output

Example of a 20-city optimization:

```
Best route: [0, 5, 1, 12, 18, 4, 13, 11, 10, 19, 6, 3, 7, 17, 9, 8, 14, 2, 16, 15]
Best total distance: 495.23
```

The program also displays a graphical representation of the optimized route.

## License

This project is for educational purposes. Feel free to modify and use the code as needed.

---
