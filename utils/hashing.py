"""
Utilidad para cálculo de hashes criptográficos.
"""

import hashlib

def compute_file_hash(path, algo="sha256"):
    """
    Calcula el hash de un archivo con el algoritmo dado.
    """
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            h.update(data)
    return h.hexdigest()