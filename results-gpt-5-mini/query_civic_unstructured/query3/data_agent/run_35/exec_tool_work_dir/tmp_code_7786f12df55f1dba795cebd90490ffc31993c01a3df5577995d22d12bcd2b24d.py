code = """import json
import re
import pandas as pd

funding_path = var_call_t41ybTqD9rfuGcYnHnPfELh2
civic_docs_path = var_call_RRCtw1M6xV7FbcQ20yHrrUFn

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# DataFrame for funding
df_f = pd.DataFrame(funding)
if 'Project_Name' not in df_f.columns:
    raise RuntimeError('Funding data missing Project_Name')

def to_int(x):
    try:
        return int(x)
    except:
        try:
            return int(float(x))
        except:
            return None

if 'Amount' in df_f.columns:
    df_f['Amount'] = df_f['Amount'].apply(to_int)
else:
    df_f['Amount'] = None

# Pattern to identify FEMA or emergency
pattern = re.compile(r'(?i)\bfema\b|\bemergency\b|outdoor warning|emergency warning')

# Filter funding rows where Project_Name matches pattern
mask = df_f['Project_Name'].astype(str).str.contains(pattern, na=False)
filtered = df_f[mask].to_dict(orient='records')

# Also include funding rows where Funding_Source mentions FEMA or Emergency
if 'Funding_Source' in df_f.columns:
    mask2 = df_f['Funding_Source'].astype(str).str.contains(pattern, na=False)
    for r in df_f[mask2].to_dict(orient='records'):
        if not any(r['Project_Name'] == x['Project_Name'] for x in filtered):
            filtered.append(r)

# Extract project names from civic docs that mention FEMA or emergency
proj_names = set()
for doc in civic_docs:
    text = doc.get('text','')
    if pattern.search(text):
        # heuristic: find lines that look like project titles (preceding 'Updates:' or 'Project Schedule')
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        for i, ln in enumerate(lines):
            if i+1 < len(lines) and re.search(r'(?i)updates:|project schedule|project description', lines[i+1]):
                if pattern.search(ln) or pattern.search('\n'.join(lines[max(0,i-3):i+4])):
                    proj_names.add(ln)

# Add any project names from docs not already in filtered
for name in proj_names:
    if not any(name.strip().lower() == r['Project_Name'].strip().lower() for r in filtered):
        filtered.append({'Funding_ID': None, 'Project_Name': name, 'Funding_Source': None, 'Amount': None})

# Status detection
status_patterns = [
    ('not started', re.compile(r'(?i)not started')),
    ('completed', re.compile(r'(?i)construction was completed|notice of completion|was completed|completed[,\s]')),
    ('design', re.compile(r'(?i)design\b|preliminary design|complete design|final design|design phase')),
]

all_text = '\n'.join(doc.get('text','') for doc in civic_docs)
all_text_lower = all_text.lower()

def find_status(pname):
    if not pname:
        return 'unknown'
    pname_clean = re.sub(r"\s*\(.*?\)\s*", "", pname).strip()
    idx = all_text_lower.find(pname_clean.lower())
    if idx == -1:
        # try original
        idx = all_text_lower.find(pname.lower())
    if idx == -1:
        return 'unknown'
    start = max(0, idx-300)
    end = min(len(all_text), idx+300)
    window = all_text[start:end]
    for label, pat in status_patterns:
        if pat.search(window):
            return label
    return 'unknown'

results = []
seen = set()
for r in filtered:
    pname = r.get('Project_Name')
    funding_source = r.get('Funding_Source')
    amount = r.get('Amount')
    status = find_status(pname)
    key = (str(pname).lower() if pname else '', str(funding_source).lower() if funding_source else '', amount, status)
    if key in seen:
        continue
    seen.add(key)
    results.append({'Project_Name': pname, 'Funding_Source': funding_source, 'Amount': amount, 'Status': status})

# Sort
results = sorted(results, key=lambda x: (x['Project_Name'] or '').lower())

import json as _json
print("__RESULT__:")
print(_json.dumps(results))"""

env_args = {'var_call_RRCtw1M6xV7FbcQ20yHrrUFn': 'file_storage/call_RRCtw1M6xV7FbcQ20yHrrUFn.json', 'var_call_t41ybTqD9rfuGcYnHnPfELh2': 'file_storage/call_t41ybTqD9rfuGcYnHnPfELh2.json'}

exec(code, env_args)
