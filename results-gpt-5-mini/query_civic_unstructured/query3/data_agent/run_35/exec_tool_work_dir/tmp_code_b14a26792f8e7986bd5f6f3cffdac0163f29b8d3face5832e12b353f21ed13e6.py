code = """import json
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

# Convert Amount to int where possible
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

# Lowercase project names for matching
proj_names_lower = df_f['Project_Name'].astype(str).str.lower()

# Define simple keyword check
def mentions_fema_emergency(s):
    if not s:
        return False
    s = s.lower()
    return ('fema' in s) or ('emergency' in s) or ('outdoor warning' in s) or ('emergency warning' in s)

# Filter funding rows where project name or funding source mentions fema/emergency
filtered = []
for r in funding:
    pname = r.get('Project_Name','')
    fsrc = r.get('Funding_Source','')
    if mentions_fema_emergency(pname) or mentions_fema_emergency(fsrc):
        # normalize amount
        amt = r.get('Amount')
        try:
            amt = int(amt)
        except:
            try:
                amt = int(float(amt))
            except:
                amt = None
        filtered.append({'Funding_ID': r.get('Funding_ID'), 'Project_Name': pname, 'Funding_Source': fsrc, 'Amount': amt})

# Now search civic docs for projects mentioning fema/emergency and extract project names heuristically
all_text = '\n'.join(doc.get('text','') for doc in civic_docs)
all_text_lower = all_text.lower()

# Heuristic: find lines that are titles: lines followed by 'Updates:' or 'Project Schedule' or 'Project Description'
proj_names_from_docs = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    for i, ln in enumerate(lines):
        nxt = lines[i+1] if i+1 < len(lines) else ''
        if any(k in nxt.lower() for k in ['updates:', 'project schedule', 'project description']):
            # Check nearby context for keywords
            context_window = ' '.join(lines[max(0,i-3):i+4]).lower()
            if 'fema' in context_window or 'emergency' in context_window or 'outdoor warning' in context_window:
                proj_names_from_docs.add(ln)

# Add doc-extracted project names to filtered if not present
existing_names = set(r['Project_Name'].strip().lower() for r in filtered if r.get('Project_Name'))
for name in proj_names_from_docs:
    if name.strip().lower() not in existing_names:
        filtered.append({'Funding_ID': None, 'Project_Name': name, 'Funding_Source': None, 'Amount': None})

# Determine status by searching for keywords near the project name in all_text
status_keywords = [
    ('not started', ['not started']),
    ('completed', ['construction was completed', 'notice of completion', 'was completed', 'completed']),
    ('design', ['design', 'preliminary design', 'complete design', 'final design', 'design phase']),
]

def find_status(pname):
    if not pname:
        return 'unknown'
    # try both with and without parenthetical suffix
    base = pname
    if '(' in pname:
        base = pname.split('(')[0].strip()
    idx = all_text_lower.find(base.lower())
    if idx == -1:
        idx = all_text_lower.find(pname.lower())
    if idx == -1:
        return 'unknown'
    start = max(0, idx-300)
    end = min(len(all_text_lower), idx+300)
    window = all_text_lower[start:end]
    for label, kwlist in status_keywords:
        for kw in kwlist:
            if kw in window:
                return label
    return 'unknown'

# Build results
results = []
seen = set()
for r in filtered:
    pname = r.get('Project_Name')
    fsrc = r.get('Funding_Source')
    amt = r.get('Amount')
    status = find_status(pname)
    key = (pname.strip().lower() if pname else '', (fsrc or '').strip().lower(), amt, status)
    if key in seen:
        continue
    seen.add(key)
    results.append({'Project_Name': pname, 'Funding_Source': fsrc, 'Amount': amt, 'Status': status})

# Sort
results = sorted(results, key=lambda x: (x['Project_Name'] or '').lower())

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_RRCtw1M6xV7FbcQ20yHrrUFn': 'file_storage/call_RRCtw1M6xV7FbcQ20yHrrUFn.json', 'var_call_t41ybTqD9rfuGcYnHnPfELh2': 'file_storage/call_t41ybTqD9rfuGcYnHnPfELh2.json'}

exec(code, env_args)
