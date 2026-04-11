from qiskit import QuantumCircuit,transpile
n=4
qc=QuantumCircuit(n,n)
qc.h(0)
for i in range(n-1):
 qc.cx(i,i+1)
qc.measure(range(n),range(n))
depth=qc.depth()
gate_count=qc.size()
num_qubits=qc.num_qubits
num_clbits=qc.num_clbits
gate_details=qc.count_ops()
print("Circuit depth:",depth)
print("Total gates:",gate_count)
print("Number of Qubits:",num_qubits)
print("Number of classical bits:",num_clbits)
print("Gate Breakdown:",gate_details)
