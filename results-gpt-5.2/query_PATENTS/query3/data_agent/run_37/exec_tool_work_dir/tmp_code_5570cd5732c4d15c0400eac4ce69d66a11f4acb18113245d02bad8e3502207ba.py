code = """import json, re, pandas as pd

# Load large query result
path = var_call_Wp1cJFhxJ95itKiyJEfq9T95
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def extract_pub_number(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)\b', patents_info)
    if m:
        return m.group(1)
    m = re.search(r'publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)\b', patents_info)
    if m:
        return m.group(1)
    return None

def extract_assignee(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r'is (?:owned by|assigned to)\s+(.+?)\s+(?:and has|with pub\.|and has publication|and has pub\.)', patents_info)
    if m:
        return m.group(1).strip(' .')
    m = re.search(r'^(.+?)\s+holds\s+the\s+', patents_info)
    if m:
        return m.group(1).strip(' .')
    return None

# Build mapping of UC patents: publication_number -> primary CPC subclass (first==true) symbol prefix 4 chars
uc_rows=[]
for r in recs:
    assignee = extract_assignee(r.get('Patents_info',''))
    if not assignee or 'UNIV CALIFORNIA' not in assignee:
        continue
    pub = extract_pub_number(r.get('Patents_info',''))
    if not pub:
        continue
    cpc_raw = r.get('cpc')
    primary_subclasses=set()
    if cpc_raw:
        try:
            cpcs = json.loads(cpc_raw)
        except Exception:
            cpcs=[]
        for c in cpcs:
            if c.get('first') is True and c.get('code'):
                code=c['code']
                subclass = re.match(r'^([A-Z]\d{2}[A-Z])', code)
                if subclass:
                    primary_subclasses.add(subclass.group(1))
    for sc in primary_subclasses:
        uc_rows.append({'uc_pub':pub, 'uc_primary_subclass':sc})

uc_df = pd.DataFrame(uc_rows).drop_duplicates()
uc_pubs = set(uc_df['uc_pub'].tolist())

# Now find citing publications that cite any UC pub
# query db for any row with citation containing 'US-' etc is huge; instead use already fetched recs? Not enough.
# We'll scan full publicationinfo table for citations referencing UC pubs via SQL LIKE ORs in chunks.

import sqlite3

# connect to the sqlite file behind logical db is not available; but we can re-query via tool. We'll generate queries in python? can't.

# Instead: use the loaded subset recs to extract citations to UC? This subset is UC-assigned only, not citing.

result = {'error':'Need broader citation search than current extraction; please allow table scan query.'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cGYV4EzbzLcu7btsG54GNN9l': ['publicationinfo'], 'var_call_HljcxoqtuUiRffWjKX9wzs2M': ['cpc_definition'], 'var_call_Wp1cJFhxJ95itKiyJEfq9T95': 'file_storage/call_Wp1cJFhxJ95itKiyJEfq9T95.json'}

exec(code, env_args)
