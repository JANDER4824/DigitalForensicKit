"""
Utilidad para extracción de cadenas de texto relevantes desde binarios/memoria.
"""

import re

def extract_strings(file_path, min_length=5):
    """
    Extrae cadenas ASCII de longitud mínima desde un archivo binario.
    """
    pattern = rb"[\x20-\x7E]{%d,}" % min_length
    with open(file_path, "rb") as f:
        data = f.read()
    return [s.decode("ascii", "ignore") for s in re.findall(pattern, data)]