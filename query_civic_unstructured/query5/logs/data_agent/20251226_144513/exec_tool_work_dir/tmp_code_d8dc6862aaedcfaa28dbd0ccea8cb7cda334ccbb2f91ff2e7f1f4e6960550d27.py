code = """import pandas as pd
import json
with open(var_call_5QN77jpOE7FA1Nn31rsikxfH) as f:
    civic_docs = json.load(f)
with open(var_call_ap8UDFILoneRTWeHLiiAuxdH) as f:
    funding = json.load(f)
import re
disaster_projects = set()
for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_type = None
    current_name = None
    for i, line in enumerate(lines):
        low_line = line.lower()
        # Identify section if it is disaster related
        if 'disaster recovery projects' in low_line or 'disaster project' in low_line:
            current_type = 'disaster'
        if current_type == 'disaster':
            # Find project name candidates (look for lines with the word Project/Repair/Improvements)
            if ('project' in low_line or 'repair' in low_line or 'improvements' in low_line) and not low_line.startswith('subject'):
                parts = line.split('(')[0].split(':')[0].strip()
                current_name = parts
            # Find start time indication
            if '2022' in line and current_name:
                # Add to set
                disaster_projects.add(current_name)
        # Reset at new section or blank
        if line.strip() == '' and current_type == 'disaster':
            current_type = None
            current_name = None
# Step 2: Find funding records for these projects
funding_df = pd.DataFrame(funding)
matched = []
for p in disaster_projects:
    matched.extend(funding_df[funding_df['Project_Name'].str.contains(p, case=False, na=False)].to_dict('records'))
# Step 3: Total funding
if matched:
    total = sum([int(m['Amount']) for m in matched])
else:
    total = 0
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_5QN77jpOE7FA1Nn31rsikxfH': 'file_storage/call_5QN77jpOE7FA1Nn31rsikxfH.json', 'var_call_ap8UDFILoneRTWeHLiiAuxdH': 'file_storage/call_ap8UDFILoneRTWeHLiiAuxdH.json'}

exec(code, env_args)
