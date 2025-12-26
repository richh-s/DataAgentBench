code = """import pandas as pd
import json
with open(var_call_5QN77jpOE7FA1Nn31rsikxfH) as f:
    civic_docs = json.load(f)
with open(var_call_ap8UDFILoneRTWeHLiiAuxdH) as f:
    funding = json.load(f)
import re
# Extract disaster-related projects from civic_docs that started in 2022
project_names = set()
for doc in civic_docs:
    text = doc['text']
    # Simple solution: just search for 'disaster' and '2022' within 3 lines of each other
    lines = text.split('\n')
    for i in range(len(lines)):
        if 'disaster' in lines[i].lower():
            # Look forward 3 lines
            for j in range(i, min(i+4, len(lines))):
                if '2022' in lines[j]:
                    # Try to extract project name (look for lines with 'Project', 'Repair', etc.)
                    for k in range(i, min(j+1, len(lines))):
                        line = lines[k]
                        if any(x in line for x in ['Project', 'Repair', 'Improvements']):
                            name = line.strip()
                            name = name.split('(')[0].split(':')[0].replace('Project','').replace('Repair','').replace('Improvements','').strip()
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
