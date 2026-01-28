code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs result
path = var_call_5j3we6F1RM2qPEfAIiGrQ4D8
with open(path, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_vggsO8EhdL1SCOR4Roi5kCgp)
funding['Amount'] = funding['Amount'].astype(int)

# Simple project record extraction: look for lines that seem like project headings
projects = []
for doc in civic_docs:
    text = doc['text']
    # split into lines
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for line in lines:
        # candidate project line: not too short, has letters, and Title Case-ish
        if len(line) < 5:
            continue
        if not re.search(r'[A-Za-z]', line):
            continue
        # Heuristic: treat lines that are not sentences (no period) as project names
        if '.' in line:
            continue
        # Filter out obvious non-project headers
        if any(k in line.lower() for k in ['agenda', 'city of', 'commission meeting', 'item ', 'subject', 'recommended action', 'discussion:', 'project description:', 'project updates:', 'project schedule:', 'updates:', 'prepared by', 'approved by']):
            continue
        projects.append({'Project_Name': line})

proj_df = pd.DataFrame(projects).drop_duplicates().reset_index(drop=True)

# Join with funding on exact Project_Name
merged = pd.merge(funding, proj_df, on='Project_Name', how='inner')

# Filter projects whose name or inferred topic suggests emergency or FEMA
mask = merged['Project_Name'].str.contains('emergency', case=False) | merged['Project_Name'].str.contains('FEMA', case=False)
result = merged[mask][['Project_Name', 'Funding_Source', 'Amount']].drop_duplicates().to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result) )"""

env_args = {'var_call_vggsO8EhdL1SCOR4Roi5kCgp': 'file_storage/call_vggsO8EhdL1SCOR4Roi5kCgp.json', 'var_call_5j3we6F1RM2qPEfAIiGrQ4D8': 'file_storage/call_5j3we6F1RM2qPEfAIiGrQ4D8.json'}

exec(code, env_args)
