from qiskit import QuantumCircuit , QuantumRegister
from qiskit.circuit.library import HGate

qc = QuantumCircuit(1)
qc.append(
    HGate(), #Forma de criar uma porta hadamard (colocar o qubit em superposição)
    [0],
)

qc.draw("mpl")