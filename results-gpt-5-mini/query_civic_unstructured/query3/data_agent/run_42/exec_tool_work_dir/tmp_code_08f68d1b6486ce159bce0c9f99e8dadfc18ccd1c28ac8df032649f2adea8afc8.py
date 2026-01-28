code = """import json
import re
import pandas as pd

# helper to load storage variable which may be a filepath or a Python object
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_var(var_call_T7kVCxI35Rb96wVLxFptILKp)
docs = load_var(var_call_Kf6WvGDTE8OWsd75wFh8A3Zf)

funding_df = pd.DataFrame(funding)
funding_df['Project_Name'] = funding_df['Project_Name'].astype(str)
funding_df['Funding_Source'] = funding_df['Funding_Source'].astype(str)

# convert Amount to int where possible
def parse_amount(a):
    try:
        if isinstance(a, (int, float)):
            return int(a)
        s = str(a).replace(',', '').strip()
        if re.match(r"^\d+$", s):
            return int(s)
        if re.match(r"^\d+\.\d+$", s):
            return int(float(s))
    except:
        return None
    return None

funding_df['Amount'] = funding_df['Amount'].apply(parse_amount)

# combine docs texts
all_text = "\n\n".join([d.get('text','') for d in docs])
all_text_lower = all_text.lower()

# status inference
status_map = {
    'design': ['complete design', 'preliminary design', 'design phase', 'final design', 'design is', 'design plans', 'design services'],
    'completed': ['construction was completed', 'complete construction', 'notice of completion', 'completed'],
    'not started': ['not started', 'identified', 'awaiting']
}

def infer_status_near(text, idx):
    if idx is None or idx < 0:
        return None
    snippet = text[max(0, idx-300): idx+300].lower()
    for status, kws in status_map.items():
        for kw in kws:
            if kw in snippet:
                return status
    if 'under construction' in snippet or 'begin construction' in snippet:
        return 'in construction'
    return None

results = []

# criteria: Project_Name contains 'fema' OR project name appears in docs near 'fema' or 'emergency' OR name contains warning/siren
for _, row in funding_df.iterrows():
    pname = row['Project_Name']
    pname_lower = pname.lower()
    include = False
    if 'fema' in pname_lower:
        include = True
    if 'warning' in pname_lower or 'siren' in pname_lower or 'outdoor' in pname_lower:
        include = True
    # check if project name appears in civic docs near keywords
    idx = all_text_lower.find(pname_lower)
    if idx != -1:
        # check window for keywords
        window = all_text_lower[max(0, idx-200): idx+200]
        if 'fema' in window or 'emergency' in window:
            include = True
    else:
        # try base name without parenthetical
        base = re.sub(r"\s*\(.*?\)\s*", "", pname).strip().lower()
        if base and base != pname_lower:
            idx2 = all_text_lower.find(base)
            if idx2 != -1:
                window = all_text_lower[max(0, idx2-200): idx2+200]
                if 'fema' in window or 'emergency' in window:
                    include = True
    if include:
        # infer status using idx if found, else try base
        status = None
        if idx != -1:
            status = infer_status_near(all_text, idx)
        else:
            base = re.sub(r"\s*\(.*?\)\s*", "", pname).strip().lower()
            idx2 = all_text_lower.find(base) if base else -1
            if idx2 != -1:
                status = infer_status_near(all_text, idx2)
        if status is None:
            status = 'unknown'
        results.append({
            'Project_Name': pname,
            'Funding_Source': row['Funding_Source'],
            'Amount': row['Amount'],
            'Status': status
        })

# deduplicate by Project_Name
unique = {}
for r in results:
    if r['Project_Name'] not in unique:
        unique[r['Project_Name']] = r

final = list(unique.values())
final = sorted(final, key=lambda x: x['Project_Name'].lower())

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_T7kVCxI35Rb96wVLxFptILKp': 'file_storage/call_T7kVCxI35Rb96wVLxFptILKp.json', 'var_call_Kf6WvGDTE8OWsd75wFh8A3Zf': 'file_storage/call_Kf6WvGDTE8OWsd75wFh8A3Zf.json'}

exec(code, env_args)
