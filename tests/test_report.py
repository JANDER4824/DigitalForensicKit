from core.report import ReportGenerator

def test_report_generation(tmp_path):
    r = ReportGenerator("CasoTest", "Tester", str(tmp_path))
    r.add_section("Sumario", "Hallazgos de prueba.")
    pdf = r.generate_pdf("test.pdf")
    html = r.generate_html("test.html")
    jsn = r.generate_json("test.json")
    assert pdf.endswith(".pdf") and html.endswith(".html") and jsn.endswith(".json")