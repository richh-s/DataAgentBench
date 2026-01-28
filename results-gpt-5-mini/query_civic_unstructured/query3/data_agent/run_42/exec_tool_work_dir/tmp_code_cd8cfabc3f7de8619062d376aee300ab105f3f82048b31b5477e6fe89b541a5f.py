code = """import json, os

# Load variables from storage
funding_var = var_call_T7kVCxI35Rb96wVLxFptILKp
docs_var = var_call_Kf6WvGDTE8OWsd75wFh8A3Zf

# If storage entries are file paths, load JSON from them
if isinstance(funding_var, str) and os.path.exists(funding_var):
    with open(funding_var, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_var

if isinstance(docs_var, str) and os.path.exists(docs_var):
    with open(docs_var, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_var

# Combine all document texts
all_text = ''
for d in docs:
    t = d.get('text', '')
    if t:
        all_text += t + (chr(10) * 2)
all_low = all_text.lower()

# Helper to convert amount
def to_int(x):
    try:
        return int(str(x).replace(',', ''))
    except:
        return None

# Keywords
keywords_in_name = ['fema', 'emergency', 'warning', 'siren', 'outdoor warning']

results = []
for rec in funding:
    pname = str(rec.get('Project_Name', ''))
    pname_low = pname.lower()
    match = False
    for kw in keywords_in_name:
        if kw in pname_low:
            match = True
            break
    # check if project name appears in docs near keywords
    if not match and pname_low:
        idx = all_low.find(pname_low)
        if idx != -1:
            window = all_low[max(0, idx-200): idx+200]
            if 'fema' in window or 'emergency' in window:
                match = True
        else:
            # try base name without parentheses
            base = pname_low.split('(')[0].strip()
            if base and base != pname_low:
                idx2 = all_low.find(base)
                if idx2 != -1:
                    window = all_low[max(0, idx2-200): idx2+200]
                    if 'fema' in window or 'emergency' in window:
                        match = True
    if match:
        # infer status
        status = 'unknown'
        idx = all_low.find(pname_low)
        if idx == -1:
            base = pname_low.split('(')[0].strip()
            idx = all_low.find(base) if base else -1
        if idx != -1:
            window = all_low[max(0, idx-200): idx+200]
            if any(x in window for x in ['complete design', 'preliminary design', 'design phase', 'final design', 'design plans']):
                status = 'design'
            if any(x in window for x in ['construction was completed', 'complete construction', 'notice of completion']) or 'completed' in window:
                status = 'completed'
            if any(x in window for x in ['not started', 'identified', 'awaiting']):
                status = 'not started'
            if any(x in window for x in ['begin construction', 'under construction']):
                status = 'in construction'
        results.append({
            'Project_Name': pname,
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': to_int(rec.get('Amount')),
            'Status': status
        })

# Deduplicate by project name
seen = set()
unique = []
for r in results:
    if r['Project_Name'] not in seen:
        seen.add(r['Project_Name'])
        unique.append(r)

# Sort
unique = sorted(unique, key=lambda x: x['Project_Name'].lower())

print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_call_T7kVCxI35Rb96wVLxFptILKp': 'file_storage/call_T7kVCxI35Rb96wVLxFptILKp.json', 'var_call_Kf6WvGDTE8OWsd75wFh8A3Zf': 'file_storage/call_Kf6WvGDTE8OWsd75wFh8A3Zf.json', 'var_call_eZIC5XlJiRf5SrqsXL4XzQLh': 'test'}

exec(code, env_args)
