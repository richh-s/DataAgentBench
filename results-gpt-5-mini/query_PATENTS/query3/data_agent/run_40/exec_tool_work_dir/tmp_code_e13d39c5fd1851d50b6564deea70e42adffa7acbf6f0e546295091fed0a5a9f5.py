code = """import json, re
# var_call_mgnuO1NLUamXno1MDIunxmSO is available from storage
path = var_call_mgnuO1NLUamXno1MDIunxmSO
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

assignee_map = {}
all_codes = set()

# patterns to extract assignee
patterns = [r'belonging to ([A-Z0-9 &\-\.,]+)',
            r'is belonging to ([A-Z0-9 &\-\.,]+)',
            r'assigned to ([A-Z0-9 &\-\.,]+)',
            r'is assigned to ([A-Z0-9 &\-\.,]+)',
            r'assignee[:\s]+([A-Z0-9 &\-\.,]+)',
            r'owned by ([A-Z0-9 &\-\.,]+)']

for rec in records:
    pi = rec.get('Patents_info') or ''
    cpc_field = rec.get('cpc') or '[]'
    # parse cpc field if it's a JSON string
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # try if already a list
        cpcs = cpc_field if isinstance(cpc_field, list) else []

    assignee = None
    upi = pi.upper()
    # try patterns on original Pi to preserve punctuation
    for pat in patterns:
        m = re.search(pat, pi, flags=re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
            # trim trailing words like 'and has publication' or 'and' or 'with'
            assignee = re.split(r'\s+AND\b|\s+WITH\b|\s+HAS\b|,|;|\.|\bAND HAS\b', assignee, flags=re.IGNORECASE)[0].strip()
            break
    if not assignee:
        # fallback: look for the phrase 'belonging to' in uppercase
        m = re.search(r'BELONGING TO ([A-Z0-9 &\-\.,]+)', upi)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        # as last resort, try to extract a sequence of words before 'and has publication' or 'has publication'
        m = re.search(r'([A-Z0-9 &\-\.,]{5,})\s+AND\s+HAS\s+PUBLICATION', upi)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        # try to find an all-caps phrase of length>3
        m = re.search(r'([A-Z]{3,}(?: [A-Z0-9]{2,})+)', upi)
        if m:
            assignee = m.group(1).strip()

    if not assignee:
        continue

    # normalize
    assignee_norm = assignee.strip()
    # exclude Univ California
    if 'UNIV CALIFORNIA' in assignee_norm.upper() or 'UNIVERSITY OF CALIFORNIA' in assignee_norm.upper():
        continue

    # find primary cpc codes (where first == true)
    primary_codes = []
    if isinstance(cpcs, list):
        for e in cpcs:
            try:
                if e.get('first') is True:
                    code = e.get('code') or e.get('symbol') or None
                    if code:
                        primary_codes.append(code)
            except Exception:
                pass
    # fallback: if no primary_codes, take first code entries
    if not primary_codes:
        if isinstance(cpcs, list) and len(cpcs)>0:
            code = cpcs[0].get('code') if isinstance(cpcs[0], dict) else None
            if not code:
                # try to find any 'code' keys
                for e in cpcs:
                    if isinstance(e, dict) and ('code' in e or 'symbol' in e):
                        code = e.get('code') or e.get('symbol')
                        break
            if code:
                primary_codes.append(code)

    if not primary_codes:
        continue

    # add to map
    current = assignee_map.get(assignee_norm, set())
    for c in primary_codes:
        current.add(c)
        all_codes.add(c)
    assignee_map[assignee_norm] = current

# prepare output
out = {
    'assignees': [{ 'assignee': a, 'codes': sorted(list(codes)) } for a, codes in assignee_map.items()],
    'codes': sorted(list(all_codes))
}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_YhT3RtPYuPUxiQPaMOH5T3TG': ['publicationinfo'], 'var_call_5SwPYlRI2uvKKcds69kZ4mQk': ['cpc_definition'], 'var_call_mgnuO1NLUamXno1MDIunxmSO': 'file_storage/call_mgnuO1NLUamXno1MDIunxmSO.json'}

exec(code, env_args)
