from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
#Create 2-qubit circuit
qc=QuantumCircuit(2)
#step1:Put a qubit 0 in Superposition
qc.h(0)    #Hadamard gate
#step2:Entangle qubits
qc.cx(0,1) #CNOT Gate
#Draw the quantum circuit diagram
qc.draw("mpl")
#Dispaly the circuit visualization
plt.show()
