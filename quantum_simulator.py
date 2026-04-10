from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
#Create quantum circuit with two qubits 
qc=QuantumCircuit(2,2)
#Apply Gates
qc.h(0)    #Hadamard Gate
qc.cx(0,1) #CNOT Gate
#Measurement
qc.measure([0,1],[0,1])
#Use Aer Simulator
simulator=Aer.get_backend('qasm_simulator')
#Transpile Circuit
compiled_circuit=transpile(qc,simulator)
#Run Simulation
job=simulator.run(compiled_circuit,shots=1024)
#Get result
result=job.result()
counts=result.get_counts()
print(counts)
