code = """import json
import re

# Load the full publicationinfo query result from storage
path = var_call_uSj2XJbyd96rb50wTleyhl2b
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Helper to extract publication numbers from Patents_info
pubnum_re = re.compile(r'\b[A-Z]{2}-\d{4,11}-[A-Z0-9]+\b')
# fallback pattern without trailing kind
pubnum_re2 = re.compile(r'\b[A-Z]{2}-\d{4,11}\b')

# Helper to extract assignee name heuristically
def extract_assignee(s):
    s = s.strip()
    # common patterns
    patterns = [r'owned by ([A-Z0-9 &,\.\-]+?)(?:\s|,|\.|and|with|has|holds)',
                r'assigned to ([A-Z0-9 &,\.\-]+?)(?:\s|,|\.|and|with|has|holds)',
                r'held by ([A-Z0-9 &,\.\-]+?)(?:\s|,|\.|and|with|has|holds)',
                r'^(?:In [A-Z]{2}, )?([A-Z0-9 &,\.\-]+?) holds',
                r'^(?:In [A-Z]{2}, )?([A-Z0-9 &,\.\-]+?) has',
                r'^(?:In [A-Z]{2}, )?([A-Z0-9 &,\.\-]+?) owns',
                r'^(?:In [A-Z]{2}, )?([A-Z0-9 &,\.\-]+?) (?:filed|appears|appears to)']
    for p in patterns:
        m = re.search(p, s)
        if m:
            name = m.group(1).strip()
            # clean trailing words
            name = re.sub(r'[\.,]$', '', name).strip()
            return name.upper()
    # fallback: take longest uppercase sequence at start
    m = re.match(r'^([A-Z0-9][A-Z0-9 \,\.\-&]{2,})', s)
    if m:
        name = m.group(1).split(' with ')[0].split(' (')[0].strip()
        # remove leading In XX,
        name = re.sub(r'^In [A-Z]{2},\s*', '', name)
        return name.upper()
    return ''

# Build publication number -> assignee mapping
pub_to_assignee = {}
for rec in data:
    s = rec.get('Patents_info','') or ''
    m = pubnum_re.search(s)
    if not m:
        m = pubnum_re2.search(s)
    if m:
        pubnum = m.group(0)
        assignee = extract_assignee(s)
        pub_to_assignee[pubnum] = assignee

# Now find citing patents that cite UNIV CALIFORNIA assigned patents
pairs = set()
codes = set()

for rec in data:
    s = rec.get('Patents_info','') or ''
    citing_assignee = extract_assignee(s)
    # parse citation field
    cit_text = rec.get('citation','') or ''
    cited_list = []
    try:
        cited_list = json.loads(cit_text)
    except Exception:
        # try to find publication numbers in the citation string
        cited_list = []
        for m in pubnum_re.finditer(cit_text):
            cited_list.append({'publication_number': m.group(0)})
        for m in pubnum_re2.finditer(cit_text):
            cited_list.append({'publication_number': m.group(0)})
    # check if any cited publication is assigned to UNIV CALIFORNIA
    cites_uc = False
    for c in cited_list:
        pubn = (c.get('publication_number') or '').strip()
        if not pubn:
            continue
        ass = pub_to_assignee.get(pubn,'').upper()
        if ass == 'UNIV CALIFORNIA':
            cites_uc = True
            break
    if not cites_uc:
        continue
    # exclude if citing assignee is UNIV CALIFORNIA
    if citing_assignee == 'UNIV CALIFORNIA' or citing_assignee == '':
        continue
    # parse cpc to find primary code
    cpc_text = rec.get('cpc','') or ''
    primary_code = None
    try:
        cpc_list = json.loads(cpc_text)
        # find first==true
        for e in cpc_list:
            if e.get('first') is True:
                primary_code = e.get('code')
                break
        if not primary_code and len(cpc_list)>0:
            primary_code = cpc_list[0].get('code')
    except Exception:
        # fallback: extract any CPC-like token
        m = re.search(r'([A-Z0-9]{1,10}\/[0-9]{1,6})', cpc_text)
        primary_code = m.group(0) if m else None
    if primary_code:
        pairs.add((citing_assignee, primary_code))
        codes.add(primary_code)

# Prepare output
pairs_list = sorted([{"assignee": a, "code": c} for (a,c) in pairs], key=lambda x:(x['assignee'], x['code']))
codes_list = sorted(list(codes))

out = {"pairs": pairs_list, "codes": codes_list}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_gsWxlXamH0bH8ljehePMHHM6': ['publicationinfo'], 'var_call_weqzvfBrnc60cyw9FtEWIR77': ['cpc_definition'], 'var_call_tjsA3rOynI5Mzn4kWRCLheXY': 'file_storage/call_tjsA3rOynI5Mzn4kWRCLheXY.json', 'var_call_uSj2XJbyd96rb50wTleyhl2b': 'file_storage/call_uSj2XJbyd96rb50wTleyhl2b.json'}

exec(code, env_args)
