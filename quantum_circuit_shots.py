from qbraid.runtime import QbraidProvider

provider = QbraidProvider()
device = provider.get_device("qbraid:qbraid:sim:qir-sv")

# Create circuit using Qiskit
from qiskit import QuantumCircuit

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

# Submit job
job = device.run(circuit, shots=1000)
result = job.result()
print(f"Counts: {result.data.get_counts()}")
