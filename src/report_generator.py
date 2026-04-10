def generate_report(df):
    total = len(df)
    covered = len(df[df["Test Covered"] == "Yes"])
    coverage = (covered / total) * 100

    # Find broken requirements
    broken = df[df["Status"] == "FAIL"]

    html = f"<h1>Traceability Report</h1>"
    html += f"<h3>Coverage: {coverage:.2f}%</h3>"

    html += "<h2>All Requirements</h2>"
    html += df.to_html(index=False)

    # 🔥 NEW SECTION
    html += "<h2 style='color:red;'>Broken Requirements</h2>"

    if len(broken) > 0:
        html += broken.to_html(index=False)
    else:
        html += "<p>No broken requirements 🎉</p>"

    with open("output/report.html", "w", encoding="utf-8") as f:
        f.write(html)