code = """import pandas as pd
import json
with open(var_call_5QN77jpOE7FA1Nn31rsikxfH) as f:
    civic_docs = json.load(f)
with open(var_call_ap8UDFILoneRTWeHLiiAuxdH) as f:
    funding = json.load(f)
# Step 1: Extract disaster-related projects that started in 2022 from civic_docs
import re
disaster_projects = []
for doc in civic_docs:
    text = doc['text']
    # Find project sections that mention disaster and have indication of starting in 2022
    lines = text.split('\n')
    project_name = None
    within_disaster_section = False
    for i, line in enumerate(lines):
        # Mark Disaster section entry
        if 'Disaster Recovery Projects' in line or 'disaster' in line.lower():
            within_disaster_section = True
        if within_disaster_section:
            # Try to spot project names in this disaster section
            if 'Project' in line or 'Repair' in line or 'Improvements' in line:
                project_name = line.split('(')[0].strip()
            # Try to find 2022 in schedule phrases
            if re.search(r'2022', line):
                if project_name:
                    disaster_projects.append(project_name)
        # End of section
        if line.strip() == '' and within_disaster_section:
            within_disaster_section = False
project_names = set([p for p in disaster_projects if p])
# Step 2: Find matching projects in funding table
funding_df = pd.DataFrame(funding)
def matches_project(name):
    for p in project_names:
        if p and p in name:
            return True
    return False
filtered_funding = funding_df[funding_df['Project_Name'].apply(matches_project)]
total_funding = filtered_funding['Amount'].astype(int).sum()
print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_call_5QN77jpOE7FA1Nn31rsikxfH': 'file_storage/call_5QN77jpOE7FA1Nn31rsikxfH.json', 'var_call_ap8UDFILoneRTWeHLiiAuxdH': 'file_storage/call_ap8UDFILoneRTWeHLiiAuxdH.json'}

exec(code, env_args)
