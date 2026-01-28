code = """import json, re
# Load the list of UC publication numbers from var_call_65VdEqZzcrDGysYV4E5QhCUt
path_uc = var_call_65VdEqZzcrDGysYV4E5QhCUt
with open(path_uc, 'r', encoding='utf-8') as f:
    uc_pub_list = json.load(f)
uc_set = set(uc_pub_list)
# Load the publications with citations from var_call_godfpDa7ee2D983skuWmCPYL
path_citing = var_call_godfpDa7ee2D983skuWmCPYL
with open(path_citing, 'r', encoding='utf-8') as f:
    citing_data = json.load(f)

results = []
# helper to parse citation field which may be a JSON string or list
for rec in citing_data:
    cit = rec.get('citation')
    if not cit:
        continue
    # try to load as json
    try:
        cit_list = json.loads(cit)
    except Exception:
        # sometimes stored as already a list
        cit_list = cit if isinstance(cit, list) else []
    # check if any cited publication_number is in uc_set
    cites_uc = False
    for c in cit_list:
        pubnum = c.get('publication_number') if isinstance(c, dict) else None
        if pubnum and pubnum in uc_set:
            cites_uc = True
            break
    if not cites_uc:
        continue
    # extract assignee from Patents_info heuristically
    pi = rec.get('Patents_info','')
    assignee = None
    # common patterns
    patterns = [r'^(.*?)\s+holds\s+the', r'^(.*?)\s+holds\s+the', r'^(.*?)\s+holds\s+', r'^(.*?)\s+is\s+assigned\s+to\s+', r'^(.*?)\s+is\s+owned\s+by\s+', r'^(.*?)\s+is\s+held\s+by\s+', r'^(.*?)\s+has\s+the', r'^(.*?)\s+own(ed|s)\s+the']
    for p in patterns:
        m = re.search(p, pi, re.IGNORECASE)
        if m:
            assignee = m.group(1).strip().strip(',')
            break
    if not assignee:
        # fallback: take first token group before 'the' or before 'patent'
        m = re.split(r'\b(the|patent|application|patent application)\b', pi, flags=re.IGNORECASE)
        if m:
            assignee = m[0].strip().strip(',')
    if not assignee:
        assignee = pi[:80]
    # normalize
    assignee = re.sub(r'\s+', ' ', assignee).strip()
    # exclude UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    # parse cpc
    cpc_field = rec.get('cpc')
    primary_code = None
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        cpc_list = cpc_field if isinstance(cpc_field, list) else []
    if isinstance(cpc_list, list):
        for el in cpc_list:
            if isinstance(el, dict) and el.get('first'):
                primary_code = el.get('code')
                break
        if not primary_code and len(cpc_list)>0 and isinstance(cpc_list[0], dict):
            primary_code = cpc_list[0].get('code')
    # skip if no primary code
    if not primary_code:
        continue
    results.append({'assignee': assignee, 'primary_cpc': primary_code})
# deduplicate pairs
unique = []
seen = set()
for r in results:
    key = (r['assignee'], r['primary_cpc'])
    if key not in seen:
        seen.add(key)
        unique.append({'assignee': r['assignee'], 'primary_cpc': r['primary_cpc']})

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_JkzVcUe9mStTDG8g0enUZ82T': 'file_storage/call_JkzVcUe9mStTDG8g0enUZ82T.json', 'var_call_mN0bvvlQgMe2C2VNhr5mLXV6': 'file_storage/call_mN0bvvlQgMe2C2VNhr5mLXV6.json', 'var_call_65VdEqZzcrDGysYV4E5QhCUt': 'file_storage/call_65VdEqZzcrDGysYV4E5QhCUt.json', 'var_call_godfpDa7ee2D983skuWmCPYL': 'file_storage/call_godfpDa7ee2D983skuWmCPYL.json'}

exec(code, env_args)
