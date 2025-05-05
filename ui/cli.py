"""
Interfaz de línea de comandos para DigitalForensicKit.
"""

import argparse
import sys
from modules.memory_analyzer import MemoryDumpAnalyzer
from modules.disk_inspector import DiskInspector
from modules.network_forensics import NetworkForensics
from modules.log_parser import LogParser
from modules.report_generator import generate_case_report

def main():
    parser = argparse.ArgumentParser(
        description="DigitalForensicKit CLI - Herramienta de análisis forense digital"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Memory
    mem_parser = subparsers.add_parser("memory", help="Análisis de memoria RAM")
    mem_parser.add_argument("--analyze", action="store_true", help="Analizar volcado de memoria")
    mem_parser.add_argument("--input", required=True, help="Archivo de volcado de memoria")
    mem_parser.add_argument("--profile", required=True, help="Perfil SO (ej: Win10x64)")
    mem_parser.add_argument("--case", help="ID del caso")

    # Disk
    disk_parser = subparsers.add_parser("disk", help="Análisis de disco")
    disk_parser.add_argument("--inspect", action="store_true", help="Inspeccionar imagen de disco")
    disk_parser.add_argument("--input", required=True, help="Archivo de imagen de disco")
    disk_parser.add_argument("--case", help="ID del caso")

    # Network
    net_parser = subparsers.add_parser("network", help="Análisis de red (PCAP)")
    net_parser.add_argument("--analyze", action="store_true", help="Analizar captura de red")
    net_parser.add_argument("--input", required=True, help="Archivo PCAP")
    net_parser.add_argument("--case", help="ID del caso")

    # Logs
    logs_parser = subparsers.add_parser("logs", help="Análisis de logs")
    logs_parser.add_argument("--parse", action="store_true", help="Parsear logs")
    logs_parser.add_argument("--input", required=True, nargs="+", help="Archivo(s) de logs")
    logs_parser.add_argument("--case", help="ID del caso")

    # Report
    report_parser = subparsers.add_parser("report", help="Generar informe")
    report_parser.add_argument("--generate", action="store_true", help="Generar informe")
    report_parser.add_argument("--case", required=True, help="Nombre del caso")
    report_parser.add_argument("--author", required=True, help="Autor del informe")

    args = parser.parse_args()

    if args.command == "memory" and args.analyze:
        analyzer = MemoryDumpAnalyzer(args.input, args.profile, args.case)
        print("Analizando procesos activos...")
        processes = analyzer.analyze_processes()
        print("Procesos encontrados:", processes)
        print("Extrayendo IOCs...")
        iocs = analyzer.extract_iocs()
        print("IOCs:", iocs)

    elif args.command == "disk" and args.inspect:
        inspector = DiskInspector(args.input, args.case)
        print("Listando archivos raíz...")
        files = inspector.list_files("/")
        print(files)

    elif args.command == "network" and args.analyze:
        netf = NetworkForensics(args.input, args.case)
        print("Analizando sesiones...")
        sessions = netf.analyze_sessions()
        print("Sesiones:", sessions)

    elif args.command == "logs" and args.parse:
        parser = LogParser(args.input, args.case)
        print("Parseando logs...")
        events = parser.parse_logs()
        print("Eventos:", events)

    elif args.command == "report" and args.generate:
        findings = [
            {"title": "Resumen", "content": "Hallazgos principales del caso."}
            # Agregar más secciones según análisis
        ]
        paths = generate_case_report(args.case, args.author, findings)
        print("Informe generado:", paths)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()