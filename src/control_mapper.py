import pandas as pd
import json
from gap_analysis import analyze_gaps
from risk_report import generate_report

controls_df = pd.read_csv("data/nist_800_171_controls.csv")
with open("data/mock_app_controls.json") as f:
    app_controls = json.load(f)

compliance, gaps = analyze_gaps(controls_df, app_controls)
generate_report(compliance, gaps)
print(f"Compliance report generated: {compliance}% compliance")
