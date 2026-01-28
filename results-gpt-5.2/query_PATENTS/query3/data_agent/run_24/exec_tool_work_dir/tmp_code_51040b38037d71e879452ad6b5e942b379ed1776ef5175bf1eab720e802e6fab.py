code = """import json, re

# load UC pubs
with open(var_call_uMQByuYhjtuOxhdCT5ngThYN, 'r', encoding='utf-8') as f:
    uc_recs = json.load(f)

def extract_pub_number(patents_info: str):
    if not patents_info:
        return None
    for pat in [r"pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", r"publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)"]:
        m = re.search(pat, patents_info)
        if m:
            return m.group(1)
    return None

def extract_assignee(patents_info: str):
    if not patents_info:
        return None
    # formats: "X holds the US patent application..." or "In US, the application ... is owned by X and ..."
    m = re.match(r"^(.*?) holds the ", patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r"is owned by (.*?) and has", patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r"is assigned to (.*?) and has", patents_info)
    if m:
        return m.group(1).strip()
    m = re.search(r"owned by (.*?)\.", patents_info)
    if m:
        return m.group(1).strip()
    return None

def extract_primary_subclass(cpc_str: str):
    if not cpc_str:
        return None
    try:
        arr = json.loads(cpc_str)
    except Exception:
        return None
    # choose first==true if present, else first entry
    code = None
    for o in arr:
        if isinstance(o, dict) and o.get('first') is True and o.get('code'):
            code = o['code']
            break
    if not code and arr and isinstance(arr[0], dict):
        code = arr[0].get('code')
    if not code:
        return None
    # derive CPC subclass: letters+digits before '/'
    m = re.match(r"^([A-Z][0-9]{2}[A-Z])", code)
    return m.group(1) if m else None

uc_pub_nums = set(extract_pub_number(r.get('Patents_info','')) for r in uc_recs)
uc_pub_nums.discard(None)

# load all publications and find those citing any UC pub
with open(var_call_KIulsuDhrhljSEmQ6G6f2zBr, 'r', encoding='utf-8') as f:
    all_recs = json.load(f)

pairs = set()  # (assignee, subclass)
for r in all_recs:
    citing_assignee = extract_assignee(r.get('Patents_info',''))
    if not citing_assignee:
        continue
    if 'UNIV CALIFORNIA' in citing_assignee:
        continue
    cit = r.get('citation')
    if not cit:
        continue
    try:
        cits = json.loads(cit)
    except Exception:
        continue
    cited_pubs = set()
    for c in cits:
        if isinstance(c, dict):
            pn = c.get('publication_number')
            if pn:
                cited_pubs.add(pn)
    if not (cited_pubs & uc_pub_nums):
        continue
    subclass = extract_primary_subclass(r.get('cpc'))
    if not subclass:
        continue
    pairs.add((citing_assignee, subclass))

# output unique subclasses for later query
subclasses = sorted({s for _, s in pairs})
result = {
    'pair_count': len(pairs),
    'assignee_count': len({a for a,_ in pairs}),
    'subclass_count': len(subclasses),
    'subclasses': subclasses,
    'pairs': sorted([{'assignee':a,'subclass':s} for a,s in pairs], key=lambda x:(x['assignee'], x['subclass']))
}

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_k78O5d6VNqdn0Sfz6lA2VsNN': ['publicationinfo'], 'var_call_UHXYP2c9u4mFCPdfMa4PRvxZ': ['cpc_definition'], 'var_call_uMQByuYhjtuOxhdCT5ngThYN': 'file_storage/call_uMQByuYhjtuOxhdCT5ngThYN.json', 'var_call_396wJYrPDq6PXFHSZ4rbfbIB': {'uc_pub_count': 114}, 'var_call_KIulsuDhrhljSEmQ6G6f2zBr': 'file_storage/call_KIulsuDhrhljSEmQ6G6f2zBr.json'}

exec(code, env_args)
