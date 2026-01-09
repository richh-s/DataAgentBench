code = """import json, re
import pandas as pd

# load UC cited pubs + subclasses from earlier by recomputing quickly from var_call_Qt...
uc_src = var_call_QtSufoFOi6RQJdWNZm6rLZoQ
if isinstance(uc_src, str):
    with open(uc_src,'r',encoding='utf-8') as f:
        uc_recs = json.load(f)
else:
    uc_recs = uc_src

rows=[]
for r in uc_recs:
    try:
        citations=json.loads(r.get('citation') or '[]')
    except Exception:
        citations=[]
    try:
        cpcs=json.loads(r.get('cpc') or '[]')
    except Exception:
        cpcs=[]
    primary=[c.get('code') for c in cpcs if isinstance(c,dict) and c.get('first') is True and c.get('code')]
    subclasses=sorted(set([p.replace(' ','')[:4] for p in primary if len(p.replace(' ',''))>=4]))
    for c in citations:
        pn=c.get('publication_number')
        if pn:
            for sc in subclasses:
                rows.append((pn,sc))
uc_map=pd.DataFrame(rows, columns=['uc_cited_pub','uc_primary_subclass']).drop_duplicates()
uc_cited_set=set(uc_map['uc_cited_pub'].unique().tolist())

# load potential citing patents records
src=var_call_WiAfJCV9JuY3DCFbgE51X515
if isinstance(src,str):
    with open(src,'r',encoding='utf-8') as f:
        citing_recs=json.load(f)
else:
    citing_recs=src

assignee_pat=re.compile(r"(?:owned by|assigned to|holds the [A-Z]{2} patent filing).*? ([A-Z0-9&\-\.\s]+?) (?:and has|with publication|has publication|has pub\.|,)", re.IGNORECASE)
assignee_simple=re.compile(r"^(.*?) holds the ", re.IGNORECASE)

def parse_assignee(pi):
    if not pi: return None
    m=assignee_simple.search(pi)
    if m:
        return m.group(1).strip()
    m2=re.search(r"(?:owned by|assigned to) ([^.,]+)", pi, re.IGNORECASE)
    if m2:
        return m2.group(1).strip()
    return None

def norm(s):
    return re.sub(r"\s+"," ",(s or '').strip().upper())

out=[]
for r in citing_recs:
    ass=parse_assignee(r.get('Patents_info'))
    if not ass: 
        continue
    try:
        citations=json.loads(r.get('citation') or '[]')
    except Exception:
        citations=[]
    cited_pubs=[c.get('publication_number') for c in citations if isinstance(c,dict) and c.get('publication_number')]
    # intersect
    hit=set(cited_pubs).intersection(uc_cited_set)
    if not hit:
        continue
    for pn in hit:
        subs=uc_map.loc[uc_map.uc_cited_pub==pn,'uc_primary_subclass'].unique().tolist()
        for sc in subs:
            out.append({'citing_assignee': ass.strip(), 'uc_cited_pub': pn, 'uc_primary_subclass': sc})

out_df=pd.DataFrame(out).drop_duplicates()
# exclude UNIV CALIFORNIA itself
out_df=out_df[out_df['citing_assignee'].str.upper().ne('UNIV CALIFORNIA')]
# aggregate unique subclasses per assignee
agg=(out_df.groupby('citing_assignee')['uc_primary_subclass']
     .apply(lambda x: sorted(set(x.tolist())))
     .reset_index())

print('__RESULT__:')
print(json.dumps({'n_citing_assignees': int(agg.shape[0]), 'assignee_subclasses': agg.to_dict(orient='records')}))"""

env_args = {'var_call_vUJMPfY6dnH3TNkgowJsOtGq': ['publicationinfo'], 'var_call_x8ZBV1E4gydbt2vDZIO64V0x': ['cpc_definition'], 'var_call_QtSufoFOi6RQJdWNZm6rLZoQ': 'file_storage/call_QtSufoFOi6RQJdWNZm6rLZoQ.json', 'var_call_2umzUbakrhvWg1WZOXw6OoCV': {'n_uc_patents': 169, 'n_cited_pubs': 1112, 'subclasses': ['A01D', 'A61B', 'A61K', 'A61L', 'A61N', 'A61P', 'B01L', 'B25J', 'C07D', 'C07H', 'C07K', 'C08B', 'C08F', 'C08G', 'C08J', 'C08K', 'C08L', 'C09C', 'C09D', 'C12N', 'C12P', 'C12Q', 'C30B', 'E04H', 'F16K', 'F25B', 'G01J', 'G01N', 'G01R', 'G01S', 'G01T', 'G01V', 'H01L', 'H01M', 'H01S', 'H03H', 'H04B', 'H04J', 'H04L']}, 'var_call_WiAfJCV9JuY3DCFbgE51X515': 'file_storage/call_WiAfJCV9JuY3DCFbgE51X515.json'}

exec(code, env_args)
