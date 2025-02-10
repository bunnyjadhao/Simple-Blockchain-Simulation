# Simple Blockchain Simulation

## Description
This project is a simple blockchain simulation in Python that demonstrates key blockchain concepts:
- **Block Structure:** Each block contains an index, timestamp, transactions, previous hash, nonce, and current hash.
- **Hashing:** Uses SHA-256 for block hash generation.
- **Proof-of-Work:** Implements a basic mining mechanism where a block’s hash must begin with a specified number of zeros.
- **Validation:** Includes a method to verify the integrity of the blockchain and detect tampering.

## Setup and Execution

### Prerequisites
- Python 3.9 (or later) installed on your system.
- Optionally, Docker (if you wish to run the simulation in a container).

### Running Locally
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/simple-blockchain-simulation.git
    ```
2. Navigate to the project directory:
    ```bash
    cd simple-blockchain-simulation
    ```
3. Run the simulation:
    ```bash
    python blockchain_simulation.py
    ```

### Running with Docker
1. Build the Docker image:
    ```bash
    docker build -t blockchain-sim .
    ```
2. Run the Docker container:
    ```bash
    docker run --rm blockchain-sim
    ```

## Project Structure
- **blockchain_simulation.py** — Main Python script containing the blockchain simulation.
- **Dockerfile** — Docker configuration to run the simulation in a container.
- **README.md** — This file with setup and usage instructions.
