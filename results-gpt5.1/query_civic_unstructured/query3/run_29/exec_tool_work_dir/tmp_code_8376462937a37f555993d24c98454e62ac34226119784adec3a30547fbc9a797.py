code = """import json, re
from pathlib import Path

# Load full funding data
funding_path = var_call_zybMRjcLAHZOtOwKgTYa5Lol
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Filter funding projects whose names suggest FEMA or emergency-related
emergency_keywords = ['fema', 'emergency', 'warning', 'backup power']
related = []
for row in funding:
    name = row.get('Project_Name', '') or ''
    lname = name.lower()
    if any(k in lname for k in emergency_keywords):
        related.append({
            'Project_Name': row['Project_Name'],
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']) if isinstance(row['Amount'], str) and row['Amount'].isdigit() else row['Amount']
        })

result = json.dumps(related)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_zybMRjcLAHZOtOwKgTYa5Lol': 'file_storage/call_zybMRjcLAHZOtOwKgTYa5Lol.json', 'var_call_FptLvhXG7Za30TLJ6MpvkEyQ': 'file_storage/call_FptLvhXG7Za30TLJ6MpvkEyQ.json'}

exec(code, env_args)
