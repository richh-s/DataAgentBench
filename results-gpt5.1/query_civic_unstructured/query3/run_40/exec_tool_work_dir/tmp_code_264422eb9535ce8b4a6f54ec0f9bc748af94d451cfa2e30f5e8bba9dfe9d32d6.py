code = """import re, json, pandas as pd

path = var_call_5j3we6F1RM2qPEfAIiGrQ4D8
with open(path, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_vggsO8EhdL1SCOR4Roi5kCgp)
funding['Amount'] = funding['Amount'].astype(int)

projects = []
skip_terms = ["agenda", "city of", "commission meeting", "item ", "subject", "recommended action", "discussion:", "project description:", "project updates:", "project schedule:", "updates:", "prepared by", "approved by"]

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for line in lines:
        if len(line) < 5:
            continue
        if not re.search('[A-Za-z]', line):
            continue
        if '.' in line:
            continue
        low = line.lower()
        if any(k in low for k in skip_terms):
            continue
        projects.append({'Project_Name': line})

proj_df = pd.DataFrame(projects).drop_duplicates().reset_index(drop=True)

merged = pd.merge(funding, proj_df, on='Project_Name', how='inner')

mask = merged['Project_Name'].str.contains('emergency', case=False) | merged['Project_Name'].str.contains('FEMA', case=False)
result = merged[mask][['Project_Name', 'Funding_Source', 'Amount']].drop_duplicates().to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vggsO8EhdL1SCOR4Roi5kCgp': 'file_storage/call_vggsO8EhdL1SCOR4Roi5kCgp.json', 'var_call_5j3we6F1RM2qPEfAIiGrQ4D8': 'file_storage/call_5j3we6F1RM2qPEfAIiGrQ4D8.json'}

exec(code, env_args)
