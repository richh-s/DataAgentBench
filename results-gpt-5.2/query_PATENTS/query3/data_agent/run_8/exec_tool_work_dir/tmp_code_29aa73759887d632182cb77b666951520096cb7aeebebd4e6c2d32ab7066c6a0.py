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
    m=re.search(r"pub\.?\s*number\s+([A-Z]{2}-[0-9A-Z\-]+)" , patents_info)
    if not m:
        m=re.search(r"publication\s+no\.?\s+([A-Z]{2}-[0-9A-Z\-]+)", patents_info)
    if not m:
        m=re.search(r"publication\s+number\s+([A-Z]{2}-[0-9A-Z\-]+)", patents_info)
    return m.group(1) if m else None

def parse_cpc_first(cpc_str: str):
    if not cpc_str:
        return []
    try:
        arr=json.loads(cpc_str)
        return [x.get('code') for x in arr if x and x.get('first')==True and x.get('code')]
    except Exception:
        return []

def to_subclass(code:str):
    # e.g. A61K47/595 -> A61K47/00 ; Y02B30/00 -> Y02B30/00
    m=re.match(r"^([A-Z]\d{2}[A-Z]\d+)/(\d+)$", code)
    if m:
        return f"{m.group(1)}/00"
    # already /00 or non-matching; keep
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

# UC owned publications set
uc_recs=load(var_call_pMEYCGMYMQKF7xLdXIS4aZG0)
uc_pubs=set()
for r in uc_recs:
    pn=extract_pubnum(r.get('Patents_info',''))
    if pn:
        uc_pubs.add(pn)

# all citing patents with citations and cpc
all_recs=load(var_call_a7WH1TvEKIIEHk5IX28MYHVl)
links=[]
for r in all_recs:
    citing_assignee=extract_assignee(r.get('Patents_info',''))
    if not citing_assignee or citing_assignee.upper().startswith('UNIV CALIFORNIA'):
        continue
    cits=parse_citations(r.get('citation',''))
    if not cits:
        continue
    # does it cite any UC pub?
    hit=[pn for pn in cits if pn in uc_pubs]
    if not hit:
        continue
    cpc_first=parse_cpc_first(r.get('cpc',''))
    subclasses=sorted(set(to_subclass(c) for c in cpc_first if c))
    for sc in subclasses:
        links.append({'citing_assignee': citing_assignee, 'cpc_subclass': sc})

df=pd.DataFrame(links).drop_duplicates()

# collect subclass list for querying titles
subclasses=sorted(df['cpc_subclass'].dropna().unique().tolist())
print('__RESULT__:')
print(json.dumps({'n_citing_pairs': int(len(df)), 'n_subclasses': len(subclasses), 'subclasses': subclasses[:50], 'assignees': sorted(df.citing_assignee.unique().tolist())[:50]}))"""

env_args = {'var_call_1rYrvyDMz1z3QQtjsFzHstWw': ['publicationinfo'], 'var_call_Ms9eMaShBwv17k0wWTZQFXz7': [], 'var_call_5eTr8UabZxWiZbQfiXRw0lFv': [], 'var_call_47XoEKYUkAFjoJCttXjRK0gU': 'file_storage/call_47XoEKYUkAFjoJCttXjRK0gU.json', 'var_call_C9RLBBJLeuadpJoDEshNxw3R': ['cpc_definition'], 'var_call_5nl6c85ItrHDBnsYe6dKNRfh': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_call_ufRM2y4QHSgCdLLpWiiplGL4': {'n_citation_links': 75, 'sample': [{'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'US-4599677-A'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'US-2015129765-A1'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'FR-3105380-A1'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'US-11466906-B2'}, {'citing_assignee': 'CALIFORNIA INST OF TECHN', 'cited_pub': 'US-4766142-A'}]}, 'var_call_OlRG6Acxj7oy14uKFE8GEztA': ['UNIV CALIFORNIA', 'CALIFORNIA INST OF TECHN'], 'var_call_pMEYCGMYMQKF7xLdXIS4aZG0': 'file_storage/call_pMEYCGMYMQKF7xLdXIS4aZG0.json', 'var_call_a7WH1TvEKIIEHk5IX28MYHVl': 'file_storage/call_a7WH1TvEKIIEHk5IX28MYHVl.json'}

exec(code, env_args)
