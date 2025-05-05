"""
Módulo central para manejo y modelado de evidencias digitales.
Incluye registro de integridad, custodia y operaciones sobre evidencias.
"""

import hashlib
import datetime
import os

class Evidence:
    """
    Clase base para modelar cualquier evidencia digital.
    """

    def __init__(self, path, evidence_type, description="", case_id=None):
        self.path = os.path.abspath(path)
        self.evidence_type = evidence_type
        self.description = description
        self.case_id = case_id
        self.created_at = datetime.datetime.utcnow()
        self.hashes = self.compute_hashes()
        self.audit_log = []
        self.log_action("Evidence created")

    def compute_hashes(self):
        """
        Calcula hashes SHA256 y MD5 para la evidencia.
        """
        hashes = {"sha256": None, "md5": None}
        if not os.path.isfile(self.path):
            return hashes
        sha256 = hashlib.sha256()
        md5 = hashlib.md5()
        with open(self.path, "rb") as f:
            while True:
                data = f.read(65536)
                if not data:
                    break
                sha256.update(data)
                md5.update(data)
        hashes["sha256"] = sha256.hexdigest()
        hashes["md5"] = md5.hexdigest()
        return hashes

    def log_action(self, action, details=None):
        """
        Registra acción sobre la evidencia (cadena de custodia).
        """
        timestamp = datetime.datetime.utcnow()
        entry = {
            "timestamp": timestamp.isoformat() + "Z",
            "action": action,
            "details": details,
        }
        self.audit_log.append(entry)

    def get_audit_log(self):
        """
        Devuelve el registro de custodia/acciones.
        """
        return self.audit_log

    def verify_integrity(self):
        """
        Verifica hashes actuales contra los iniciales.
        """
        current_hashes = self.compute_hashes()
        return current_hashes == self.hashes

    def __repr__(self):
        return (
            f"<Evidence {self.evidence_type} '{self.path}' "
            f"SHA256:{self.hashes['sha256'][:8]}...>"
        )