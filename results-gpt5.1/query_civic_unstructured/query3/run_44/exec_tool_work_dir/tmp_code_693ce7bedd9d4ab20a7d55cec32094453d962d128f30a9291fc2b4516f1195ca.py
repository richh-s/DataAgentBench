code = """import re, json
from pathlib import Path
import pandas as pd

funding_records = var_call_7GbNZcNwglJo17NnQO4dUEtr
civic_path = Path(var_call_hjwztXzN4kChBJE271ucnpJn)

with open(civic_path, 'r') as f:
    civic_records = json.load(f)

emergency_projects = set()

for doc in civic_records:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        if re.search(r'(emergency|FEMA)', line_stripped, re.IGNORECASE):
            if len(line_stripped) < 120 and not line_stripped.endswith((':', ';')):
                emergency_projects.add(line_stripped)

funding_df = pd.DataFrame(funding_records)

matches = []
for proj in emergency_projects:
    for pname, fsrc, amt in funding_df[['Project_Name', 'Funding_Source', 'Amount']].itertuples(index=False):
        if proj.lower() in pname.lower() or pname.lower() in proj.lower():
            matches.append({
                'Project_Name': pname,
                'Funding_Source': fsrc,
                'Amount': int(amt),
                'Matched_From_Text': proj
            })

unique = {}
for m in matches:
    key = (m['Project_Name'], m['Funding_Source'], m['Amount'])
    if key not in unique:
        unique[key] = m

result = list(unique.values())
result_sorted = sorted(result, key=lambda x: x['Project_Name'])

print("__RESULT__:")
print(json.dumps(result_sorted))"""

env_args = {'var_call_7GbNZcNwglJo17NnQO4dUEtr': 'file_storage/call_7GbNZcNwglJo17NnQO4dUEtr.json', 'var_call_hjwztXzN4kChBJE271ucnpJn': 'file_storage/call_hjwztXzN4kChBJE271ucnpJn.json'}

exec(code, env_args)
