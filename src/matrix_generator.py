import pandas as pd
import json
from src.parser import extract_test_mapping

def load_results():
    with open("ci_results/results.json") as f:
        return json.load(f)

def generate_matrix(stories):
    results = load_results()
    mapping = extract_test_mapping()   # 🔥 AUTO mapping

    data = []

    for story in stories:
        sid = story['id']

        if sid in mapping:
            covered = "Yes"
            test_name = mapping[sid]
            status = results.get(test_name, "UNKNOWN")
        else:
            covered = "No"
            status = "NO TEST ❌"

        data.append([sid, covered, status])

    df = pd.DataFrame(data, columns=["Story ID", "Test Covered", "Status"])
    df.to_csv("output/traceability.csv", index=False)

    return df