code = """import json, re
# Load stored JSON results from previous query_db calls
uc_file = var_call_lFZ8uNxaeU5pX5Ch15ofoav1
all_file = var_call_X0QLcnAs0WWuHXE5JbGpCQuc
with open(uc_file, 'r', encoding='utf-8') as f:
    uc_records = json.load(f)
with open(all_file, 'r', encoding='utf-8') as f:
    all_records = json.load(f)

# Extract publication numbers for UNIV CALIFORNIA patents
pubnums = set()
pat_pub_regex = re.compile(r'pub(?:lication)?\.? number\s*([A-Z0-9\-]+)', re.IGNORECASE)
for r in uc_records:
    pi = r.get('Patents_info','')
    m = pat_pub_regex.search(pi)
    if m:
        pubnums.add(m.group(1).strip())
# Also some Patents_info may include 'publication number' without that exact phrase - try alternative
alt_regex = re.compile(r'publication number\s*([A-Z0-9\-]+)', re.IGNORECASE)
for r in uc_records:
    pi = r.get('Patents_info','')
    m = alt_regex.search(pi)
    if m:
        pubnums.add(m.group(1).strip())

# Fallback: some records might contain 'pub. number' with different punctuation already captured

# Now find all patents that cite any of these publication numbers
citing = {}  # assignee -> set of primary cpc codes
for r in all_records:
    citations_raw = r.get('citation','')
    if not citations_raw:
        continue
    try:
        citations = json.loads(citations_raw)
    except Exception:
        # maybe empty list string or already list
        if isinstance(citations_raw, list):
            citations = citations_raw
        else:
            try:
                citations = eval(citations_raw)
            except Exception:
                continue
    cited = False
    for c in citations:
        pub = c.get('publication_number','') if isinstance(c, dict) else ''
        if pub and pub in pubnums:
            cited = True
            break
    if not cited:
        continue
    # extract assignee from Patents_info
    pi = r.get('Patents_info','')
    assignee = None
    patterns = [r'^(.*?) holds', r'^(.*?) holds the', r'^(.*?) is assigned to', r'^(.*?) is owned by', r'^(.*?) holds the', r'^(.*?) has been assigned to', r'^(.*?) has assigned', r'^(.*?)\s+owns\s+the']
    for p in patterns:
        m = re.search(p, pi, re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
            break
    if not assignee:
        # fallback: take leading phrase before 'the' or before 'holds' etc
        m = re.match(r'^([A-Z0-9\- &,\.]+?)\s+(?:has|holds|is|owns)', pi)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        # last fallback: take first 60 chars
        assignee = pi.split(' has ')[0].split(' holds ')[0].strip()[:120]
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    # get primary cpc code
    primary_codes = set()
    cpc_raw = r.get('cpc','')
    try:
        cpcs = json.loads(cpc_raw)
    except Exception:
        if isinstance(cpc_raw, list):
            cpcs = cpc_raw
        else:
            try:
                cpcs = eval(cpc_raw)
            except Exception:
                cpcs = []
    # find entries with 'first'==True
    for e in cpcs:
        if isinstance(e, dict) and e.get('first'):
            code = e.get('code')
            if code:
                primary_codes.add(code)
    if not primary_codes:
        # take first code encountered
        for e in cpcs:
            if isinstance(e, dict):
                code = e.get('code')
                if code:
                    primary_codes.add(code)
                    break
    if not primary_codes:
        continue
    if assignee not in citing:
        citing[assignee] = set()
    citing[assignee].update(primary_codes)

# Prepare result list
result = []
for a, codes in citing.items():
    result.append({'assignee': a, 'cpc_codes': sorted(list(codes))})

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lFZ8uNxaeU5pX5Ch15ofoav1': 'file_storage/call_lFZ8uNxaeU5pX5Ch15ofoav1.json', 'var_call_X0QLcnAs0WWuHXE5JbGpCQuc': 'file_storage/call_X0QLcnAs0WWuHXE5JbGpCQuc.json'}

exec(code, env_args)
