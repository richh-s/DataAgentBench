code = """import json, re
# load UNIV CALIFORNIA records
path_univ = var_call_gDrSP1Sva9xFHcnb3CZWe5Hy
with open(path_univ, 'r', encoding='utf-8') as f:
    univ_records = json.load(f)
# load all records with citations
path_with_cit = var_call_oKnfuZPM2rRjOch4s2WsCqEb
with open(path_with_cit, 'r', encoding='utf-8') as f:
    with_cit_records = json.load(f)
# extract publication numbers from univ records
pub_pattern = re.compile(r"[A-Z]{2}-[0-9A-Z\-]+")
univ_pubnums = set()
for rec in univ_records:
    pi = rec.get('Patents_info','')
    for m in pub_pattern.findall(pi):
        univ_pubnums.add(m.strip())
# Also try to parse publication number mention like 'publication number US-xxx' in other formats; already covered

# function to extract assignee from Patents_info
def extract_assignee(text):
    if not text or not isinstance(text, str):
        return None
    # Try multiple regex patterns
    patterns = [
        r"^(.*?) holds the",
        r"is owned by ([A-Z0-9 &\.-]+?)(?: and|,| with|\.|$)",
        r"is assigned to ([A-Z0-9 &\.-]+?)(?: and|,| with|\.|$)",
        r"assigned to ([A-Z0-9 &\.-]+?)(?: and|,| with|\.|$)",
        r"^(.+?) holds the US",
        r"^(.+?) holds the patent",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            name = m.group(1).strip()
            # cleanup trailing phrases
            name = re.sub(r"\s+\(.*\)$", "", name)
            return name.upper()
    # fallback: take leading token before ' the ' or before ' patent '
    m = re.match(r"^([A-Z0-9 &\.-]+?)\b", text)
    if m:
        return m.group(1).strip().upper()
    return None

assignee_to_cpcs = {}
matched_citing_records = []
for rec in with_cit_records:
    cit = rec.get('citation','')
    try:
        cit_list = json.loads(cit)
    except Exception:
        cit_list = []
    cited_pubnums = set()
    for c in cit_list:
        pn = c.get('publication_number') if isinstance(c, dict) else None
        if pn:
            cited_pubnums.add(pn.strip())
    # intersection
    if univ_pubnums & cited_pubnums:
        # this record cites a UNIV CALIF patent
        assignee = extract_assignee(rec.get('Patents_info',''))
        if not assignee:
            continue
        if 'UNIV CALIF' in assignee or 'UNIVERSITY OF CALIFORNIA' in assignee or 'UNIVERSITY CALIF' in assignee:
            # exclude UNIV CALIFORNIA itself
            continue
        # parse CPC
        cpc_field = rec.get('cpc','')
        try:
            cpc_list = json.loads(cpc_field)
        except Exception:
            cpc_list = []
        primary_code = None
        for c in cpc_list:
            if isinstance(c, dict) and c.get('first'):
                primary_code = c.get('code')
                break
        if not primary_code and cpc_list:
            # take first code
            first = cpc_list[0]
            if isinstance(first, dict):
                primary_code = first.get('code')
        if not primary_code:
            continue
        assignee_to_cpcs.setdefault(assignee, set()).add(primary_code)
        matched_citing_records.append({'rowid': rec.get('rowid'), 'assignee': assignee, 'primary_cpc': primary_code})

# prepare outputs
assignee_map = {k: sorted(list(v)) for k,v in assignee_to_cpcs.items()}
unique_cpcs = sorted({code for codes in assignee_map.values() for code in codes})
result = {'assignee_to_cpcs': assignee_map, 'unique_cpcs': unique_cpcs, 'matched_count': len(matched_citing_records)}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_gDrSP1Sva9xFHcnb3CZWe5Hy': 'file_storage/call_gDrSP1Sva9xFHcnb3CZWe5Hy.json', 'var_call_eWOblcZdr0yKyeHcZjYuDGdv': 'file_storage/call_eWOblcZdr0yKyeHcZjYuDGdv.json', 'var_call_oKnfuZPM2rRjOch4s2WsCqEb': 'file_storage/call_oKnfuZPM2rRjOch4s2WsCqEb.json'}

exec(code, env_args)
