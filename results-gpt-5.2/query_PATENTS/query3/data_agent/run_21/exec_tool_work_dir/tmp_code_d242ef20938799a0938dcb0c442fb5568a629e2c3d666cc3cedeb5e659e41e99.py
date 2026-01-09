code = """import json, re
import pandas as pd

# load full result list
path = var_call_E6tbXMkCCY50UNQlzqQSeEjh
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

# Build mapping from UC publication_number to its first CPC subclass (4-char+subclass letter) from primary CPC (first==true)
uc_pubs = set()
uc_pub_to_primary_subclass = {}

for r in recs:
    pi = r.get('Patents_info') or ''
    # extract publication number like US-2022074631-A1
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi)
    if not m:
        m = re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi)
    if not m:
        m = re.search(r'with pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi)
    pub = m.group(1) if m else None
    if pub:
        uc_pubs.add(pub)
    # parse cpc json
    cpc_str = r.get('cpc')
    primary_code = None
    if cpc_str:
        try:
            cpcs = json.loads(cpc_str)
            for e in cpcs:
                if isinstance(e, dict) and e.get('first') is True and e.get('code'):
                    primary_code = e['code']
                    break
        except Exception:
            primary_code = None
    # subclass is first 4 chars (section+class+subclass letter), e.g. F25B
    if pub and primary_code:
        subclass = primary_code[:4]
        uc_pub_to_primary_subclass[pub] = subclass

# Now scan all publicationinfo to find citing patents that cite any UC pub.
# We need to query entire table for Patents_info and citation, but do in sqlite with LIKE for 'US-' etc is hard.
# Instead, query all rows where citation contains any of the UC pubs (OR chain). Limit chain size by batching.

uc_pubs_list = sorted(list(uc_pubs))

# function to batch OR LIKE queries
import sqlite3
con = sqlite3.connect('publication_database')

all_citing = []
B=50
for i in range(0, len(uc_pubs_list), B):
    batch = uc_pubs_list[i:i+B]
    like_clause = ' OR '.join(["citation LIKE '%"+p+"%'" for p in batch])
    q = f"SELECT Patents_info, citation FROM publicationinfo WHERE citation IS NOT NULL AND citation!='[]' AND ({like_clause});"
    df = pd.read_sql_query(q, con)
    if len(df):
        all_citing.append(df)
con.close()

if all_citing:
    citing_df = pd.concat(all_citing, ignore_index=True).drop_duplicates()
else:
    citing_df = pd.DataFrame(columns=['Patents_info','citation'])

# extract citing assignee from Patents_info; exclude UNIV CALIFORNIA itself
rows=[]
for _, row in citing_df.iterrows():
    pi = row['Patents_info'] or ''
    # assignee patterns: 'is owned by X', 'is assigned to X', 'holds the XX patent filing'
    am = re.search(r'(?:owned by|assigned to)\s+([^,.]+)', pi)
    if not am:
        am = re.search(r'^([^,]+?)\s+holds', pi)
    assignee = am.group(1).strip() if am else None
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    # parse citations to find which UC pubs cited
    cited_uc_subclasses=set()
    try:
        cits = json.loads(row['citation'])
    except Exception:
        cits=[]
    for c in cits:
        pn = (c or {}).get('publication_number')
        if pn in uc_pub_to_primary_subclass:
            cited_uc_subclasses.add(uc_pub_to_primary_subclass[pn])
    for sc in cited_uc_subclasses:
        rows.append({'citing_assignee': assignee, 'cpc_subclass': sc})

out_df = pd.DataFrame(rows).drop_duplicates().sort_values(['citing_assignee','cpc_subclass'])
result = out_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ky9p28bfw6ZzpdkIpcICy6Ul': ['publicationinfo'], 'var_call_9FjvG9K7GEUQ2jOWlZFfSjSr': ['cpc_definition'], 'var_call_FPczLPUeIyYnvaQzIKLNGXAr': [], 'var_call_E6tbXMkCCY50UNQlzqQSeEjh': 'file_storage/call_E6tbXMkCCY50UNQlzqQSeEjh.json'}

exec(code, env_args)
