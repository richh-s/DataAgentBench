code = """import json, re
import pandas as pd

# load large result
path = var_call_9RVtcJOgzfif5Kwn7XVkpCk3
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def parse_assignee(patents_info: str):
    if not patents_info:
        return None
    # common patterns
    m = re.search(r"owned by ([^\.]+)", patents_info, flags=re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"assigned to ([^\.]+)", patents_info, flags=re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r"assignee(?:_harmonized)?[:\s]+([^\.]+)", patents_info, flags=re.I)
    if m:
        return m.group(1).strip()
    return None

def parse_pub_number(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r"pub\. number\s+([A-Z]{2,}-[0-9A-Z]+-[A-Z0-9]+)", patents_info)
    if m:
        return m.group(1)
    m = re.search(r"publication number\s+([A-Z]{2,}-[0-9A-Z]+-[A-Z0-9]+)", patents_info)
    if m:
        return m.group(1)
    return None

def normalize_pub(pub):
    if not pub:
        return None
    return pub.strip()

def cpc_subclass(code):
    if not code:
        return None
    code = code.strip().replace(' ', '')
    m = re.match(r"^([A-HY]\d{2}[A-Z])", code)
    return m.group(1) if m else None

rows = []
for r in recs:
    assignee = parse_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    if assignee.strip().upper() == 'UNIV CALIFORNIA':
        continue
    # cited pubs
    citation_raw = r.get('citation')
    if not citation_raw:
        continue
    try:
        citations = json.loads(citation_raw) if isinstance(citation_raw, str) else citation_raw
    except Exception:
        continue
    cited_pubs = [c.get('publication_number') for c in citations if isinstance(c, dict) and c.get('publication_number')]
    if not cited_pubs:
        continue
    # primary CPC subclasses for this citing patent
    cpc_raw = r.get('cpc')
    try:
        cpcs = json.loads(cpc_raw) if isinstance(cpc_raw, str) else cpc_raw
    except Exception:
        cpcs = []
    primary_codes = []
    for c in cpcs if isinstance(cpcs, list) else []:
        if isinstance(c, dict) and c.get('first') is True and c.get('code'):
            primary_codes.append(c.get('code'))
    subclasses = sorted({cpc_subclass(c) for c in primary_codes if cpc_subclass(c)})
    for sc in subclasses:
        rows.append({'citing_assignee': assignee.strip(), 'cpc_subclass': sc})

out = pd.DataFrame(rows).drop_duplicates().sort_values(['citing_assignee','cpc_subclass']).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lcjFhTyKzuPLwaCmwJdrVTp8': ['publicationinfo'], 'var_call_PFaRcpbJzb9CLkv748uaflfN': ['cpc_definition'], 'var_call_9RVtcJOgzfif5Kwn7XVkpCk3': 'file_storage/call_9RVtcJOgzfif5Kwn7XVkpCk3.json'}

exec(code, env_args)
