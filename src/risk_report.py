from weasyprint import HTML

def generate_report(compliance, gaps):
    html_content = f"""
    <h1>NIST 800-171 Compliance Report</h1>
    <p>Compliance: {compliance}%</p>
    <p>Gaps: {', '.join(gaps)}</p>
    """
    with open("output/compliance_report.html", "w") as f:
        f.write(html_content)
    HTML(string=html_content).write_pdf("output/compliance_report.pdf")
