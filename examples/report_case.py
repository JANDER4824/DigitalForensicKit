"""
Ejemplo de generación de informe forense con DigitalForensicKit.
"""

from modules.report_generator import generate_case_report

def main():
    case = "CasoDemo"
    author = "Perito Digital"
    findings = [
        {"title": "Resumen", "content": "Caso de ejemplo con hallazgos de memoria, disco y red."},
        {"title": "IOCs", "content": "IP maliciosa: 1.2.3.4\nProceso sospechoso: malware.exe"}
    ]
    paths = generate_case_report(case, author, findings)
    print("Informe generado en:", paths)

if __name__ == "__main__":
    main()