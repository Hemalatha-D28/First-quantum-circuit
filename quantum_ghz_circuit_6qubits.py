from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
#Create circuit with 6 qubits and 6 classical bits
qc=QuantumCircuit(6,6)
#put first qubit into superposition
qc.h(0)
#Entangle all qubits to create GHZ state
for i in range(1,6):
 qc.cx(0,i)
#Measurement
qc.measure(range(6),range(6))
print(qc)
#Run simulator
sim=AerSimulator()
compiled_circuit=transpile(qc,sim)
result=sim.run(compiled_circuit,shots=1024).result()
#Get results
counts=result.get_counts()
print(counts)
#Plot histogram
fig=plot_histogram(counts)
plt.show()
