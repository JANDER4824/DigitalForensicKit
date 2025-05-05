"""
Ejemplo de análisis de volcado de memoria con DigitalForensicKit.
"""

from modules.memory_analyzer import MemoryDumpAnalyzer

def main():
    dump_path = "examples/memdump.raw"
    profile = "Win10x64"
    analyzer = MemoryDumpAnalyzer(dump_path, profile)
    print("Procesos activos:", analyzer.analyze_processes())
    print("IOCs detectados:", analyzer.extract_iocs())
    print("Conexiones de red:", analyzer.extract_network_connections())

if __name__ == "__main__":
    main()