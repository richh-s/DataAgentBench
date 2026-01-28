code = """import json, re, pandas as pd
from pathlib import Path

def load_records(x):
    if isinstance(x, str) and x.endswith('.json') and Path(x).exists():
        return json.load(open(x,'r',encoding='utf-8'))
    return x

uc_recs = load_records(var_call_fFngABqbPTYeNh9mZGcg98nw)

pub_re = re.compile(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', re.I)

def extract_pub(pi):
    m=pub_re.search(pi or '')
    return m.group(1).upper() if m else None

def parse_jsonish(s):
    if s is None:
        return []
    if isinstance(s,(list,dict)):
        return s
    st=str(s).strip()
    if st=='':
        return []
    try:
        return json.loads(st)
    except Exception:
        return []

uc_pubs=set(filter(None,(extract_pub(r.get('Patents_info','')) for r in uc_recs)))

# collect cited pubs in UC records
cited=set()
for r in uc_recs:
    cites=parse_jsonish(r.get('citation'))
    for c in cites if isinstance(cites,list) else []:
        if isinstance(c,dict) and c.get('publication_number'):
            cited.add(str(c['publication_number']).upper())

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubs), 'unique_cited_by_uc': len(cited), 'sample_cited': sorted(list(cited))[:20]}))"""

env_args = {'var_call_BqFBih7gQaqIxBlVRthiRuTU': ['publicationinfo'], 'var_call_jto7NMN8HlbGcKqShFKjzGug': ['cpc_definition'], 'var_call_qRWQTJABX8lc4IPA6CVXZtuH': 'file_storage/call_qRWQTJABX8lc4IPA6CVXZtuH.json', 'var_call_4BrysovM4ieWkXrEYOajkq7H': {'uc_pub_count': 59}, 'var_call_nMZK8LL7ZeOangfkUSEz78Fg': 'file_storage/call_nMZK8LL7ZeOangfkUSEz78Fg.json', 'var_call_EB3aTh6vzGcOVcpfDhT1HB60': {'rows': 0, 'cols': [], 'head': []}, 'var_call_bZ175VH1VbtempXLSoGZxaC7': {'sample_uc_pubs': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2'], 'sample_citing_citations': ['JP-H01209663-A', 'JP-H0737617-A', 'WO-9744842-A1', 'JP-H09330720-A', 'JP-H10294100-A'], 'overlap_in_first_2000': 0, 'total_uc_pubs': 59, 'total_citing_checked': 2000}, 'var_call_fFngABqbPTYeNh9mZGcg98nw': 'file_storage/call_fFngABqbPTYeNh9mZGcg98nw.json'}

exec(code, env_args)
