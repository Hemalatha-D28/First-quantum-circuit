from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
#Create a quantum circuit with 3 qubits
qc=QuantumCircuit(3,3)
#Apply Hadamard gate on first qubit
qc.h(0)
#Apply CNOT gate from qubit 0 to qubit 1
qc.cx(0,1)
#Apply CNOT gate from qubit 0 to qubit 2
qc.cx(0,2)
#Measure all qubits
#convert quantum state into classical bits
qc.measure([0,1,2],[0,1,2])
#Run the quantum circuit on the simulator
sim=AerSimulator()
result=sim.run(qc,shots=1024).result()
#Get counts
counts=result.get_counts()
print(counts)
