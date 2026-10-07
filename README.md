# Traveling Salesman Problem Solver

A Python implementation of the Traveling Salesman Problem (TSP) that selects a random set of cities, computes the distances between them, and searches for a shorter route using an iterative swap-based optimization approach.

## Overview

This project reads city data from a CSV file, randomly selects a specified number of cities, calculates the pairwise distances between them, and attempts to find a near-optimal route that minimizes the total travel distance.

## Features

- Reads city data from a CSV file
- Randomly selects a configurable number of cities
- Computes pairwise distances using the Euclidean distance formula
- Optimizes the tour by testing city swaps
- Displays the final tour and total route length

## Project Files

- `Salesman_Traveling_Problem.py` - Main Python script implementing the TSP logic
- `README.md` - Project documentation
- `uscities.csv` - City dataset file required by the program

## Requirements

- Python 3.x
- Standard library modules: `csv`, `math`, and `random`

## Dataset

The program expects the file `uscities.csv` to be present in the same folder as the Python script.

This CSV file should contain city information with columns similar to:

- city name
- latitude
- longitude

The script reads the data and skips the header row before processing.

## Usage

1. Make sure Python is installed on your system.
2. Place `uscities.csv` in the same directory as `Salesman_Traveling_Problem.py`.
3. Run the script:

```bash
python Salesman_Traveling_Problem.py
```

4. The program will:
   - select a random set of cities
   - compute the travel distances
   - find a shorter route
   - print the tour and total distance

## How the Algorithm Works

The program performs the following steps:

1. Loads city records from the CSV file.
2. Randomly chooses `n` cities.
3. Builds a distance map for each city pair.
4. Initializes a tour in a random order.
5. Repeatedly tries swapping segments of the tour to reduce total length.
6. Keeps the tour that yields the shortest total distance.

## Example Output

```text
Selected Cities : [('City A', 42.3601, -71.0589), ('City B', 34.0522, -118.2437), ...]
Tour: [0, 2, 4, 1, 3]
Tour length: 1245.67
```

## Notes

- The implementation is a simple optimization approach and not a full exact TSP solver for very large city counts.
- The program is designed for learning and demonstration purposes.

## License

This project is provided for educational use.


