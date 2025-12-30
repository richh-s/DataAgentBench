code = """import json, re
from pathlib import Path

# Load full funding data
with open(var_call_ffgQFTjFVkyj5NoCZr7Fo3Qr, 'r') as f:
    funding = json.load(f)

# Filter funding projects whose names suggest emergency/FEMA-related
emergency_keywords = ["emergency", "FEMA", "Warning", "Backup Power"]
pattern = re.compile(r"(emergency|FEMA|warning|backup power)", re.I)

relevant_funding = []
for row in funding:
    name = row.get("Project_Name", "") or ""
    if pattern.search(name):
        relevant_funding.append({
            "Project_Name": name,
            "Funding_Source": row.get("Funding_Source"),
            "Amount": int(row.get("Amount")) if row.get("Amount") not in (None, "") else None
        })

result = json.dumps(relevant_funding)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ffgQFTjFVkyj5NoCZr7Fo3Qr': 'file_storage/call_ffgQFTjFVkyj5NoCZr7Fo3Qr.json', 'var_call_IhqN4jAi9eh2ZGoHHX5lLFDt': 'file_storage/call_IhqN4jAi9eh2ZGoHHX5lLFDt.json'}

exec(code, env_args)
