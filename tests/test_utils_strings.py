from utils.strings import extract_strings

def test_extract_strings(tmp_path):
    file = tmp_path / "bin"
    file.write_bytes(b"\x00URL:http://evil.com\x00Secret123\x00")
    strings = extract_strings(str(file), min_length=5)
    assert "http://evil.com" in strings
    assert "Secret123" in strings