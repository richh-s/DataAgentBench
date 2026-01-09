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

# normalize function for publication numbers
_norm_re = re.compile(r'\s+')

def norm_pn(pn):
    if pn is None:
        return None
    pn=str(pn).strip()
    pn=_norm_re.sub('', pn)
    pn=pn.replace('_','-')
    # ensure format like US-xxxx
    pn=pn.replace('–','-').replace('−','-')
    return pn

uc_norm=set(norm_pn(p) for p in uc_pubnums if p)

matches=[]
for r in all_citing:
    cit=r.get('citation','')
    if not (isinstance(cit,str) and cit.strip().startswith('[')):
        continue
    try:
        cit_list=json.loads(cit)
    except Exception:
        continue
    for c in cit_list:
        pn=norm_pn(c.get('publication_number'))
        if pn in uc_norm:
            matches.append({'citing_patents_info':r.get('Patents_info','')[:200], 'matched_pn':pn})
            break

print('__RESULT__:')
print(json.dumps({'uc_norm_count':len(uc_norm), 'num_citing_rows_found':len(matches), 'sample_matches':matches[:5]}))"""

env_args = {'var_call_23VvrFdA40JcWZBuqH9jRbLo': ['publicationinfo'], 'var_call_7lw1L8BPzvfVu1w1VqgpeU3c': ['cpc_definition'], 'var_call_kiOeirk9Z6qjJK8KB6oCKo89': [], 'var_call_L8fDs73ZbOWv1aufcn7fQYRG': 'file_storage/call_L8fDs73ZbOWv1aufcn7fQYRG.json', 'var_call_FMaB2Nlmx7boT6wAirTHAU4w': {'uc_publications_count': 58, 'unique_cited_pubnums_in_uc_patents': 1112, 'sample_uc_pubnums': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C']}, 'var_call_83ldsRl8mhGM7kfK3kFRZn1Q': 'file_storage/call_83ldsRl8mhGM7kfK3kFRZn1Q.json', 'var_call_XNsF3hYBG1Oal0f5hfp0VBr6': {'pairs': [], 'count_pairs': 0, 'count_assignees': 0}}

exec(code, env_args)
