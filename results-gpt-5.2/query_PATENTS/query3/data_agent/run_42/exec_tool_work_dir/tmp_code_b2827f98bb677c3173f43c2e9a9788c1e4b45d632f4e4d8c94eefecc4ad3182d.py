code = """import json, re, pandas as pd
from pathlib import Path

def load_records(x):
    if isinstance(x, str) and x.endswith('.json') and Path(x).exists():
        with open(x,'r',encoding='utf-8') as f:
            return json.load(f)
    return x

uc_recs = load_records(var_call_qRWQTJABX8lc4IPA6CVXZtuH)
all_citing = load_records(var_call_nMZK8LL7ZeOangfkUSEz78Fg)

pub_re = re.compile(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', re.I)
assg_res = [
    re.compile(r'owned by\s+([^\.]+)', re.I),
    re.compile(r'assigned to\s+([^\.]+)', re.I),
    re.compile(r'^([^\.]+?)\s+holds the', re.I)
]

def extract_pub(pi):
    m = pub_re.search(pi or '')
    return m.group(1).upper() if m else None

def extract_assignee(pi):
    s = pi or ''
    for rx in assg_res:
        m = rx.search(s)
        if m:
            return m.group(1).strip()
    return None

def parse_jsonish(s):
    if s is None:
        return []
    if isinstance(s, (list, dict)):
        return s
    st = str(s).strip()
    if st == '':
        return []
    try:
        return json.loads(st)
    except Exception:
        return []

uc_pubs = set()
for r in uc_recs:
    pub = extract_pub(r.get('Patents_info',''))
    if pub:
        uc_pubs.add(pub)

out=[]
for r in all_citing:
    cites = parse_jsonish(r.get('citation'))
    cited_pubs=set()
    if isinstance(cites, list):
        for c in cites:
            if isinstance(c, dict):
                pn=c.get('publication_number')
                if pn:
                    cited_pubs.add(str(pn).upper())
    if not (cited_pubs & uc_pubs):
        continue
    assg=extract_assignee(r.get('Patents_info',''))
    if not assg:
        continue
    if 'UNIV CALIFORNIA' in assg.upper():
        continue
    cpcs=parse_jsonish(r.get('cpc'))
    primary=[]
    if isinstance(cpcs, list):
        primary=[x.get('code') for x in cpcs if isinstance(x,dict) and x.get('first')==True and x.get('code')]
    for code in primary:
        m=re.match(r'^([A-HY]\d{2}[A-Z])', code)
        subclass=m.group(1) if m else None
        if subclass:
            out.append({'citing_assignee':assg.strip(), 'primary_cpc_subclass':subclass})

res_df=pd.DataFrame(out).drop_duplicates()
subclasses=sorted(res_df['primary_cpc_subclass'].dropna().unique().tolist())
assignees=sorted(res_df['citing_assignee'].dropna().unique().tolist())

print('__RESULT__:')
print(json.dumps({'n_pairs': int(len(res_df)), 'n_assignees': len(assignees), 'n_subclasses': len(subclasses), 'subclasses': subclasses}))"""

env_args = {'var_call_BqFBih7gQaqIxBlVRthiRuTU': ['publicationinfo'], 'var_call_jto7NMN8HlbGcKqShFKjzGug': ['cpc_definition'], 'var_call_qRWQTJABX8lc4IPA6CVXZtuH': 'file_storage/call_qRWQTJABX8lc4IPA6CVXZtuH.json', 'var_call_4BrysovM4ieWkXrEYOajkq7H': {'uc_pub_count': 59}, 'var_call_nMZK8LL7ZeOangfkUSEz78Fg': 'file_storage/call_nMZK8LL7ZeOangfkUSEz78Fg.json'}

exec(code, env_args)
