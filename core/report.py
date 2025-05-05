"""
Módulo central para la generación de informes forenses.
Soporta PDF, HTML y JSON, e integración de hallazgos.
"""

import os
import json
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from jinja2 import Environment, FileSystemLoader

class ReportGenerator:
    """
    Clase principal para generar informes forenses.
    """

    def __init__(self, case_name, author, output_dir="reports"):
        self.case_name = case_name
        self.author = author
        self.created_at = datetime.datetime.utcnow()
        self.output_dir = output_dir
        self.sections = []
        os.makedirs(output_dir, exist_ok=True)

    def add_section(self, title, content):
        self.sections.append({"title": title, "content": content})

    def _timestamp(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S UTC")

    def generate_pdf(self, filename, evidence_hashes=None):
        path = os.path.join(self.output_dir, filename)
        pdf = canvas.Canvas(path, pagesize=A4)
        width, height = A4
        pdf.setTitle(self.case_name)
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, height - 50, f"Informe Forense: {self.case_name}")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(50, height - 70, f"Autor: {self.author}")
        pdf.drawString(50, height - 85, f"Fecha: {self._timestamp()}")
        if evidence_hashes:
            pdf.drawString(50, height - 100, f"Evidencia: {evidence_hashes}")
        y = height - 130
        for section in self.sections:
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(50, y, section["title"])
            y -= 18
            pdf.setFont("Helvetica", 10)
            for line in section["content"].splitlines():
                pdf.drawString(50, y, line)
                y -= 14
                if y < 60:
                    pdf.showPage()
                    y = height - 60
        pdf.save()
        return path

    def generate_html(self, filename):
        env = Environment(loader=FileSystemLoader("docs/templates"))
        template = env.get_template("report.html")
        html = template.render(
            case_name=self.case_name,
            author=self.author,
            created_at=self._timestamp(),
            sections=self.sections
        )
        path = os.path.join(self.output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        return path

    def generate_json(self, filename):
        data = {
            "case_name": self.case_name,
            "author": self.author,
            "created_at": self._timestamp(),
            "sections": self.sections,
        }
        path = os.path.join(self.output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return path

    def export_IOCs(self, ioc_list, fmt="stix", filename="iocs.xml"):
        # Exportar IOCs en STIX/OpenIOC (simplificado)
        path = os.path.join(self.output_dir, filename)
        if fmt == "stix":
            with open(path, "w") as f:
                f.write("<STIX_Package>\n")
                for ioc in ioc_list:
                    f.write(f"  <Indicator>{ioc}</Indicator>\n")
                f.write("</STIX_Package>\n")
        elif fmt == "openioc":
            with open(path, "w") as f:
                f.write("<OpenIOC>\n")
                for ioc in ioc_list:
                    f.write(f"  <IndicatorItem>{ioc}</IndicatorItem>\n")
                f.write("</OpenIOC>\n")
        return path