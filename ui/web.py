"""
Interfaz web básica para DigitalForensicKit usando Flask.
"""

from flask import Flask, request, render_template, send_file
import os
from modules.memory_analyzer import MemoryDumpAnalyzer
from modules.disk_inspector import DiskInspector
from modules.network_forensics import NetworkForensics
from modules.log_parser import LogParser
from modules.report_generator import generate_case_report

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/memory", methods=["POST"])
def memory_analysis():
    file = request.files["dump"]
    profile = request.form["profile"]
    case = request.form.get("case", None)
    path = os.path.join("/tmp", file.filename)
    file.save(path)
    analyzer = MemoryDumpAnalyzer(path, profile, case)
    processes = analyzer.analyze_processes()
    iocs = analyzer.extract_iocs()
    return render_template(
        "memory_result.html", processes=processes, iocs=iocs, case=case
    )

@app.route("/disk", methods=["POST"])
def disk_analysis():
    file = request.files["image"]
    case = request.form.get("case", None)
    path = os.path.join("/tmp", file.filename)
    file.save(path)
    inspector = DiskInspector(path, case)
    files = inspector.list_files("/")
    return render_template("disk_result.html", files=files, case=case)

@app.route("/network", methods=["POST"])
def network_analysis():
    file = request.files["pcap"]
    case = request.form.get("case", None)
    path = os.path.join("/tmp", file.filename)
    file.save(path)
    netf = NetworkForensics(path, case)
    sessions = netf.analyze_sessions()
    return render_template("network_result.html", sessions=sessions, case=case)

@app.route("/logs", methods=["POST"])
def logs_analysis():
    files = request.files.getlist("logs")
    case = request.form.get("case", None)
    paths = []
    for file in files:
        p = os.path.join("/tmp", file.filename)
        file.save(p)
        paths.append(p)
    parser = LogParser(paths, case)
    events = parser.parse_logs()
    return render_template("logs_result.html", events=events, case=case)

@app.route("/report", methods=["POST"])
def generate_report():
    case = request.form["case"]
    author = request.form["author"]
    # findings deben ser recolectados de análisis previos
    findings = [{"title": "Resumen", "content": "Hallazgos principales del caso."}]
    paths = generate_case_report(case, author, findings)
    return render_template("report_result.html", paths=paths, case=case)

@app.route("/download/<path:filename>")
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)