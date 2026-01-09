code = """import json, re, sqlite3
import pandas as pd

# load UC-owned records from file
path = var_call_E6tbXMkCCY50UNQlzqQSeEjh
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

uc_pubs=set()
uc_pub_to_primary_subclass={}

for r in recs:
    pi = r.get('Patents_info') or ''
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi)
    if not m:
        m = re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi)
    if not m:
        m = re.search(r'with pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9]*-[A-Z0-9]+)', pi)
    pub = m.group(1) if m else None
    if pub:
        uc_pubs.add(pub)
    primary_code=None
    cpc_str=r.get('cpc')
    if cpc_str:
        try:
            cpcs=json.loads(cpc_str)
            for e in cpcs:
                if isinstance(e, dict) and e.get('first') is True and e.get('code'):
                    primary_code=e['code']
                    break
        except Exception:
            pass
    if pub and primary_code:
        uc_pub_to_primary_subclass[pub]=primary_code[:4]

uc_pubs_list=sorted(uc_pubs)

# Connect to underlying sqlite db file directly
con = sqlite3.connect('publication_database.sqlite')

all_citing=[]
B=30
for i in range(0,len(uc_pubs_list),B):
    batch=uc_pubs_list[i:i+B]
    like_clause=' OR '.join(["citation LIKE '%"+p+"%'" for p in batch])
    q=f"SELECT Patents_info, citation FROM publicationinfo WHERE citation IS NOT NULL AND citation!='[]' AND ({like_clause});"
    df=pd.read_sql_query(q, con)
    if len(df):
        all_citing.append(df)
con.close()

citing_df=pd.concat(all_citing, ignore_index=True).drop_duplicates() if all_citing else pd.DataFrame(columns=['Patents_info','citation'])

rows=[]
for _, rr in citing_df.iterrows():
    pi=rr['Patents_info'] or ''
    am=re.search(r'(?:owned by|assigned to)\s+([^,.]+)', pi)
    if not am:
        am=re.search(r'^([^,]+?)\s+holds', pi)
    assignee=am.group(1).strip() if am else None
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    try:
        cits=json.loads(rr['citation'])
    except Exception:
        cits=[]
    subclasses=set()
    for c in cits:
        pn=(c or {}).get('publication_number')
        if pn in uc_pub_to_primary_subclass:
            subclasses.add(uc_pub_to_primary_subclass[pn])
    for sc in subclasses:
        rows.append({'citing_assignee':assignee,'cpc_subclass':sc})

out_df=pd.DataFrame(rows).drop_duplicates().sort_values(['citing_assignee','cpc_subclass'])
print('__RESULT__:')
print(json.dumps(out_df.to_dict(orient='records')))"""

env_args = {'var_call_ky9p28bfw6ZzpdkIpcICy6Ul': ['publicationinfo'], 'var_call_9FjvG9K7GEUQ2jOWlZFfSjSr': ['cpc_definition'], 'var_call_FPczLPUeIyYnvaQzIKLNGXAr': [], 'var_call_E6tbXMkCCY50UNQlzqQSeEjh': 'file_storage/call_E6tbXMkCCY50UNQlzqQSeEjh.json'}

exec(code, env_args)
