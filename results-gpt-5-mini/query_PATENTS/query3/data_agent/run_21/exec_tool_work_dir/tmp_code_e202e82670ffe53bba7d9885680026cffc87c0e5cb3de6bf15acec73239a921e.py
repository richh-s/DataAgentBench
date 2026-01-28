code = """import json, re
# load UC-assigned records and full publicationinfo
uc_records = json.load(open(var_call_FWaq87obpvltPwUmTRpRaycV, 'r'))
all_records = json.load(open(var_call_tgrM8QNXraQ65lKZy8S0oDdF, 'r'))

# extract UC publication numbers from uc_records by parsing Patents_info and also citation fields
uc_pubnums = set()
pat_regex = re.compile(r"[A-Z]{2}-[0-9A-Za-z\-]+")
for rec in uc_records:
    text = (rec.get('Patents_info') or '') + '\n' + (rec.get('citation') or '')
    for m in pat_regex.findall(text):
        uc_pubnums.add(m)

# normalize: ensure no short tokens like 'AM-dependent' (seen previously). Keep those that match country codes of 2 letters then dash then digits
uc_pubnums = {p for p in uc_pubnums if re.match(r'^[A-Z]{2}-\d', p)}

# iterate all_records and find citing records where citation JSON contains any of uc_pubnums
citing = []
for rec in all_records:
    cit_text = rec.get('citation') or ''
    if not cit_text or cit_text.strip()=='[]':
        continue
    # try to parse as JSON
    try:
        cit_list = json.loads(cit_text)
    except Exception:
        # fallback: find publication-like tokens in text
        found = set(pat_regex.findall(cit_text))
        cit_list = []
        for f in found:
            cit_list.append({'publication_number': f})
    # check if any cited publication_number in uc_pubnums
    cited_any = False
    for c in cit_list:
        pubn = c.get('publication_number','')
        if pubn in uc_pubnums:
            cited_any = True
            break
    if not cited_any:
        continue
    # extract assignee from Patents_info using heuristics
    pinfo = rec.get('Patents_info','')
    assignee = None
    patterns = [
        r'is owned by ([^,\.;\n]+)',
        r'is assigned to ([^,\.;\n]+)',
        r'holds the .*?\((?:ID )?([^\)]+)\), with publication',
        r'^(.*?) holds the',
        r'^(.*?) owns the',
        r'^(.*?) is the owner of',
        r'^(.*?)\s+has the',
        r'^(.*?) holds the',
        r'^(.*?) owns',
        r'^(.*?)\s+\(',
    ]
    for pat in patterns:
        m = re.search(pat, pinfo, re.IGNORECASE)
        if m:
            candidate = m.group(1).strip()
            # remove trailing phrases like 'and has pub.'
            candidate = re.split(r'\s+and\s+has|\s+with\s+pub|,|;|\.|\s+with\s+application', candidate, maxsplit=1)[0].strip()
            # Ignore if candidate is short or contains 'the application'
            if len(candidate)>1 and 'application' not in candidate.lower():
                assignee = candidate
                break
    if not assignee:
        # fallback: try to take leading token up to 'holds' or 'has'
        m = re.match(r'([^,\n]+?)\s+(holds|has|owns|is)', pinfo, re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        assignee = pinfo.strip()[:80]
    # parse cpc field
    cpc_text = rec.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_text)
    except Exception:
        # find codes via regex
        codes = pat_regex.findall(cpc_text)
        cpc_list = [{'code':c} for c in codes]
    primary_code = None
    # cpc_list may contain dicts with 'code' and 'first'
    if isinstance(cpc_list, list) and cpc_list:
        for e in cpc_list:
            if isinstance(e, dict) and e.get('first'):
                primary_code = e.get('code')
                break
        if not primary_code:
            # pick first element's code
            first = cpc_list[0]
            if isinstance(first, dict):
                primary_code = first.get('code')
            else:
                primary_code = first
    if not primary_code:
        continue
    # skip if assignee is UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    citing.append({'rowid': rec.get('rowid'), 'assignee': assignee, 'primary_cpc': primary_code})

# deduplicate by assignee and primary_cpc
pairs = []
seen = set()
for c in citing:
    key = (c['assignee'], c['primary_cpc'])
    if key in seen:
        continue
    seen.add(key)
    pairs.append({'assignee': c['assignee'], 'cpc_code': c['primary_cpc']})

# collect unique cpc codes
cpc_codes = sorted({p['cpc_code'] for p in pairs})
output = {'pairs': pairs, 'cpc_codes': cpc_codes}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_FWaq87obpvltPwUmTRpRaycV': 'file_storage/call_FWaq87obpvltPwUmTRpRaycV.json', 'var_call_xPULEoxuCI0R7gn4s9WmVLxr': 'file_storage/call_xPULEoxuCI0R7gn4s9WmVLxr.json', 'var_call_tgrM8QNXraQ65lKZy8S0oDdF': 'file_storage/call_tgrM8QNXraQ65lKZy8S0oDdF.json'}

exec(code, env_args)
