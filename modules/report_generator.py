"""
Módulo para integración y extensión de generación de informes.
"""

from core.report import ReportGenerator

def generate_case_report(case_name, author, findings, output_dir="reports"):
    """
    Genera reporte forense integrando hallazgos.
    """
    report = ReportGenerator(case_name, author, output_dir)
    for section in findings:
        report.add_section(section["title"], section["content"])
    pdf_path = report.generate_pdf(f"{case_name}_forensic_report.pdf")
    html_path = report.generate_html(f"{case_name}_forensic_report.html")
    json_path = report.generate_json(f"{case_name}_forensic_report.json")
    return {"pdf": pdf_path, "html": html_path, "json": json_path}