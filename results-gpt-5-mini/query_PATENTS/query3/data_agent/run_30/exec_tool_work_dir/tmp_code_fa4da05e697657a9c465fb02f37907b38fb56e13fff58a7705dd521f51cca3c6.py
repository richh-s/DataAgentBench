code = """import json, re
path = var_call_Lb2aFYNCzIUGMiHjFYMERzCW
with open(path, 'r') as f:
    records = json.load(f)
# Build set of Univ California publication numbers from these records
univ_pubnums = set()
re_pub = re.compile(r'\b[A-Z]{2,3}-[0-9]{4,}[A-Z0-9\-]*\b')
for rec in records:
    pi = rec.get('Patents_info') or ''
    if 'UNIV' in pi.upper() or 'UNIVERSITY OF CALIFORNIA' in pi.upper():
        for m in re_pub.finditer(pi.upper()):
            univ_pubnums.add(m.group(0))
# also include patterns like 'publication number US-11421276-B2' maybe with 'US-11421276-B2'

# Now scan the full publicationinfo table (we have earlier big file var_call_5I4DtjpcM4Fv7fjmRPlhswNj)
with open(var_call_5I4DtjpcM4Fv7fjmRPlhswNj, 'r') as f:
    allrecs = json.load(f)

assignee_to_codes = {}
all_codes = set()

for rec in allrecs:
    # parse citation field
    citations = rec.get('citation') or []
    if isinstance(citations, str):
        try:
            citations = json.loads(citations)
        except:
            citations = []
    cited_pubnums = set()
    for c in citations:
        if isinstance(c, dict):
            p = (c.get('publication_number') or '').upper().strip()
            if p:
                cited_pubnums.add(p)
    if not (cited_pubnums & univ_pubnums):
        continue
    # this record cites a Univ California patent
    pi = rec.get('Patents_info') or ''
    # find assignee in Patents_info
    assignee = None
    # common forms: 'X holds the US patent', 'In US, the application ... is assigned to X and has publication number X'
    m = re.search(r'IS ASSIGNED TO ([^,\.]+)', pi.upper())
    if not m:
        m = re.search(r'OWNED BY ([^,\.]+)', pi.upper())
    if not m:
        m = re.search(r'HOLDS THE [A-Z ]*PATENT [^(]*\((.*?)\)', pi.upper())
    if not m:
        m = re.search(r'^(.*?) HOLDS', pi, flags=re.IGNORECASE)
    if m:
        assignee = m.group(1).strip()
    else:
        # fallback: try until 'holds' or 'has' token
        parts = re.split(r' holds | is owned by | owned by | is assigned to | has publication', pi, flags=re.IGNORECASE)
        if parts:
            assignee = parts[0].strip()
    if not assignee:
        assignee = pi.split(' ')[0]
    assignee_norm = re.sub(r'[^A-Z0-9 &\-\.]+',' ', assignee.upper()).strip()
    if 'UNIV' in assignee_norm and 'CALIFORNIA' in assignee_norm:
        continue
    # primary cpc
    primary_code = None
    cpc_field = rec.get('cpc')
    if cpc_field:
        try:
            cpcs = json.loads(cpc_field)
        except:
            cpcs = []
        for it in cpcs:
            if isinstance(it, dict) and it.get('first'):
                primary_code = it.get('code')
                break
        if not primary_code and cpcs:
            if isinstance(cpcs[0], dict):
                primary_code = cpcs[0].get('code')
    if not primary_code:
        primary_code = None
    if assignee_norm not in assignee_to_codes:
        assignee_to_codes[assignee_norm] = set()
    if primary_code:
        assignee_to_codes[assignee_norm].add(primary_code)
        all_codes.add(primary_code)

print('__RESULT__:')
print(json.dumps({'univ_pubnums':sorted(list(univ_pubnums)),'assignees': {k:list(v) for k,v in assignee_to_codes.items()}, 'codes': sorted(list(all_codes))}))"""

env_args = {'var_call_5I4DtjpcM4Fv7fjmRPlhswNj': 'file_storage/call_5I4DtjpcM4Fv7fjmRPlhswNj.json', 'var_call_3VyetCwrZExI2Xpet9Um2Z3I': 'file_storage/call_3VyetCwrZExI2Xpet9Um2Z3I.json', 'var_call_aQiaaKewuvuNUgNV4DvyEt09': {'pairs': [], 'codes': []}, 'var_call_dEoQDTzU3g8MBJxJTTtcYTmC': 'file_storage/call_dEoQDTzU3g8MBJxJTTtcYTmC.json', 'var_call_nxN5eBvJXYwbAZgZ0FnUqKrV': [], 'var_call_Lb2aFYNCzIUGMiHjFYMERzCW': 'file_storage/call_Lb2aFYNCzIUGMiHjFYMERzCW.json'}

exec(code, env_args)
