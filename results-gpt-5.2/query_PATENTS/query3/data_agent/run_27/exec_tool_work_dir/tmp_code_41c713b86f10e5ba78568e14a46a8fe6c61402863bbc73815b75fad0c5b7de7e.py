code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

uc_recs = load_records(var_call_L8fDs73ZbOWv1aufcn7fQYRG)
all_citing = load_records(var_call_83ldsRl8mhGM7kfK3kFRZn1Q)

# UC publication numbers set
uc_pubnums=set()
for r in uc_recs:
    pi=r.get('Patents_info','')
    m=re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+[^\s\.,]*)', pi)
    if m:
        uc_pubnums.add(m.group(1).strip())

_norm_re=re.compile(r'\s+')

def norm_pn(pn):
    if pn is None:
        return None
    pn=str(pn).strip()
    pn=_norm_re.sub('', pn)
    pn=pn.replace('–','-').replace('−','-')
    return pn

uc_norm=set(norm_pn(p) for p in uc_pubnums if p)

pairs=set()
for r in all_citing:
    cit=r.get('citation','')
    if not (isinstance(cit,str) and cit.strip().startswith('[')):
        continue
    try:
        cit_list=json.loads(cit)
    except Exception:
        continue
    if not any(norm_pn(c.get('publication_number')) in uc_norm for c in cit_list):
        continue
    pi=r.get('Patents_info','')
    m=re.match(r'^(.+?)\s+holds\s+the\s+', pi)
    if not m:
        m=re.search(r'is\s+held\s+by\s+([^\s].+?)(?:\s+and\s+has|\s+with|\.)', pi)
    if not m:
        m=re.search(r'is\s+(?:assigned|owned)\s+by\s+([^\s].+?)(?:\s+and\s+has|\s+with|\.)', pi)
    assignee=m.group(1).strip() if m else None
    if not assignee or 'UNIV CALIFORNIA' in assignee:
        continue
    cpc=r.get('cpc','')
    subclass=None
    if isinstance(cpc,str) and cpc.strip().startswith('['):
        try:
            cpc_list=json.loads(cpc)
            first_codes=[e.get('code') for e in cpc_list if e.get('first')==True and e.get('code')]
            code=first_codes[0] if first_codes else (cpc_list[0].get('code') if cpc_list else None)
            if code:
                subclass=code[:4]
        except Exception:
            pass
    if subclass:
        pairs.add((assignee,subclass))

print('__RESULT__:')
print(json.dumps({'pairs':sorted(list(pairs))}))"""

env_args = {'var_call_23VvrFdA40JcWZBuqH9jRbLo': ['publicationinfo'], 'var_call_7lw1L8BPzvfVu1w1VqgpeU3c': ['cpc_definition'], 'var_call_kiOeirk9Z6qjJK8KB6oCKo89': [], 'var_call_L8fDs73ZbOWv1aufcn7fQYRG': 'file_storage/call_L8fDs73ZbOWv1aufcn7fQYRG.json', 'var_call_FMaB2Nlmx7boT6wAirTHAU4w': {'uc_publications_count': 58, 'unique_cited_pubnums_in_uc_patents': 1112, 'sample_uc_pubnums': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C']}, 'var_call_83ldsRl8mhGM7kfK3kFRZn1Q': 'file_storage/call_83ldsRl8mhGM7kfK3kFRZn1Q.json', 'var_call_XNsF3hYBG1Oal0f5hfp0VBr6': {'pairs': [], 'count_pairs': 0, 'count_assignees': 0}, 'var_call_aYHyNXmliH2JM8HMGwJJqexY': {'uc_norm_count': 59, 'num_citing_rows_found': 1, 'sample_matches': [{'citing_patents_info': 'The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.', 'matched_pn': 'US-6767662-B2'}]}}

exec(code, env_args)
