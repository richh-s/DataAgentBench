code = """import json, re, pandas as pd
from pathlib import Path

def load_records(x):
    if isinstance(x, str) and x.endswith('.json') and Path(x).exists():
        return json.load(open(x,'r',encoding='utf-8'))
    return x

uc_recs = load_records(var_call_fFngABqbPTYeNh9mZGcg98nw)
all_recs = load_records(var_call_nMZK8LL7ZeOangfkUSEz78Fg)

pub_re = re.compile(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', re.I)
assg_res = [
    re.compile(r'owned by\s+([^\.]+)', re.I),
    re.compile(r'assigned to\s+([^\.]+)', re.I),
    re.compile(r'^([^\.]+?)\s+holds the', re.I)
]

def extract_pub(pi):
    m=pub_re.search(pi or '')
    return m.group(1).upper() if m else None

def extract_assignee(pi):
    s=pi or ''
    for rx in assg_res:
        m=rx.search(s)
        if m:
            return m.group(1).strip()
    return None

def parse_jsonish(s):
    if s is None:
        return []
    if isinstance(s,(list,dict)):
        return s
    st=str(s).strip()
    if st=='' or st=='[]':
        return []
    try:
        return json.loads(st)
    except Exception:
        return []

uc_pubs=set(filter(None,(extract_pub(r.get('Patents_info','')) for r in uc_recs)))

out=[]
for r in all_recs:
    cites=parse_jsonish(r.get('citation'))
    cited_pubs=set()
    for c in cites if isinstance(cites,list) else []:
        if isinstance(c,dict) and c.get('publication_number'):
            cited_pubs.add(str(c['publication_number']).upper())
    if not (cited_pubs & uc_pubs):
        continue
    assg=extract_assignee(r.get('Patents_info',''))
    if not assg or 'UNIV CALIFORNIA' in assg.upper():
        continue
    cpcs=parse_jsonish(r.get('cpc'))
    primary=[x.get('code') for x in cpcs if isinstance(cpcs,list) and isinstance(x,dict) and x.get('first')==True and x.get('code')]
    for code in primary:
        m=re.match(r'^([A-HY]\d{2}[A-Z])', code)
        if m:
            out.append({'citing_assignee':assg, 'primary_cpc_subclass':m.group(1)})

res_df=pd.DataFrame(out).drop_duplicates()
print('__RESULT__:')
print(json.dumps({'n_rows': int(len(res_df)), 'n_assignees': int(res_df.citing_assignee.nunique()) if len(res_df)>0 else 0, 'n_subclasses': int(res_df.primary_cpc_subclass.nunique()) if len(res_df)>0 else 0, 'sample': res_df.head(10).to_dict(orient='records')}))"""

env_args = {'var_call_BqFBih7gQaqIxBlVRthiRuTU': ['publicationinfo'], 'var_call_jto7NMN8HlbGcKqShFKjzGug': ['cpc_definition'], 'var_call_qRWQTJABX8lc4IPA6CVXZtuH': 'file_storage/call_qRWQTJABX8lc4IPA6CVXZtuH.json', 'var_call_4BrysovM4ieWkXrEYOajkq7H': {'uc_pub_count': 59}, 'var_call_nMZK8LL7ZeOangfkUSEz78Fg': 'file_storage/call_nMZK8LL7ZeOangfkUSEz78Fg.json', 'var_call_EB3aTh6vzGcOVcpfDhT1HB60': {'rows': 0, 'cols': [], 'head': []}, 'var_call_bZ175VH1VbtempXLSoGZxaC7': {'sample_uc_pubs': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2'], 'sample_citing_citations': ['JP-H01209663-A', 'JP-H0737617-A', 'WO-9744842-A1', 'JP-H09330720-A', 'JP-H10294100-A'], 'overlap_in_first_2000': 0, 'total_uc_pubs': 59, 'total_citing_checked': 2000}, 'var_call_fFngABqbPTYeNh9mZGcg98nw': 'file_storage/call_fFngABqbPTYeNh9mZGcg98nw.json', 'var_call_vQZGmhsldCvQaFu2X3Wa0XeD': {'uc_pub_count': 34, 'unique_cited_by_uc': 1112, 'sample_cited': ['CN-101061570-A', 'CN-101086963-A', 'CN-101631902-A', 'CN-102964610-A', 'CN-103224947-A', 'CN-103233028-A', 'CN-103343120-A', 'CN-104264260-A', 'CN-106880693-A', 'CN-107058224-A', 'CN-1237247-A', 'CN-1346403-A', 'CN-1413250-A', 'CN-85101623-A', 'DE-1509371-A1', 'EP-0111214-A2', 'EP-0399833-A1', 'EP-0474891-A1', 'EP-0474894-A1', 'EP-0476808-A1']}}

exec(code, env_args)
