code = """import json, re

# Load UC pubs
with open(var_call_uvI2aAReL1EIyoQzvdd975yY, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

pub_re = re.compile(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)')

def extract_pub(pinfo:str):
    if not pinfo:
        return None
    m = pub_re.search(pinfo)
    return m.group(1) if m else None

uc_pubs = set(filter(None, (extract_pub(r.get('Patents_info','')) for r in uc_rows)))

# Load all citing candidates
with open(var_call_MJEd5NvKxBOqGSkxGceBre3H, 'r', encoding='utf-8') as f:
    citing_rows = json.load(f)

# regex for assignee from Patents_info
assignee_re = re.compile(r'^(.+?)\s+holds\b')

def extract_assignee(pinfo:str):
    if not pinfo:
        return None
    m = assignee_re.search(pinfo)
    if m:
        return m.group(1).strip()
    # alternative wording
    m = re.search(r'^In [A-Z]{2},\s+the .*? is (?:owned by|assigned to)\s+(.+?)\s+and has', pinfo)
    if m:
        return m.group(1).strip()
    return None

# parse cpc primary (first=true) -> subclass (4 chars) and gather

def parse_primary_subclasses(cpc_str):
    if not cpc_str:
        return set()
    try:
        arr = json.loads(cpc_str)
    except Exception:
        return set()
    subs=set()
    for o in arr:
        if isinstance(o, dict) and o.get('first') is True and 'code' in o:
            code=o['code']
            subs.add(code[:4])
    return subs

# parse citations list and check intersection with uc_pubs

def cites_uc(citation_str):
    if not citation_str:
        return False
    try:
        arr=json.loads(citation_str)
    except Exception:
        return False
    for o in arr:
        if isinstance(o, dict):
            pn=o.get('publication_number')
            if pn in uc_pubs:
                return True
    return False

pairs=set()
for r in citing_rows:
    if not cites_uc(r.get('citation')):
        continue
    assignee = extract_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee.upper() or 'UNIVERSITY OF CALIFORNIA' in assignee.upper():
        continue
    for sub in parse_primary_subclasses(r.get('cpc')):
        pairs.add((assignee, sub))

pairs_sorted = sorted(pairs)

print('__RESULT__:')
print(json.dumps({'pair_count': len(pairs_sorted), 'pairs': pairs_sorted[:50]}))"""

env_args = {'var_call_YgowPBKHhXY5o2brkI4UJaYV': [], 'var_call_PJuXR6cD4jOjJNzoV5V1CUJU': 'file_storage/call_PJuXR6cD4jOjJNzoV5V1CUJU.json', 'var_call_v4YEqqXSReRaZdU3Iv4eBvOJ': ['publicationinfo'], 'var_call_SRdGpWawm7GMalN0gLjD3xat': ['cpc_definition'], 'var_call_uvI2aAReL1EIyoQzvdd975yY': 'file_storage/call_uvI2aAReL1EIyoQzvdd975yY.json', 'var_call_yMekXpvCW9FgQeWudppiFHUv': {'uc_pub_count': 114}, 'var_call_MJEd5NvKxBOqGSkxGceBre3H': 'file_storage/call_MJEd5NvKxBOqGSkxGceBre3H.json'}

exec(code, env_args)
