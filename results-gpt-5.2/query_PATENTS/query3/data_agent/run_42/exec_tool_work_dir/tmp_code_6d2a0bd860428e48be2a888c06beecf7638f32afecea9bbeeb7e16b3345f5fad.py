code = """import json, re
from pathlib import Path

def load_records(x):
    if isinstance(x, str) and x.endswith('.json') and Path(x).exists():
        return json.load(open(x,'r',encoding='utf-8'))
    return x

uc_recs = load_records(var_call_qRWQTJABX8lc4IPA6CVXZtuH)
all_citing = load_records(var_call_nMZK8LL7ZeOangfkUSEz78Fg)

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

# sample first 5 UC pubs
sample_uc=list(sorted(uc_pubs))[:5]

# find one record in all_citing whose citation contains any 'US-' and show first 3 cited pubs
sample_cited=[]
for r in all_citing[:200]:
    cites=parse_jsonish(r.get('citation'))
    pubs=[c.get('publication_number') for c in cites if isinstance(c,dict) and c.get('publication_number')]
    if pubs:
        sample_cited=pubs[:5]
        break

# compute overlap count quickly by scanning 2000 records
overlap=0
for r in all_citing[:2000]:
    cites=parse_jsonish(r.get('citation'))
    for c in cites if isinstance(cites,list) else []:
        pn=c.get('publication_number') if isinstance(c,dict) else None
        if pn and str(pn).upper() in uc_pubs:
            overlap +=1
            break

print('__RESULT__:')
print(json.dumps({'sample_uc_pubs': sample_uc, 'sample_citing_citations': sample_cited, 'overlap_in_first_2000': overlap, 'total_uc_pubs': len(uc_pubs), 'total_citing_checked': min(2000,len(all_citing))}))"""

env_args = {'var_call_BqFBih7gQaqIxBlVRthiRuTU': ['publicationinfo'], 'var_call_jto7NMN8HlbGcKqShFKjzGug': ['cpc_definition'], 'var_call_qRWQTJABX8lc4IPA6CVXZtuH': 'file_storage/call_qRWQTJABX8lc4IPA6CVXZtuH.json', 'var_call_4BrysovM4ieWkXrEYOajkq7H': {'uc_pub_count': 59}, 'var_call_nMZK8LL7ZeOangfkUSEz78Fg': 'file_storage/call_nMZK8LL7ZeOangfkUSEz78Fg.json', 'var_call_EB3aTh6vzGcOVcpfDhT1HB60': {'rows': 0, 'cols': [], 'head': []}}

exec(code, env_args)
