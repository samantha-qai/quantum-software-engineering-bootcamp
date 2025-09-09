from datetime import datetime
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def log_time(func):
    def wrapper():
        now = datetime.now()
        print("Program started at", now)
        func_return = func()
        now = datetime.now()
        print("Program ended at", now)
        return func_return

    return wrapper

@log_time
def run_qc():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.measure_all()
    simulator = AerSimulator()
    result = simulator.run(qc).result()
    counts = result.get_counts(qc)
    return counts

if __name__ == 'main':
    run_qc()
