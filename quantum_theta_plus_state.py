from qiskit import QuantumCircuit,transpile
from qiskit_aer import Aer
#Use statevector simulator
backend=Aer.get_backend('statevector_simulator')
#Create 2-qubit circuit
qc=QuantumCircuit(2)
#step1:put a qubit 0 in superposition
qc.h(0)
#step2:Entangle qubits
qc.cx(0,1)
#Run simulation 
qc_t=transpile(qc,backend)
result=backend.run(qc_t).result()
#get quantum state
state=result.get_statevector()
print("0+(theta plus)statevector:")
print(state)
