# modules/report_exporter.py

import pandas as pd
import json
import base64
import io

def export_csv(data: pd.DataFrame, filename="summary.csv"):
    return download_button(data.to_csv(index=False), filename, "CSV")

def export_json(data: dict, filename="summary.json"):
    json_str = json.dumps(data, indent=2)
    return download_button(json_str, filename, "JSON")

def download_button(content, filename, label):
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Download {label}</a>'
    return href

