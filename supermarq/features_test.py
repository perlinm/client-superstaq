# pylint: disable=missing-function-docstring
import cirq

import supermarq as sm

CIRCUIT = cirq.Circuit(
    cirq.SWAP(*cirq.LineQubit.range(2)),
    cirq.measure(cirq.LineQubit(0)),
    cirq.reset(cirq.LineQubit(0)),
    cirq.measure(*cirq.LineQubit.range(2)),
)


def test_compute_communication() -> None:
    feature = sm.features.compute_communication(CIRCUIT)
    assert feature >= 0 and feature <= 1


def test_compute_liveness() -> None:
    feature = sm.features.compute_liveness(CIRCUIT)
    assert feature >= 0 and feature <= 1


def test_compute_parallelism() -> None:
    feature = sm.features.compute_parallelism(CIRCUIT)
    assert feature >= 0 and feature <= 1


def test_compute_measurement() -> None:
    feature = sm.features.compute_measurement(CIRCUIT)
    assert feature >= 0 and feature <= 1


def test_compute_entanglement() -> None:
    feature = sm.features.compute_entanglement(CIRCUIT)
    assert feature >= 0 and feature <= 1


def test_compute_depth() -> None:
    qubits = cirq.LineQubit.range(4)
    test_circuit = cirq.Circuit(
        cirq.CX(qubits[0], qubits[1]),
        cirq.CZ(qubits[2], qubits[3]),
        cirq.CX(qubits[1], qubits[2]),
        cirq.CX(qubits[2], qubits[3]),
    )
    test_feature = sm.features.compute_depth(test_circuit)
    assert test_feature >= 0 and test_feature <= 1

    assert sm.features.compute_depth(cirq.Circuit()) == 0
