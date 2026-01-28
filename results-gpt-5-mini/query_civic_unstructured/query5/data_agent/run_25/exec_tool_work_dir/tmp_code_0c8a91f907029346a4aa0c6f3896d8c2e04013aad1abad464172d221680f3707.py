code = """import json, re

# Load files
with open(var_call_lKT8uPWviNN3rRqoFcXonicP, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_fS8Y5kTNulIFeAWyFvtLhN3D, 'r') as f:
    funding = json.load(f)

# Normalize amounts
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount',0))
    except:
        r['Amount'] = 0

# Disaster keywords
dis_keywords = ['fema','caloes','caljpia','disaster','woolsey','fire','fema/']

# Helper to check if base name appears in text
def base_in_text(base, text):
    base_low = base.lower()
    text_low = text.lower()
    if base_low in text_low:
        return True
    # check if most long words appear
    words = [w for w in re.findall(r"\w+", base_low) if len(w)>3]
    if not words:
        return False
    count = sum(1 for w in words if w in text_low)
    return count >= max(1, len(words)//1)  # require at least 1 long word

# Find funding projects that are disaster-related and mentioned in civic docs with 2022
matched = []
for r in funding:
    pname = r['Project_Name']
    base = pname.split('(')[0].strip()
    pname_low = pname.lower()
    is_dis_suffix = any(k in pname_low for k in dis_keywords)
    found_in_2022_doc = False
    for doc in civic_docs:
        text = doc.get('text','')
        if '2022' not in text:
            continue
        if base_in_text(base, text):
            # if doc indicates disaster keywords or name indicates disaster
            doc_low = text.lower()
            if is_dis_suffix or any(k in doc_low for k in dis_keywords):
                found_in_2022_doc = True
                break
    if found_in_2022_doc:
        matched.append(r)

# Also consider funding records whose names do not include suffix but doc describes as disaster and contains project name and 2022
# (above already handles doc containing dis keywords)

total = sum(r['Amount'] for r in matched)

result = {
    'matched_project_count': len(matched),
    'total_disaster_funding_started_2022': total,
    'matched_projects': [r['Project_Name'] for r in matched]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8CSv4MQuV8zmMnSqLtgrYNGU': ['civic_docs'], 'var_call_eLTMZjr8CgQ9dUU26Ub6TmYQ': ['Funding'], 'var_call_lKT8uPWviNN3rRqoFcXonicP': 'file_storage/call_lKT8uPWviNN3rRqoFcXonicP.json', 'var_call_fS8Y5kTNulIFeAWyFvtLhN3D': 'file_storage/call_fS8Y5kTNulIFeAWyFvtLhN3D.json'}

exec(code, env_args)
