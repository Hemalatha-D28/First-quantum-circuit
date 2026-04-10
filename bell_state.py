from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
qc=QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
qc.draw("mpl")
plt.show()
