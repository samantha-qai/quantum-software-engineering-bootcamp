from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

qr = QuantumRegister(2)
cr = ClassicalRegister(2)

qc = QuantumCircuit(qr, cr)

qc.h(0)
qc.x(qr)
qc.h(qr)
qc.cx(0, 1)
qc.h(qr)

qc.measure(qr, cr)

aer = AerSimulator()
counts = aer.run(qc).result().get_counts()

plot_histogram(counts, title="Reverse CNOT", filename="test.png")
