code = """import json, re
# Load UC publication numbers (from earlier processing)
path_uc = var_call_IYjBMs1tkQ1XxzrTNhLGV0Wl
with open(path_uc, 'r', encoding='utf-8') as f:
    uc_data = json.load(f)
uc_pubs = set(uc_data.get('uc_pub_numbers', []))
# Load non-UC records with citations
path_nonuc = var_call_nBCou4wn7Rs8JeY4pUeQlPqr
with open(path_nonuc, 'r', encoding='utf-8') as f:
    records = json.load(f)

# helper to parse assignee from Patents_info
def parse_assignee(info):
    if not info:
        return ''
    # common delimiters: ' holds the ', ' holds ', ' is assigned to ', ' assigned to ', ' owns ', ' is owned by ', ' holds the US patent ', 'has the US patent'
    patterns = [r'^(.*?)\s+holds\b', r'^(.*?)\s+owns\b', r'^(.*?)\s+is owned by\b', r'^(.*?)\s+is assigned to\b', r'^(.*?)\s+assigned to\b', r'^(.*?)\s+holds the\b', r'^(.*?)\s+has the\b', r'^(.*?)\s+has\b']
    for p in patterns:
        m = re.search(p, info, flags=re.IGNORECASE)
        if m:
            name = m.group(1).strip()
            return name
    # fallback: take up to first comma or ' with '
    m = re.split(r',| with |;|\(|\[', info)
    if m:
        return m[0].strip()
    return info.strip()

results = {}
for r in records:
    info = r.get('Patents_info','') or ''
    citation_text = r.get('citation','') or ''
    cpc_text = r.get('cpc','') or ''
    # parse citation JSON if possible
    try:
        cited = json.loads(citation_text)
    except Exception:
        # try to extract publication numbers via regex
        cited = []
        cited_pubs = re.findall(r'[A-Z]{2}-\d{4,}[-A-Z0-9]*', citation_text)
        for cp in cited_pubs:
            cited.append({'publication_number': cp})
    # check if any cited pub matches UC pubs
    matches = []
    for c in cited:
        pubnum = (c.get('publication_number') or '').strip()
        if pubnum in uc_pubs:
            matches.append(pubnum)
    if matches:
        assignee = parse_assignee(info)
        if not assignee:
            continue
        # ignore UNIV CALIFORNIA
        if re.search(r'UNIV(?:ERSITY)?\.?\s*CALIFORNIA', assignee, flags=re.IGNORECASE):
            continue
        # parse cpc JSON to get primary codes (where first==true)
        primary_codes = set()
        try:
            cpcs = json.loads(cpc_text)
            for e in cpcs:
                try:
                    if e.get('first'):
                        code = e.get('code')
                        if code:
                            primary_codes.add(code.strip())
                except Exception:
                    pass
        except Exception:
            # fallback regex for codes
            codes = re.findall(r'[A-Z]\w?\d+[A-Z]?\d*/\d+', cpc_text)
            for code in codes:
                primary_codes.add(code)
        if not primary_codes:
            # if no primary flagged, try to pick first code in list
            try:
                cpcs = json.loads(cpc_text)
                if isinstance(cpcs, list) and len(cpcs)>0:
                    code = cpcs[0].get('code')
                    if code:
                        primary_codes.add(code.strip())
            except Exception:
                pass
        if primary_codes:
            if assignee not in results:
                results[assignee] = set()
            results[assignee].update(primary_codes)

# convert sets to sorted lists
out = []
for a, codes in results.items():
    out.append({'assignee': a, 'cpc_codes': sorted(codes)})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vMO4SSFPl5xkRPbQmRvesVNp': ['publicationinfo'], 'var_call_XjK1ao19p1kMAkNjSWtWLtsL': ['cpc_definition'], 'var_call_bvwscKjgXSiVzmcGDY8sDDH7': 'file_storage/call_bvwscKjgXSiVzmcGDY8sDDH7.json', 'var_call_1wUCiArK5fhy4meeI5gcsEYD': {'uc_pub_numbers': []}, 'var_call_IYjBMs1tkQ1XxzrTNhLGV0Wl': 'file_storage/call_IYjBMs1tkQ1XxzrTNhLGV0Wl.json', 'var_call_nBCou4wn7Rs8JeY4pUeQlPqr': 'file_storage/call_nBCou4wn7Rs8JeY4pUeQlPqr.json'}

exec(code, env_args)
