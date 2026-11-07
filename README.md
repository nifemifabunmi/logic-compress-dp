# Logic-Compress-DP Engine

A modular Python framework demonstrating advanced algorithmic optimizations across three distinct domains: Data Compression, Dynamic Programming (Sequence Alignment & Probabilistic Modeling), and Graph-Based Constraint Satisfaction (NP-Complete Reduction).

## Project Scope
This project serves as an algorithmic toolbox designed to solve real-world optimization problems. It is structured to demonstrate clean architecture, complexity analysis, and algorithmic efficiency.

### 1. Data Compression (`src/compression/`)
*   **Huffman Coding:** Optimal prefix-tree encoding utilizing priority queues.
*   **Jabberwocky:** Adaptive dictionary compression (LZW-style) for real-time data reduction without pre-shared dictionaries.

### 2. Dynamic Programming & Probabilistic Models (`src/dp/`)
*   **Hidden Markov Models (HMM):** Viterbi, Forward, and Backward algorithms to infer hidden state sequences from observable data.
*   **Sequence Alignment:** Edit Distance and Longest Common Subsequence (LCS) optimizations.

### 3. Constraint Satisfaction & Graphs (`src/graphs/`)
*   **2-SAT Solver:** Reduces Boolean constraint systems (e.g., the "Existential Lightbulb Problem") to implication graphs.
*   **Tarjan's Algorithm:** Computes Strongly Connected Components (SCC) in \(O(V+E)\) time to detect contradictions in massive datasets (tested up to 10,000 constraints).

## Tech Stack
*   **Language:** Python 3
*   **Concepts:** Dynamic Programming, Greedy Algorithms, Graph Theory, SCC, NP-Hardness.

## How to Run
*(Will be updated once the CLI is built)*