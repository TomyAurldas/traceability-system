from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():
    df = pd.read_csv("output/traceability.csv")

    total = len(df)
    passed = len(df[df["Status"] == "PASS"])
    failed = len(df[df["Status"] == "FAIL"])
    coverage = (len(df[df["Test Covered"] == "Yes"]) / total) * 100

    broken = df[df["Status"] == "FAIL"]

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Traceability Dashboard</title>

        <!-- Chart.js -->
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

        <!-- Icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

        <style>
            body {{
                font-family: 'Segoe UI', sans-serif;
                background: #f4f6f9;
                padding: 20px;
            }}

            h1 {{
                text-align: center;
                color: #2c3e50;
            }}

            /* Cards Layout */
            .cards {{
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
                margin-top: 20px;
            }}

            .card {{
                background: white;
                padding: 20px;
                margin: 10px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                flex: 1;
                min-width: 200px;
                text-align: center;
            }}

            .card i {{
                font-size: 30px;
                margin-bottom: 10px;
            }}

            .total {{ color: #3498db; }}
            .pass {{ color: #2ecc71; }}
            .fail {{ color: #e74c3c; }}

            table {{
                border-collapse: collapse;
                width: 100%;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: center;
            }}

            th {{
                background-color: #3498db;
                color: white;
            }}

            /* Chart container fix */
            .chart-container {{
                width: 350px;
                height: 350px;
                margin: auto;
            }}

        </style>
    </head>

    <body>

    <h1> Traceability Dashboard</h1>

    <!-- 🔥 DASHBOARD CARDS -->
    <div class="cards">
        <div class="card total">
            <i class="fas fa-list"></i>
            <h3>Total Stories</h3>
            <h2>{total}</h2>
        </div>

        <div class="card pass">
            <i class="fas fa-check-circle"></i>
            <h3>Passed</h3>
            <h2>{passed}</h2>
        </div>

        <div class="card fail">
            <i class="fas fa-times-circle"></i>
            <h3>Failed</h3>
            <h2>{failed}</h2>
        </div>

        <div class="card total">
            <i class="fas fa-chart-pie"></i>
            <h3>Coverage</h3>
            <h2>{coverage:.2f}%</h2>
        </div>
    </div>

    <!--  PIE CHART -->
    <div class="card">
        <h2> Test Results Overview</h2>
        <div class="chart-container">
            <canvas id="myChart"></canvas>
        </div>
    </div>

    <!-- TABLE -->
    <div class="card">
        <h2> All Requirements</h2>
        {df.to_html(index=False)}
    </div>

    <!-- BROKEN -->
    <div class="card">
        <h2 style="color:#e74c3c;"> Broken Requirements</h2>
        {broken.to_html(index=False) if len(broken) > 0 else "<p>No broken requirements 🎉</p>"}
    </div>

    <script>
        var ctx = document.getElementById('myChart').getContext('2d');
        var chart = new Chart(ctx, {{
            type: 'pie',
            data: {{
                labels: ['PASS', 'FAIL'],
                datasets: [{{
                    data: [{passed}, {failed}],
                    backgroundColor: ['#2ecc71', '#e74c3c']
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
    </script>

    </body>
    </html>
    """

    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)