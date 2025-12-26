code = """import pandas as pd
import json
with open(var_call_5QN77jpOE7FA1Nn31rsikxfH) as f:
    civic_docs = json.load(f)
with open(var_call_ap8UDFILoneRTWeHLiiAuxdH) as f:
    funding = json.load(f)
import re
# Extract disaster-related projects that started in 2022
project_names = set()
for doc in civic_docs:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i]
        if 'disaster' in line.lower() and '2022' in line:
            # Try to find project name in the same line or previous few lines
            for j in range(max(0, i-3), i+1):
                prev_line = lines[j]
                if any(keyword in prev_line for keyword in ['Project', 'Repair', 'Improvements']):
                    name = prev_line.split('(')[0].split(':')[0].replace('Project','').replace('Repair','').replace('Improvements','').strip()
                    if name:
                        project_names.add(name)
funding_df = pd.DataFrame(funding)
matched = []
for name in project_names:
    records = funding_df[funding_df['Project_Name'].str.contains(name, case=False, na=False)]
    matched.extend(records.to_dict('records'))
total = sum([int(m['Amount']) for m in matched])
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_5QN77jpOE7FA1Nn31rsikxfH': 'file_storage/call_5QN77jpOE7FA1Nn31rsikxfH.json', 'var_call_ap8UDFILoneRTWeHLiiAuxdH': 'file_storage/call_ap8UDFILoneRTWeHLiiAuxdH.json'}

exec(code, env_args)
