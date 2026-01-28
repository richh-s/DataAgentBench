code = """import json
import pandas as pd

# Load data
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract projects with emergency/FEMA from documents
projects = []
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'fema' in text or 'emergency' in text or 'warning' in text:
        # Split into lines to find project names
        lines = doc.get('text', '').split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 5 and len(line) < 120 and (line.istitle() or 'Project' in line):
                # Check if line likely describes a project
                if any(kw in line for kw in ['Project', 'Improvement', 'Repair', 'Replacement']):
                    if 'fema' in line.lower() or 'emergency' in line.lower():
                        info = {'Project_Name': line}
                        # Look at context for status
                        context = ' '.join(lines[:20]).lower()
                        if 'design' in context:
                            info['status'] = 'design'
                        elif 'construction' in context:
                            info['status'] = 'construction'
                        elif 'completed' in context:
                            info['status'] = 'completed'
                        projects.append(info)

# Find relevant funding
funding_df = pd.DataFrame(funding_data)
keywords = ['fema', 'emergency', 'warning']

results = []
for _, fund in funding_df.iterrows():
    proj_name = fund['Project_Name'].lower()
    if any(kw in proj_name for kw in keywords):
        # Find status
        status = 'Unknown'
        for proj in projects:
            if proj['Project_Name'].lower() in proj_name or proj_name in proj['Project_Name'].lower():
                status = proj.get('status', 'Unknown')
                break
        results.append({
            'Project_Name': fund['Project_Name'],
            'Funding_Source': fund['Funding_Source'],
            'Amount': int(fund['Amount']),
            'Status': status
        })

# Output
output = sorted(results, key=lambda x: x['Project_Name'])
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
