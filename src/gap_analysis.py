def analyze_gaps(controls_df, app_controls):
    implemented = [c["id"] for c in app_controls["controls"] if c["implemented"]]
    total = len(controls_df)
    compliant = sum(1 for cid in implemented if cid in controls_df["Control ID"].values)
    compliance_pct = round((compliant / total) * 100, 1)
    gaps = [row["Control ID"] for _, row in controls_df.iterrows() if row["Control ID"] not in implemented]
    return compliance_pct, gaps
