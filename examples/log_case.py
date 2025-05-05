"""
Ejemplo de análisis de logs con DigitalForensicKit.
"""

from modules.log_parser import LogParser

def main():
    logs = ["examples/syslog.log", "examples/apache.log"]
    parser = LogParser(logs)
    print("Eventos:", parser.parse_logs())
    print("Anomalías:", parser.detect_anomalies())

if __name__ == "__main__":
    main()