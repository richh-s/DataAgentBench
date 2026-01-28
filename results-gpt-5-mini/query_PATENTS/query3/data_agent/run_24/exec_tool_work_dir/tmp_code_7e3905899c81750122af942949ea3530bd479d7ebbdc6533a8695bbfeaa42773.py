code = """import json, re
# load files
path_uc = var_call_tjsA3rOynI5Mzn4kWRCLheXY
path_all = var_call_uSj2XJbyd96rb50wTleyhl2b
with open(path_uc, 'r', encoding='utf-8') as f:
    uc_data = json.load(f)
with open(path_all, 'r', encoding='utf-8') as f:
    all_data = json.load(f)

# regex to extract publication numbers like US-2022074631-A1 or US-11466906-B2 or WO-...
pub_re = re.compile(r'\b[A-Z]{2}-[0-9]{4,12}(?:-[A-Z0-9]+)?\b')

uc_pubs = set()
for rec in uc_data:
    s = rec.get('Patents_info','') or ''
    for m in pub_re.finditer(s):
        uc_pubs.add(m.group(0))

# fallback: also check citation fields inside uc_data
for rec in uc_data:
    cit = rec.get('citation','') or ''
    try:
        cl = json.loads(cit)
        for c in cl:
            pn = (c.get('publication_number') or '').strip()
            if pn:
                uc_pubs.add(pn)
    except Exception:
        for m in pub_re.finditer(cit):
            uc_pubs.add(m.group(0))

# helper to detect UC assignee
def is_uc(name):
    if not name:
        return False
    name_u = name.upper()
    if 'UNIV' in name_u and 'CALIFORNIA' in name_u:
        return True
    if 'UNIVERSITY OF CALIFORNIA' in name_u:
        return True
    return False

# helper to extract assignee
def extract_assignee(s):
    s = (s or '').strip()
    patterns = [r'owned by ([A-Z0-9 &\.,\-]+?)(?:\s|,|\.|and|with|has|holds)',
                r'assigned to ([A-Z0-9 &\.,\-]+?)(?:\s|,|\.|and|with|has|holds)',
                r'held by ([A-Z0-9 &\.,\-]+?)(?:\s|,|\.|and|with|has|holds)',
                r'^(?:In [A-Z]{2}, )?([A-Z0-9 &\.,\-]+?) holds',
                r'^(?:In [A-Z]{2}, )?([A-Z0-9 &\.,\-]+?) has',
                r'^(?:In [A-Z]{2}, )?([A-Z0-9 &\.,\-]+?) owns',
                r'^(?:In [A-Z]{2}, )?([A-Z0-9 &\.,\-]+?) (?:filed|appears|appears to)']
    for p in patterns:
        m = re.search(p, s, re.IGNORECASE)
        if m:
            name = m.group(1).strip()
            name = re.sub(r'[\.,]$', '', name).strip()
            return name
    # fallback: take first sequence before 'holds' or 'has'
    m = re.match(r'^([A-Za-z0-9 &\.,\-]{3,100})', s)
    if m:
        return m.group(1).strip()
    return ''

pairs = set()
codes = set()

for rec in all_data:
    cit_text = rec.get('citation','') or ''
    cited_pubs = []
    try:
        cited_pubs = json.loads(cit_text)
    except Exception:
        # find pub-like tokens
        for m in pub_re.finditer(cit_text):
            cited_pubs.append({'publication_number': m.group(0)})
    # check if any cited pub is in uc_pubs
    cites = False
    for c in cited_pubs:
        pn = (c.get('publication_number') or '').strip()
        if pn and pn in uc_pubs:
            cites = True
            break
    if not cites:
        continue
    citing_assignee = extract_assignee(rec.get('Patents_info','') or '')
    if is_uc(citing_assignee):
        continue
    if not citing_assignee:
        continue
    # get primary cpc
    primary = None
    cpc_text = rec.get('cpc','') or ''
    try:
        cl = json.loads(cpc_text)
        for e in cl:
            if e.get('first') is True:
                primary = e.get('code')
                break
        if not primary and len(cl)>0:
            primary = cl[0].get('code')
    except Exception:
        m = pub_re.search(cpc_text)
        primary = m.group(0) if m else None
    if not primary:
        continue
    pairs.add((citing_assignee.strip(), primary.strip()))
    codes.add(primary.strip())

result = {"pairs": sorted([{"assignee": a, "code": c} for (a,c) in pairs], key=lambda x:(x['assignee'], x['code'])),
          "codes": sorted(list(codes))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_gsWxlXamH0bH8ljehePMHHM6': ['publicationinfo'], 'var_call_weqzvfBrnc60cyw9FtEWIR77': ['cpc_definition'], 'var_call_tjsA3rOynI5Mzn4kWRCLheXY': 'file_storage/call_tjsA3rOynI5Mzn4kWRCLheXY.json', 'var_call_uSj2XJbyd96rb50wTleyhl2b': 'file_storage/call_uSj2XJbyd96rb50wTleyhl2b.json', 'var_call_kYlzlUWo5eXA7pqnDn7VJWw3': {'pairs': [], 'codes': []}}

exec(code, env_args)
