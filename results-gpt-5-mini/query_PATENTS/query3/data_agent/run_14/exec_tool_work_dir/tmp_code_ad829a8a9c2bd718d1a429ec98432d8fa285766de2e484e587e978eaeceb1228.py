code = """import json, re
# load files from storage keys
fp_uc = var_call_q57aScl073IRIRJqWMJOS9E9
fp_others = var_call_lSeKCaJYvKmAFrQEd6Ri9Oy6
with open(fp_uc, 'r', encoding='utf-8') as f:
    uc = json.load(f)
with open(fp_others, 'r', encoding='utf-8') as f:
    others = json.load(f)
uc_set = set(uc.get('publication_numbers', []))

results = []
primary_codes_set = set()

for rec in others:
    citation = rec.get('citation')
    if not citation:
        continue
    try:
        cites = json.loads(citation)
    except Exception:
        # try to find publication numbers via regex
        cites = []
        for m in re.finditer(r'([A-Z]{2}-?\d+[A-Z0-9\-]*)', str(citation)):
            cites.append({'publication_number': m.group(1)})
    matched = False
    for c in cites:
        pn = c.get('publication_number')
        if pn and pn in uc_set:
            matched = True
            break
    if not matched:
        continue
    # extract assignee from Patents_info
    pi = rec.get('Patents_info','')
    assignee = None
    # try patterns
    patterns = [r'^(.*?)\s+holds\b', r'^(.*?)\s+holds the\b', r'^(.*?)\s+is assigned to\b', r'^(.*?)\s+is owned by\b', r'^(.*?)\s+owned by\b', r'^(.*?)\s+owns\b', r'^(.*?)\s+has\b', r'^(.*?)\s+holder\b', r'^(.*?)\s+applicant\b', r'^(.*?)\s+\(ID\b']
    for p in patterns:
        m = re.search(p, pi, flags=re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
            break
    if not assignee:
        # fallback: take up to comma
        assignee = pi.split(',')[0].strip()
    # skip UNIV CALIFORNIA
    if re.search(r'UNIV\.?\s*CALIFORNIA', assignee, flags=re.IGNORECASE):
        continue
    # parse cpc field to get primary codes where first==true
    cpc_field = rec.get('cpc')
    primary_codes = []
    if cpc_field:
        try:
            cpcs = json.loads(cpc_field)
            for cp in cpcs:
                if cp.get('first') or cp.get('first')==True:
                    code = cp.get('code')
                    if code:
                        primary_codes.append(code)
                        primary_codes_set.add(code)
        except Exception:
            # fallback: find codes via regex
            for m in re.finditer(r'([A-Z]\d[0-9A-Z/\-]+)', str(cpc_field)):
                primary_codes.append(m.group(1))
                primary_codes_set.add(m.group(1))
    if not primary_codes:
        # if none marked first, pick first code encountered
        try:
            cpcs = json.loads(cpc_field)
            if cpcs:
                code = cpcs[0].get('code')
                if code:
                    primary_codes.append(code)
                    primary_codes_set.add(code)
        except Exception:
            pass
    results.append({'rowid': rec.get('rowid'), 'assignee': assignee, 'primary_codes': primary_codes})

out = {'results': results, 'primary_codes': sorted(primary_codes_set)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MuJAaiO2PzoIYGskQYaoTn64': 'file_storage/call_MuJAaiO2PzoIYGskQYaoTn64.json', 'var_call_q57aScl073IRIRJqWMJOS9E9': 'file_storage/call_q57aScl073IRIRJqWMJOS9E9.json', 'var_call_lSeKCaJYvKmAFrQEd6Ri9Oy6': 'file_storage/call_lSeKCaJYvKmAFrQEd6Ri9Oy6.json'}

exec(code, env_args)
