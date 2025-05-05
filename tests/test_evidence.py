import os
from core.evidence import Evidence

def test_evidence_hash_and_audit(tmp_path):
    # Crear archivo temporal
    file = tmp_path / "test.txt"
    file.write_text("Test DigitalForensicKit")
    ev = Evidence(str(file), "test")
    assert ev.hashes["sha256"]
    assert ev.verify_integrity()
    ev.log_action("Test action", {"foo": "bar"})
    assert len(ev.get_audit_log()) >= 2