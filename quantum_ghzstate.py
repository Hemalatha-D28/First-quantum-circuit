from qiskit import QuantumCircuit

def ghz_circuit(n):
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(n - 1):
        qc.cx(i, i + 1)
    return qc
for n in range(2, 7):   # from 2 to 6 qubits
    print(f"\nGHZ Circuit for {n} qubits:\n")
    qc = ghz_circuit(n)
    print(qc.draw())
