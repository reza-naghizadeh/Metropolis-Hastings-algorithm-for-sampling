## Overview

This Python script implements the **Metropolis-Hastings algorithm**, a Markov Chain Monte Carlo (MCMC) method for sampling from a target distribution. It includes data preprocessing, acceptance rate computation, and visualization of the input and sampled distributions. 

This code was developed as part of my Probabilistic Graphical Models (PGM) course project at IASBS.

## Features

- **Preprocessing**: Loads and preprocesses data from a file.
- **Proposal Distribution**: Uses a normal distribution for proposal generation.
- **Acceptance Rate Calculation**: Determines whether to accept or reject proposed samples.
- **Burn-In**: Removes a percentage of initial samples to improve convergence.
- **Visualization**: Provides histograms of the original and sampled distributions.
- **Statistical Summary**: Computes the mean and standard deviation of the sampled data.

## Files
- **`input.txt`**: Contains the target distribution data.
- **`MetropolisHastings.py`**: Main script for running the algorithm.

## Dependencies

- **Python 3.x**
- **NumPy**: For numerical operations.
- **Matplotlib**: For data visualization.

Install the dependencies using:
```bash
pip install numpy matplotlib
```

## How to Use

1. Place the target distribution data in `input.txt`.
2. Run the script:
   ```bash
   python MetropolisHastings.py
   ```
3. The script will:
   - Load and preprocess the data.
   - Perform 100,000 iterations of the Metropolis-Hastings algorithm.
   - Apply a burn-in phase to discard 30% of initial samples.
   - Compute and display the mean and standard deviation of the samples.
   - Visualize the input and sampled distributions.

## Key Functions

### `Preprocess()`
Loads and preprocesses the target distribution from `input.txt`.

### `ProposalDistribution(mean, sd, number)`
Computes the proposal distribution using a normal distribution.

### `AcceptanceRate(xZero, xPrim, dataSet)`
Calculates the acceptance rate based on the likelihood and proposal distribution.

### `BurnIn(samples, percentage)`
Removes the initial samples based on the specified percentage.

### `FinalFinder(samples)`
Calculates and displays the mean and standard deviation of the sampled distribution.

### `Visualization(dataSet, samples)`
Plots histograms of the input and sampled distributions.

## Example Output

- **Mean** and **Standard Deviation** of the sampled data.
- Histograms comparing the original and sampled distributions.

## Notes

- The `input.txt` file should contain numeric data, one value per line.
- Adjust the `iteration` variable to control the number of MCMC steps.
- The burn-in percentage can be modified by changing `burnInPercentage`.