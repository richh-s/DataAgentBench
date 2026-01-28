code = """import json, re
# load full publicationinfo result
path = var_call_5I4DtjpcM4Fv7fjmRPlhswNj
with open(path, 'r') as f:
    records = json.load(f)

univ_pubnums = set()
# regex to find publication numbers like US-11081687-B2, WO-..., JP-..., KR-..., US-2002...-A1, etc.
pubnum_re = re.compile(r'\b[A-Z]{2}-[0-9]{4,}[A-Z0-9\-]*\b')
for rec in records:
    pi = rec.get('Patents_info') or ''
    if 'UNIV' in pi.upper() and 'CALIFORNIA' in pi.upper():
        m = pubnum_re.search(pi)
        if m:
            univ_pubnums.add(m.group(0))
# also try variants like 'publication no. US-11124615-B2' or 'publication number US-11081687-B2'

# Now scan all records to find citations to these pubnums
assignee_to_codes = {}
all_codes = set()

for rec in records:
    citations = rec.get('citation') or []
    # citation may be string; handle
    if isinstance(citations, str):
        try:
            citations = json.loads(citations)
        except:
            citations = []
    cited_pubnums = set()
    for c in citations:
        if not isinstance(c, dict):
            continue
        pnum = (c.get('publication_number') or '').strip()
        if pnum:
            cited_pubnums.add(pnum)
    if not (cited_pubnums & univ_pubnums):
        continue
    # this record cites a Univ California patent
    pi = rec.get('Patents_info') or ''
    assignee = None
    # try several patterns
    patterns = [r'^(.*?) holds', r'owned by ([^,\.]+)', r'is owned by ([^,\.]+)', r'^(.*?) has publication', r'^(.*?) has the US', r'^(.*?) holds the', r'^(.*?),', r'^(.*?)\s\(']
    for pat in patterns:
        m = re.search(pat, pi, flags=re.IGNORECASE)
        if m:
            g = m.group(1) if '()' not in pat else m.group(1)
            if g:
                assignee = g.strip()
                break
    if not assignee:
        # fallback: take first 4 words
        assignee = ' '.join(pi.split()[:4])
    # clean assignee
    assignee_norm = re.sub(r'[^A-Z0-9 &\-\.]+',' ', assignee.upper()).strip()
    # exclude Univ California
    if 'UNIV' in assignee_norm and 'CALIFORNIA' in assignee_norm:
        continue
    # get primary CPC code
    cpc_field = rec.get('cpc')
    primary_code = None
    if cpc_field:
        try:
            cpc_list = json.loads(cpc_field)
        except:
            cpc_list = []
        if isinstance(cpc_list, list):
            for item in cpc_list:
                if isinstance(item, dict) and item.get('first'):
                    primary_code = item.get('code')
                    break
            if not primary_code and len(cpc_list)>0:
                first_item = cpc_list[0]
                if isinstance(first_item, dict):
                    primary_code = first_item.get('code')
    if not primary_code:
        primary_code = None
    # record
    if assignee_norm not in assignee_to_codes:
        assignee_to_codes[assignee_norm] = set()
    if primary_code:
        assignee_to_codes[assignee_norm].add(primary_code)
        all_codes.add(primary_code)

# prepare output
out_pairs = []
for a, codes in assignee_to_codes.items():
    out_pairs.append({'assignee': a, 'codes': sorted(list(codes))})

result = {'pairs': out_pairs, 'codes': sorted(list(all_codes))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5I4DtjpcM4Fv7fjmRPlhswNj': 'file_storage/call_5I4DtjpcM4Fv7fjmRPlhswNj.json', 'var_call_3VyetCwrZExI2Xpet9Um2Z3I': 'file_storage/call_3VyetCwrZExI2Xpet9Um2Z3I.json'}

exec(code, env_args)
