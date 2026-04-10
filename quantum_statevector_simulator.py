from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
#Create quantum circuit with 2 qubits
qc=QuantumCircuit(2)
#Apply gates
qc.h(0)
qc.cx(0,1)
#Use Aer Simulator
backend=Aer.get_backend('statevector_simulator')
#Transpile circuit
qc_t=transpile(qc,backend)
#Run Simulation
job=backend.run(qc_t)
#Get result
result=job.result()
statevector=result.get_statevector()
print("statevector:",statevector)
