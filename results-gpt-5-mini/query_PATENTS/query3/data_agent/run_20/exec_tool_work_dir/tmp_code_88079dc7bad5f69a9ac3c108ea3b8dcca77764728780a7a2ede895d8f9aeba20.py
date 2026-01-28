code = """import json, re
with open(var_call_UCPD1RS4AZvlswJyAis5URH1, 'r') as f:
    univ_rows = json.load(f)
with open(var_call_TXF5iLgHVwuGHi0geYBudpqL, 'r') as f:
    citing_rows = json.load(f)

# Extract pub numbers by finding tokens like XX-... with digits
pubnum_pattern = re.compile(r"\b[A-Z]{2}-[A-Z0-9\-]+\b")

univ_pubnums = set()
for r in univ_rows:
    text = r.get('Patents_info','')
    for m in pubnum_pattern.findall(text):
        if re.search(r"\d", m):
            univ_pubnums.add(m.strip())

# function to extract assignee name
def extract_assignee(text):
    if not text:
        return None
    text = text.strip()
    # common separators
    for sep in [' holds the', ' holds', ' is assigned to', ' is owned by', ' owns the', ' belonging to', ' is belonging to', ' held by', ',']:
        idx = text.lower().find(sep)
        if idx!=-1:
            name = text[:idx]
            return name.strip().upper()
    # fallback first 40 chars
    return text.split()[0:4]

results = []
unique_primary_cpcs = set()

for r in citing_rows:
    citation_field = r.get('citation')
    if not citation_field:
        continue
    # parse citation JSON
    try:
        citations = json.loads(citation_field) if isinstance(citation_field, str) else citation_field
    except:
        citations = []
    matched = False
    for c in citations:
        if not isinstance(c, dict):
            continue
        pubnum = c.get('publication_number')
        if not pubnum:
            continue
        if pubnum.strip() in univ_pubnums:
            matched = True
            break
    if not matched:
        continue
    # get assignee
    assignee = extract_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    # if assignee contains UNIV CALIFORNIA skip
    if 'UNIV CALIFORNIA' in assignee:
        continue
    # parse cpc
    primary_codes = []
    cpc_field = r.get('cpc')
    try:
        cpcs = json.loads(cpc_field) if isinstance(cpc_field, str) else cpc_field
    except:
        cpcs = []
    if isinstance(cpcs, list):
        for e in cpcs:
            if isinstance(e, dict) and e.get('first'):
                code = e.get('code')
                if code:
                    primary_codes.append(code)
                    unique_primary_cpcs.add(code)
    if not primary_codes and isinstance(cpcs, list) and len(cpcs)>0:
        e = cpcs[0]
        if isinstance(e, dict) and e.get('code'):
            primary_codes.append(e.get('code'))
            unique_primary_cpcs.add(e.get('code'))
    results.append({'assignee': assignee, 'primary_cpcs': primary_codes})

output = {'mappings': results, 'unique_primary_cpcs': sorted(unique_primary_cpcs)}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_JmtpD4VJGFoecQO8VCX0zY1M': 'file_storage/call_JmtpD4VJGFoecQO8VCX0zY1M.json', 'var_call_UCPD1RS4AZvlswJyAis5URH1': 'file_storage/call_UCPD1RS4AZvlswJyAis5URH1.json', 'var_call_TXF5iLgHVwuGHi0geYBudpqL': 'file_storage/call_TXF5iLgHVwuGHi0geYBudpqL.json'}

exec(code, env_args)
