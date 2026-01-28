code = """import json

# Load tool results
with open(var_call_kq69hvHWYSRKtORLwXydbpNC, 'r') as f:
    funding_rows = json.load(f)
with open(var_call_i9fPgsVIaQXx6Vwcf9GVFWgf, 'r') as f:
    civic_docs = json.load(f)

# Normalize amounts
for r in funding_rows:
    try:
        r['Amount'] = int(r.get('Amount'))
    except Exception:
        try:
            r['Amount'] = int(float(r.get('Amount')))
        except Exception:
            r['Amount'] = None

# Identify funding rows related to FEMA or emergency
keywords = ['fema', 'emergency', 'outdoor warning', 'outdoor warning siren', 'outdoor warning sirens']
candidate_funding = []
for r in funding_rows:
    name = (r.get('Project_Name') or '').lower()
    src = (r.get('Funding_Source') or '').lower()
    if any(k in name for k in keywords) or any(k in src for k in ['federal assistance']):
        candidate_funding.append(r)

# Also include projects whose Project_Name contains '(fema' or 'fema/' etc
for r in funding_rows:
    name = (r.get('Project_Name') or '').lower()
    if 'fema' in name and r not in candidate_funding:
        candidate_funding.append(r)

# Deduplicate
seen_ids = set()
uniq_candidate_funding = []
for r in candidate_funding:
    if r.get('Funding_ID') in seen_ids:
        continue
    seen_ids.add(r.get('Funding_ID'))
    uniq_candidate_funding.append(r)

# Helper to get base name without parenthetical suffix
def base_name(n):
    if not n:
        return n
    if '(' in n:
        return n.split('(')[0].strip()
    return n

# status detection
def detect_status(context):
    if not context:
        return None
    c = context.lower()
    if 'construction was completed' in c or 'complete construction' in c or 'completed' in c:
        return 'completed'
    if 'complete design' in c or 'preliminary design' in c or 'in the preliminary design' in c or 'design' in c:
        return 'design'
    if 'not started' in c or ('identified' in c and 'not' in c):
        return 'not started'
    if 'currently under construction' in c or 'begin construction' in c or 'begin construction' in c:
        return 'design'
    if 'awaiting' in c or 'awaiting final' in c or 'awaiting final fema' in c:
        return 'design'
    return None

# For each candidate funding, search civic documents for mentions and extract status
results = []
for fr in uniq_candidate_funding:
    pname = fr.get('Project_Name')
    pname_lower = pname.lower() if pname else ''
    bname = base_name(pname)
    bname_lower = bname.lower() if bname else ''
    found = False
    found_file = None
    status = None
    for doc in civic_docs:
        text = doc.get('text','')
        text_lower = text.lower()
        # try full project name first
        idx = -1
        if pname_lower and pname_lower in text_lower:
            idx = text_lower.find(pname_lower)
        elif bname_lower and bname_lower in text_lower:
            idx = text_lower.find(bname_lower)
        else:
            # try keywords related to emergency projects like 'outdoor warning' or 'sirens'
            if 'outdoor warning' in pname_lower or 'outdoor warning' in text_lower:
                idx = text_lower.find('outdoor warning')
            elif 'sirens' in pname_lower or 'sirens' in text_lower:
                idx = text_lower.find('sirens')
            elif 'emergency' in pname_lower and 'emergency' in text_lower:
                idx = text_lower.find('emergency')
        if idx != -1:
            found = True
            found_file = doc.get('filename')
            start = max(0, idx-300)
            end = min(len(text), idx+300)
            context = text[start:end]
            status = detect_status(context)
            break
    results.append({
        'Project_Name': pname,
        'Funding_Source': fr.get('Funding_Source'),
        'Amount': fr.get('Amount'),
        'Status': status,
        'Found_In_File': found_file
    })

# If no candidates found, try to additionally find projects in funding_rows where project name contains keywords like 'Guardrail' with '(FEMA' etc.
# (already covered by 'fema' in name)

# Final output
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_i9fPgsVIaQXx6Vwcf9GVFWgf': 'file_storage/call_i9fPgsVIaQXx6Vwcf9GVFWgf.json', 'var_call_JwmRPtqX1MX9rXaQGM5997gn': ['Funding'], 'var_call_kq69hvHWYSRKtORLwXydbpNC': 'file_storage/call_kq69hvHWYSRKtORLwXydbpNC.json'}

exec(code, env_args)
