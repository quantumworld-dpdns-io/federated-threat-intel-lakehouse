# Quantum Computing Integration

## Overview

The FTIL quantum module provides quantum-enhanced threat detection capabilities.

## Components

### Qiskit Engine
- Circuit execution on IBM Quantum backends
- Error mitigation and noise simulation
- Variational quantum classifiers for IoC classification

### CUDA-Q
- GPU-accelerated quantum simulation
- Hybrid quantum-classical execution
- Custom kernels for threat scoring

### Post-Quantum Cryptography
- **CRYSTALS-Kyber**: Key encapsulation
- **CRYSTALS-Dilithium**: Digital signatures
- **SPHINCS+**: Hash-based signatures
- PQC migration toolkit

### Zero-Knowledge Proofs
- **Noir**: ZK circuit DSL for IoC provenance
- **RISC Zero**: zkVM for verifiable computation
- Proof verification service

### Quantum Key Distribution
- BB84 protocol implementation
- Quantum random number generation

## Usage

```python
from src.quantum.circuits.ioc_classifier import QuantumIoCClassifier

classifier = QuantumIoCClassifier(num_qubits=4)
circuit = classifier.build_circuit(features)
result = classifier.classify(counts)
```
