code = """import re, json
from pathlib import Path

funding_path = var_call_RSQfeQHpZKGwI5GeF7lfTrsj
with open(funding_path, 'r') as f:
    funding = json.load(f)

civic_path = var_call_taPVwOvSGkedxtaCfSSYzHY0
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

text_combined = '\n'.join(doc['text'] for doc in civic_docs)

pattern = re.compile(r'(emergency|fema)', re.I)
emergency_projects = []
for row in funding:
    name = row['Project_Name']
    if pattern.search(name) or (pattern.search(text_combined) and name.lower() in text_combined.lower()):
        emergency_projects.append(row)

extra = []
for row in funding:
    if any(tag in row['Project_Name'] for tag in ['FEMA', 'CalOES', 'CalJPIA']):
        extra.append(row)

seen = set()
results = []
for row in emergency_projects + extra:
    key = (row['Project_Name'], row['Funding_Source'], row['Amount'])
    if key not in seen:
        seen.add(key)
        amount = row['Amount']
        if isinstance(amount, str) and amount.isdigit():
            amount = int(amount)
        results.append({
            'Project_Name': row['Project_Name'],
            'Funding_Source': row['Funding_Source'],
            'Amount': amount,
            'Status': None
        })

for r in results:
    name = r['Project_Name']
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
