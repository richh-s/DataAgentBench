code = """import json, re, ast
# load UNIV CALIFORNIA records
var_univ = var_call_cc68Z6aX2MXH8DgcWXYV034B
if isinstance(var_univ, str):
    with open(var_univ, 'r', encoding='utf-8') as f:
        univ_records = json.load(f)
else:
    univ_records = var_univ

# extract publication numbers of UNIV CALIFORNIA patents from Patents_info
pub_regex = re.compile(r"\b[A-Z]{2,3}-\d{4,}[A-Z0-9-]*\b")
univ_pubnums = set()
for r in univ_records:
    pi = r.get('Patents_info','') or ''
    for m in pub_regex.findall(pi):
        univ_pubnums.add(m)
# Also check if publication number occurs elsewhere (title_localized? not needed)

# load all publication records
var_all = var_call_eiXMVRbHEswgJ2rp1nTqEsy4
if isinstance(var_all, str):
    with open(var_all, 'r', encoding='utf-8') as f:
        all_records = json.load(f)
else:
    all_records = var_all

# helper to parse citation field
def parse_json_field(val):
    if not val:
        return []
    if isinstance(val, list):
        return val
    try:
        return json.loads(val)
    except Exception:
        try:
            return ast.literal_eval(val)
        except Exception:
            return []

# keywords to split assignee name
keywords = [' holds the', ' is assigned to', ' is owned by', ' belongs to', ' is belonging to', ' held by', ' is belonging to', ' is belonging to', ' is assigned to', ' from ', ' belonging to ', ' assigned to '] 
# better regex to capture leading assignee
assignee_split_re = re.compile(r'^(.*?)\s+(?:holds the|is assigned to|is owned by|belongs to|held by|is belonging to|is assigned to|owns|has pub\.|with pub\.|with publication|with publication number|has publication|has pub\.|has publication number)')

assignee_map = {}  # assignee -> set of cpc codes
code_set = set()

for r in all_records:
    cit = r.get('citation','') or ''
    cit_arr = parse_json_field(cit)
    cited_pubnums = {it.get('publication_number','').strip() for it in cit_arr if isinstance(it, dict) and it.get('publication_number')}
    # if intersects with univ_pubnums
    if univ_pubnums and cited_pubnums.intersection(univ_pubnums):
        # exclude if this record itself is UNIV CALIFORNIA
        pi = (r.get('Patents_info') or '').upper()
        if 'UNIV CALIFORNIA' in pi:
            continue
        # extract assignee
        pat = assignee_split_re.search(r.get('Patents_info',''))
        if pat:
            assignee = pat.group(1).strip()
        else:
            # fallback: take up to first comma
            pi_orig = r.get('Patents_info','')
            assignee = pi_orig.split(',')[0].strip()
        if not assignee:
            assignee = 'UNKNOWN'
        # parse cpc primary codes
        cpc_field = r.get('cpc','') or ''
        cpc_arr = parse_json_field(cpc_field)
        primary_codes = []
        for c in cpc_arr:
            if isinstance(c, dict) and c.get('first'):
                code = c.get('code')
                if code:
                    primary_codes.append(code)
        # if none marked first, take first code entries
        if not primary_codes:
            for c in cpc_arr[:1]:
                if isinstance(c, dict) and c.get('code'):
                    primary_codes.append(c.get('code'))
        if not primary_codes:
            primary_codes = []
        # update map
        assignee_map.setdefault(assignee, set()).update(primary_codes)
        for cc in primary_codes:
            code_set.add(cc)

# prepare results
results = []
for a, codes in assignee_map.items():
    results.append({'assignee': a, 'cpc_codes': sorted(list(codes))})

out = {'assignees': results, 'cpc_codes': sorted(list(code_set)), 'num_univ_pubs': len(univ_pubnums)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cc68Z6aX2MXH8DgcWXYV034B': 'file_storage/call_cc68Z6aX2MXH8DgcWXYV034B.json', 'var_call_r1rLlChnwgV9fpjtfBZ4FUB9': [], 'var_call_gpK3xriqZczE4HtoLAE6feqr': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'], 'var_call_aImyVbUV9Z2hMgiWtgSxfFfT': 'file_storage/call_aImyVbUV9Z2hMgiWtgSxfFfT.json', 'var_call_eiXMVRbHEswgJ2rp1nTqEsy4': 'file_storage/call_eiXMVRbHEswgJ2rp1nTqEsy4.json'}

exec(code, env_args)
