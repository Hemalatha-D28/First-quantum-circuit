# First-quantum-circuit
Quantum circuit experiments and fast implementations using Qiskit. 
Quantum Computing Projects (Qiskit + qBraid)

This repository contains my quantum computing experiments built using **Qiskit**, **Python**, and executed using **VS Code** and **qBraid cloud platform**.

These projects demonstrate fundamental quantum computing concepts such as superposition, entanglement, and quantum measurement.

---

## 📁 Projects Included

### 🔹 1. Bell State
- Creates a 2-qubit entangled Bell state
- Demonstrates quantum entanglement
- Output shows correlated results (00 and 11)

---

### 🔹 2. Quantum Circuit Shots
- Runs quantum circuits with multiple shots (1024)
- Produces probability distribution of outcomes
- Helps understand measurement statistics

---

### 🔹 3. GHZ State (3-qubit)
- Creates Greenberger–Horne–Zeilinger state
- State: (|000⟩ + |111⟩) / √2
- Demonstrates multi-qubit entanglement

---

### 🔹 4. GHZ Circuit (6-qubit)
- Extended entanglement across 6 qubits
- State: (|000000⟩ + |111111⟩) / √2
- Shows scalability of entanglement

---

### 🔹 5. Quantum Simulator (AerSimulator)
- Classical simulation of quantum circuits
- Used for testing quantum algorithms before hardware execution

---

### 🔹 6. State Vector Simulator
- Displays full quantum state amplitudes
- Helps understand quantum state representation

---

### 🔹 7. Theta Plus State (|+⟩ state)
- Single qubit superposition state
- Created using Hadamard gate

---

## 🧠 Tools & Technologies Used

- Python 🐍
- Qiskit ⚛️
- qBraid Cloud Platform ☁️
- VS Code 💻
- Matplotlib 📊

---

## 📊 Concepts Covered

- Quantum Superposition
- Quantum Entanglement
- Measurement in Quantum Systems
- State Vector Representation
- Quantum Circuit Simulation
- Multi-qubit GHZ States

---

## 🚀 How to Run

```bash
pip install qiskit
pip install matplotlib
pip install qiskit-aer
python bell_state.py
