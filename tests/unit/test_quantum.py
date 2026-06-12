import pytest

from src.quantum.circuits.ioc_classifier import QuantumIoCClassifier
from src.quantum.circuits.anomaly_detector import QuantumAnomalyDetector
from src.quantum.circuits.key_gen import QuantumKeyDistribution, QuantumRandomNumberGenerator
from src.quantum.algorithms.grover import GroverSearch
from src.quantum.algorithms.quantum_ml import VariationalQuantumClassifier, QuantumKernelEstimation
from src.quantum.algorithms.error_correction import BitFlipCode, PhaseFlipCode, ShorCode, SurfaceCode
from src.quantum.pqc.liboqs import PQCKeyEncapsulation, PQCSignatures
from src.quantum.pqc.key_exchange import PQCKeyExchange
from src.quantum.zkp.verifier import ZKProofVerifier
from src.quantum.threat_detection.quantum_classifier import QuantumThreatClassifier
from src.quantum.threat_detection.quantum_anomaly import QuantumAnomalyDetection
from src.quantum.threat_detection.quantum_similarity import QuantumSimilaritySearch


class TestQuantumIoCClassifier:
    def test_build_circuit(self):
        qc = QuantumIoCClassifier(num_qubits=4)
        circuit = qc.build_circuit([0.1, 0.2, 0.3, 0.4])
        assert circuit["num_qubits"] == 4
        assert len(circuit["gates"]) > 0

    def test_classify(self):
        qc = QuantumIoCClassifier()
        result = qc.classify({"0000": 800, "1111": 200})
        assert result["class"] in [0, 1]
        assert 0 <= result["confidence"] <= 1


class TestGroverSearch:
    def test_search_space(self):
        gs = GroverSearch(num_qubits=4)
        assert gs.search_space_size() == 16
        assert gs.optimal_iterations() > 0

    def test_speedup(self):
        gs = GroverSearch(num_qubits=8)
        assert gs.speedup_vs_classical() > 1


class TestErrorCorrection:
    def test_bit_flip(self):
        bf = BitFlipCode()
        encoded = bf.encode(0)
        assert encoded == [0, 0, 0]
        corrected = bf.correct([0, 1, 0])
        assert corrected == [0, 0, 0]

    def test_shor_code(self):
        sc = ShorCode()
        encoded = sc.encode(1)
        assert len(encoded) == 3
        assert all(len(b) == 3 for b in encoded)


class TestPQC:
    def test_kem_keygen(self):
        kem = PQCKeyEncapsulation()
        keys = kem.generate_keypair()
        assert "public_key" in keys
        assert "secret_key" in keys

    def test_kem_encapsulate(self):
        kem = PQCKeyEncapsulation()
        keys = kem.generate_keypair()
        result = kem.encapsulate(keys["public_key"])
        assert "ciphertext" in result
        assert "shared_secret" in result

    def test_signatures(self):
        sig = PQCSignatures()
        keys = sig.generate_keypair()
        signature = sig.sign(b"test message", keys["secret_key"])
        assert sig.verify(b"test message", signature, keys["public_key"])

    def test_key_exchange(self):
        kex = PQCKeyExchange()
        init = kex.initiate()
        respond = kex.respond(init["public_key"])
        assert "ciphertext" in respond


class TestZKP:
    def test_verify_proof(self):
        verifier = ZKProofVerifier()
        result = verifier.verify_proof({"proof": "data"}, {"public": "input"})
        assert result["valid"] is True

    def test_batch_verify(self):
        verifier = ZKProofVerifier()
        result = verifier.batch_verify([{"proof": "a"}, {"proof": "b"}])
        assert result["total"] == 2
        assert result["valid"] == 2


class TestQuantumThreatDetection:
    def test_classifier(self):
        qc = QuantumThreatClassifier()
        result = qc.classify([0.8, 0.9, 0.7, 0.6])
        assert result["threat_level"] in ["low", "medium", "high"]

    def test_anomaly_detection(self):
        qad = QuantumAnomalyDetection()
        result = qad.detect_network_anomaly([1.0, 1.0, 1.0, 100.0])
        assert "anomaly_score" in result

    def test_similarity(self):
        qss = QuantumSimilaritySearch()
        sim = qss.ioc_similarity([1.0, 0.0, 0.0], [1.0, 0.0, 0.0])
        assert sim == 1.0

    def test_qkd(self):
        qkd = QuantumKeyDistribution(key_length=128)
        result = qkd.bb84_protocol()
        assert "key" in result
        assert result["security"] == "information_theoretic"

    def test_qrng(self):
        qrng = QuantumRandomNumberGenerator(256)
        result = qrng.generate()
        assert result["entropy"] == "quantum"
        assert len(result["random_bytes"]) == 64
