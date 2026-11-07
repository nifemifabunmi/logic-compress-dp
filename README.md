# Logic-Compress-DP Engine

A modular Python framework demonstrating advanced algorithmic optimizations across three distinct domains: Data Compression, Dynamic Programming (Sequence Alignment & Probabilistic Modeling), and Graph-Based Constraint Satisfaction (NP-Complete Reduction).

## Project Scope
This project serves as an algorithmic toolbox designed to solve real-world optimization problems. It is structured to demonstrate clean architecture, complexity analysis, and algorithmic efficiency using a unified Command Line Interface (CLI).

### 1. Data Compression (`src/compression/`)
*   **Huffman Coding:** Optimal prefix-tree encoding utilizing priority queues to achieve variable-length encoding based on character frequencies.
*   **Jabberwocky:** Adaptive dictionary compression (LZW-style) for real-time data reduction without pre-shared dictionaries.

### 2. Dynamic Programming & Probabilistic Models (`src/dp/`)
*   **Hidden Markov Models (HMM):** Implementation of the Viterbi algorithm to infer the most likely sequence of hidden states from observable data (e.g., isolating coin tosses).
*   **Sequence Alignment:** Edit Distance and Longest Common Subsequence (LCS) optimizations.

### 3. Constraint Satisfaction & Graphs (`src/graphs/`)
*   **2-SAT Solver:** Reduces Boolean constraint systems (e.g., the "Existential Lightbulb Problem") into implication graphs.
*   **Tarjan's Algorithm:** Computes Strongly Connected Components (SCC) in \(O(V+E)\) time to detect logical contradictions in massive datasets (tested up to 10,000 constraints).

## Architecture
```text
├── main.py                  # CLI Entry Point
├── data/                    # Sample test data
└── src/
    ├── compression/         # Huffman & Jabberwocky
    ├── dp/                  # HMM (Viterbi) & Edit Distance
    └── graphs/              # 2-SAT Solver (Tarjan's SCC)