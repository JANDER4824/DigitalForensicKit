from modules.memory_analyzer import MemoryDumpAnalyzer

def test_memory_analyzer_initialization(tmp_path):
    file = tmp_path / "mem.raw"
    file.write_bytes(b"\x00" * 4096)
    analyzer = MemoryDumpAnalyzer(str(file), "Win10x64", "CASE1")
    assert analyzer.evidence.path == str(file)
    assert analyzer.profile == "Win10x64"