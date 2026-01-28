code = """import json
import pandas as pd

# Access storage variables directly
funding_data = var_call_T7kVCxI35Rb96wVLxFptILKp
docs_data = var_call_Kf6WvGDTE8OWsd75wFh8A3Zf

# If they are file paths (strings), load JSON
import os
if isinstance(funding_data, str) and os.path.exists(funding_data):
    with open(funding_data, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_data

if isinstance(docs_data, str) and os.path.exists(docs_data):
    with open(docs_data, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_data

# Build combined text
all_text = "\n\n".join([d.get('text','') for d in docs])
all_text_lower = all_text.lower()

# Load funding into DataFrame
df = pd.DataFrame(funding)
if 'Project_Name' not in df.columns:
    df = pd.DataFrame(columns=['Funding_ID','Project_Name','Funding_Source','Amount'])

# normalize amount
def to_int(x):
    try:
        return int(str(x).replace(',',''))
    except:
        return None

if 'Amount' in df.columns:
    df['Amount'] = df['Amount'].apply(to_int)
else:
    df['Amount'] = None

# define keywords
kw_lower = ['fema','emergency','warning','siren','outdoor warning']

results = []
for _, row in df.iterrows():
    pname = str(row.get('Project_Name',''))
    pname_low = pname.lower()
    match = False
    for kw in kw_lower:
        if kw in pname_low:
            match = True
            break
    # also check if project name appears in docs near keywords
    if not match:
        idx = all_text_lower.find(pname_low)
        if idx != -1:
            window = all_text_lower[max(0, idx-200): idx+200]
            for kw in ['fema','emergency']:
                if kw in window:
                    match = True
                    break
    if match:
        # infer status by searching nearby words
        status = 'unknown'
        idx = all_text_lower.find(pname_low)
        if idx == -1:
            # try base name without parenthesis
            base = pname_low
            if '(' in base:
                base = base.split('(')[0].strip()
            idx = all_text_lower.find(base)
        if idx != -1:
            window = all_text_lower[max(0, idx-200): idx+200]
            if 'complete design' in window or 'preliminary design' in window or 'design phase' in window or 'final design' in window:
                status = 'design'
            if 'construction was completed' in window or 'complete construction' in window or 'notice of completion' in window or 'completed' in window:
                status = 'completed'
            if 'not started' in window or 'identified' in window or 'awaiting' in window:
                status = 'not started'
            if 'begin construction' in window or 'under construction' in window:
                status = 'in construction'
        results.append({
            'Project_Name': pname,
            'Funding_Source': row.get('Funding_Source'),
            'Amount': row.get('Amount'),
            'Status': status
        })

# deduplicate by project name
seen = set()
unique = []
for r in results:
    if r['Project_Name'] not in seen:
        seen.add(r['Project_Name'])
        unique.append(r)

unique = sorted(unique, key=lambda x: x['Project_Name'].lower())

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_T7kVCxI35Rb96wVLxFptILKp': 'file_storage/call_T7kVCxI35Rb96wVLxFptILKp.json', 'var_call_Kf6WvGDTE8OWsd75wFh8A3Zf': 'file_storage/call_Kf6WvGDTE8OWsd75wFh8A3Zf.json'}

exec(code, env_args)
