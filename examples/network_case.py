"""
Ejemplo de análisis de captura de red con DigitalForensicKit.
"""

from modules.network_forensics import NetworkForensics

def main():
    pcap_path = "examples/network.pcap"
    nf = NetworkForensics(pcap_path)
    print("Sesiones:", nf.analyze_sessions())
    print("Anomalías:", nf.detect_anomalies())

if __name__ == "__main__":
    main()