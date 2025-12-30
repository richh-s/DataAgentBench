code = """import re, json
from pathlib import Path

# Load full funding data
funding_path = var_call_RSQfeQHpZKGwI5GeF7lfTrsj
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Load civic docs with emergency or FEMA
civic_path = var_call_taPVwOvSGkedxtaCfSSYzHY0
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

text_combined = '\n'.join(doc['text'] for doc in civic_docs)

# Build set of project names from funding that are likely emergency/FEMA related
pattern = re.compile(r'(emergency|fema)', re.I)
emergency_projects = []
for row in funding:
    name = row['Project_Name']
    if pattern.search(name) or pattern.search(text_combined) and name.lower() in text_combined.lower():
        emergency_projects.append(row)

# Also include known FEMA/CalOES/CalJPIA suffix projects
extra = []
for row in funding:
    if any(tag in row['Project_Name'] for tag in ['FEMA', 'CalOES', 'CalJPIA']):
        extra.append(row)

# Merge and deduplicate by (Project_Name, Funding_Source, Amount)
seen = set()
results = []
for row in emergency_projects + extra:
    key = (row['Project_Name'], row['Funding_Source'], row['Amount'])
    if key not in seen:
        seen.add(key)
        results.append({
            'Project_Name': row['Project_Name'],
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']) if isinstance(row['Amount'], str) and row['Amount'].isdigit() else row['Amount'],
            'Status': None
        })

# Very rough status extraction from civic text: search lines around project name
for r in results:
    name = r['Project_Name']
    # find a snippet containing the name
    idx = text_combined.lower().find(name.lower())
    status = None
    if idx != -1:
        start = max(0, idx-200)
        end = idx+200
        snippet = text_combined[start:end].lower()
        if 'completed' in snippet:
            status = 'completed'
        elif 'under construction' in snippet or 'begin construction' in snippet or 'construction' in snippet:
            status = 'design'
        elif 'not started' in snippet:
            status = 'not started'
    r['Status'] = status

result_json = json.dumps(results, indent=2)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_RSQfeQHpZKGwI5GeF7lfTrsj': 'file_storage/call_RSQfeQHpZKGwI5GeF7lfTrsj.json', 'var_call_taPVwOvSGkedxtaCfSSYzHY0': 'file_storage/call_taPVwOvSGkedxtaCfSSYzHY0.json'}

exec(code, env_args)
