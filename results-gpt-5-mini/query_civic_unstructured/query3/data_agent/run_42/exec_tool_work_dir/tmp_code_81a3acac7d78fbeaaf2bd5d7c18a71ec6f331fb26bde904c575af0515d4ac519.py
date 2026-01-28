code = """import json
import re
import pandas as pd

# load storage variables
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

# parse amount without using backslash escapes
def parse_amount(a):
    try:
        if isinstance(a, (int, float)):
            return int(a)
        s = str(a).replace(',','').strip()
        if s.isdigit():
            return int(s)
        if '.' in s:
            return int(float(s))
    except:
        return None
    return None

funding_df['Amount'] = funding_df['Amount'].apply(parse_amount)

# combine all texts
all_text = "\n\n".join([d.get('text','') for d in docs])
all_text_lower = all_text.lower()

# status inference keywords
status_map = {
    'design': ['complete design', 'preliminary design', 'design phase', 'final design', 'design is', 'design plans', 'design services'],
    'completed': ['construction was completed', 'complete construction', 'notice of completion', 'completed'],
    'not started': ['not started', 'identified', 'awaiting']
}

def infer_status_near(text, idx):
    if idx is None or idx < 0:
        return None
    start = idx-300 if idx-300>0 else 0
    end = idx+300 if idx+300 < len(text) else len(text)
    snippet = text[start:end].lower()
    for status, kws in status_map.items():
        for kw in kws:
            if kw in snippet:
                return status
    if 'under construction' in snippet or 'begin construction' in snippet:
        return 'in construction'
    return None

# remove parenthetical content without backslashes
def remove_paren_content(s):
    res = s
    while True:
        if '(' in res and ')' in res:
            i = res.find('(')
            j = res.find(')', i)
            if j == -1:
                break
            res = (res[:i] + res[j+1:]).strip()
        else:
            break
    return res

results = []
for _, row in funding_df.iterrows():
    pname = row['Project_Name']
    pname_lower = pname.lower()
    include = False
    if 'fema' in pname_lower:
        include = True
    if 'warning' in pname_lower or 'siren' in pname_lower or 'outdoor' in pname_lower or 'emergency' in pname_lower:
        include = True
    # search for project in docs
    idx = all_text_lower.find(pname_lower)
    if idx != -1:
        window = all_text_lower[max(0, idx-200): idx+200]
        if 'fema' in window or 'emergency' in window:
            include = True
    else:
        base = remove_paren_content(pname).lower()
        if base and base != pname_lower:
            idx2 = all_text_lower.find(base)
            if idx2 != -1:
                window = all_text_lower[max(0, idx2-200): idx2+200]
                if 'fema' in window or 'emergency' in window:
                    include = True
    if include:
        status = 'unknown'
        if idx != -1:
            st = infer_status_near(all_text, idx)
            if st:
                status = st
        else:
            base = remove_paren_content(pname).lower()
            idx2 = all_text_lower.find(base) if base else -1
            if idx2 != -1:
                st = infer_status_near(all_text, idx2)
                if st:
                    status = st
        results.append({'Project_Name': pname, 'Funding_Source': row['Funding_Source'], 'Amount': row['Amount'], 'Status': status})

# deduplicate
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
