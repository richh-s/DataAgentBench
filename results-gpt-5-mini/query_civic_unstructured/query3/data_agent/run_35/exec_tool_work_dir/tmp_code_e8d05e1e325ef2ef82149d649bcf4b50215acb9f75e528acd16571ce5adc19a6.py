code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
funding_path = var_call_t41ybTqD9rfuGcYnHnPfELh2
civic_docs_path = var_call_RRCtw1M6xV7FbcQ20yHrrUFn

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
df_f = pd.DataFrame(funding)
# Ensure column names
if 'Project_Name' not in df_f.columns:
    raise ValueError('Funding data missing Project_Name')

# Normalize types
df_f['Project_Name'] = df_f['Project_Name'].astype(str)
# Convert Amount to int where possible
def to_int(x):
    try:
        return int(x)
    except:
        try:
            return int(float(x))
        except:
            return None

df_f['Amount'] = df_f.get('Amount').apply(to_int)

# Pattern to identify FEMA or emergency related projects
pattern = re.compile(r'(?i)fema|emergency|outdoor warning|emergency warning')

# Filter funding rows matching the pattern in Project_Name
mask = df_f['Project_Name'].str.contains(pattern)
filtered_fund = df_f[mask].to_dict(orient='records')

# Also, search civic documents for project names that mention FEMA or emergency (even if not in funding names)
# Extract potential project names from civic docs by simple heuristic: lines that look like project headings
project_names_in_docs = set()
for doc in civic_docs:
    text = doc.get('text','')
    # Find lines that are non-empty and not too long and followed by Updates or Project Schedule
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    for i, ln in enumerate(lines):
        if (i+1 < len(lines)) and re.search(r'(?i)updates:|project schedule|project description', lines[i+1]):
            # candidate project name
            project_names_in_docs.add(ln)
# Filter those that mention FEMA or emergency
for name in project_names_in_docs:
    if pattern.search(name):
        # Check if already in filtered_fund by name
        if not any(r['Project_Name'].lower() == name.lower() for r in filtered_fund):
            filtered_fund.append({'Funding_ID': None, 'Project_Name': name, 'Funding_Source': None, 'Amount': None})

# Function to find status from civic docs for a given project name
status_keywords = [
    ('not started', re.compile(r'(?i)not started')),
    ('completed', re.compile(r'(?i)construction was completed|notice of completion|was completed|completed[,\s]')), 
    ('design', re.compile(r'(?i)design\b|preliminary design|complete design|final design|design phase')),
]

def find_status_for_project(pname):
    # Try exact name and a base name without parenthetical suffix
    candidates = [pname, re.sub(r"\s*\(.*?\)\s*", "", pname).strip()]
    text_join = "\n".join([doc.get('text','') for doc in civic_docs])
    text_lower = text_join.lower()
    for cand in candidates:
        if not cand:
            continue
        idx = text_lower.find(cand.lower())
        if idx != -1:
            # extract window
            start = max(0, idx-400)
            end = min(len(text_join), idx+400)
            window = text_join[start:end]
            # Check keywords
            for status, regex in status_keywords:
                if regex.search(window):
                    return status
            # No keyword matched
            return 'unknown'
    return 'unknown'

results = []
seen = set()
for row in filtered_fund:
    pname = row.get('Project_Name')
    funding_source = row.get('Funding_Source')
    amount = row.get('Amount')
    status = find_status_for_project(pname)
    key = (pname, funding_source, amount, status)
    if key in seen:
        continue
    seen.add(key)
    results.append({
        'Project_Name': pname,
        'Funding_Source': funding_source,
        'Amount': amount,
        'Status': status
    })

# Sort results by Project_Name
results = sorted(results, key=lambda x: (x['Project_Name'] or '').lower())

import json as _json
print("__RESULT__:")
print(_json.dumps(results))"""

env_args = {'var_call_RRCtw1M6xV7FbcQ20yHrrUFn': 'file_storage/call_RRCtw1M6xV7FbcQ20yHrrUFn.json', 'var_call_t41ybTqD9rfuGcYnHnPfELh2': 'file_storage/call_t41ybTqD9rfuGcYnHnPfELh2.json'}

exec(code, env_args)
