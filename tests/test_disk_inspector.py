from modules.disk_inspector import DiskInspector

def test_disk_inspector_initialization(tmp_path):
    file = tmp_path / "test.img"
    file.write_bytes(b"\x00" * 4096)
    inspector = DiskInspector(str(file), "CASE2")
    assert inspector.evidence.path == str(file)