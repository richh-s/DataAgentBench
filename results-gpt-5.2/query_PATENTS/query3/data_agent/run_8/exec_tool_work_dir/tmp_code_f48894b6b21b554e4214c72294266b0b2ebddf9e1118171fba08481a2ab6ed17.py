code = """import json, re
import pandas as pd

def load(x):
    if isinstance(x,str):
        with open(x,'r',encoding='utf-8') as f:
            return json.load(f)
    return x

def extract_assignee(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r"owned by ([^,\.]+)", patents_info, flags=re.IGNORECASE)
    if not m:
        return None
    s=m.group(1).strip()
    s=re.sub(r"\s+and\s+has\s+pub.*$","",s,flags=re.IGNORECASE).strip()
    return s

def extract_pubnum(patents_info: str):
    if not patents_info:
        return None
    for pat in [r"pub\.?\s*number\s+([A-Z]{2}-[0-9A-Z\-]+)", r"publication\s+no\.?\s+([A-Z]{2}-[0-9A-Z\-]+)", r"publication\s+number\s+([A-Z]{2}-[0-9A-Z\-]+)"]:
        m=re.search(pat, patents_info)
        if m:
            return m.group(1)
    return None

def parse_cpc_first(cpc_str: str):
    if not cpc_str:
        return []
    try:
        arr=json.loads(cpc_str)
        return [x.get('code') for x in arr if x and x.get('first')==True and x.get('code')]
    except Exception:
        return []

def to_subclass(code:str):
    m=re.match(r"^([A-Z]\d{2}[A-Z]\d+)/(\d+)$", code)
    if m:
        return f"{m.group(1)}/00"
    return code

def parse_citations(citation_str: str):
    if not citation_str:
        return []
    try:
        arr=json.loads(citation_str)
        pubs=[]
        for x in arr:
            pn=(x or {}).get('publication_number')
            if pn:
                pubs.append(pn)
        return pubs
    except Exception:
        return []

uc_recs=load(var_call_pMEYCGMYMQKF7xLdXIS4aZG0)
uc_pubs=set(filter(None,[extract_pubnum(r.get('Patents_info','')) for r in uc_recs]))

all_recs=load(var_call_a7WH1TvEKIIEHk5IX28MYHVl)
links=[]
for r in all_recs:
    citing_assignee=extract_assignee(r.get('Patents_info',''))
    if not citing_assignee:
        continue
    if citing_assignee.strip().upper() in ['UNIV CALIFORNIA','UNIVERSITY OF CALIFORNIA']:
        continue
    hit=False
    for pn in parse_citations(r.get('citation','')):
        if pn in uc_pubs:
            hit=True
            break
    if not hit:
        continue
    subclasses=sorted(set(to_subclass(c) for c in parse_cpc_first(r.get('cpc','')) if c))
    for sc in subclasses:
        links.append({'citing_assignee': citing_assignee, 'cpc_subclass': sc})

df=pd.DataFrame(links).drop_duplicates()
subclasses=sorted(df['cpc_subclass'].dropna().unique().tolist()) if len(df)>0 else []
assignees=sorted(df['citing_assignee'].dropna().unique().tolist()) if len(df)>0 else []
print('__RESULT__:')
print(json.dumps({'n_uc_pubs': len(uc_pubs), 'n_pairs': int(len(df)), 'n_assignees': len(assignees), 'n_subclasses': len(subclasses), 'assignees': assignees, 'subclasses': subclasses}))"""

env_args = {'var_call_1rYrvyDMz1z3QQtjsFzHstWw': ['publicationinfo'], 'var_call_Ms9eMaShBwv17k0wWTZQFXz7': [], 'var_call_5eTr8UabZxWiZbQfiXRw0lFv': [], 'var_call_47XoEKYUkAFjoJCttXjRK0gU': 'file_storage/call_47XoEKYUkAFjoJCttXjRK0gU.json', 'var_call_C9RLBBJLeuadpJoDEshNxw3R': ['cpc_definition'], 'var_call_5nl6c85ItrHDBnsYe6dKNRfh': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_call_ufRM2y4QHSgCdLLpWiiplGL4': {'n_citation_links': 75, 'sample': [{'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'US-4599677-A'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'US-2015129765-A1'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'FR-3105380-A1'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'US-11466906-B2'}, {'citing_assignee': 'CALIFORNIA INST OF TECHN', 'cited_pub': 'US-4766142-A'}]}, 'var_call_OlRG6Acxj7oy14uKFE8GEztA': ['UNIV CALIFORNIA', 'CALIFORNIA INST OF TECHN'], 'var_call_pMEYCGMYMQKF7xLdXIS4aZG0': 'file_storage/call_pMEYCGMYMQKF7xLdXIS4aZG0.json', 'var_call_a7WH1TvEKIIEHk5IX28MYHVl': 'file_storage/call_a7WH1TvEKIIEHk5IX28MYHVl.json'}

exec(code, env_args)
