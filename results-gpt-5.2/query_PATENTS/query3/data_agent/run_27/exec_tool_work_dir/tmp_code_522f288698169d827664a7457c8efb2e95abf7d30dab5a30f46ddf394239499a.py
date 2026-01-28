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
        uc_pubnums.add(m.group(1))

# build pairs: (assignee, primary_cpc_subclass)
rows=[]
for r in all_citing:
    cit=r.get('citation','')
    if not (isinstance(cit,str) and cit.strip().startswith('[')):
        continue
    try:
        cit_list=json.loads(cit)
    except Exception:
        continue
    cites_uc=False
    for c in cit_list:
        pn=c.get('publication_number')
        if pn in uc_pubnums:
            cites_uc=True
            break
    if not cites_uc:
        continue
    pi=r.get('Patents_info','')
    # assignee is before ' holds' or 'In US, the ... is assigned to'
    m=re.match(r'^(.+?)\s+holds\s+the\s+', pi)
    if not m:
        m=re.search(r'is\s+(?:assigned|owned)\s+by\s+([^\s].+?)(?:\s+and\s+has|\s+with|\.)', pi)
    assignee=m.group(1).strip() if m else None
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee:
        continue
    # primary CPC subclass: from cpc json entries where first==true; take code and reduce to subclass (first 4 + letter?) Actually CPC subclass is like A61K; take first 4 chars.
    cpc=r.get('cpc','')
    primary_sub=None
    if isinstance(cpc,str) and cpc.strip().startswith('['):
        try:
            cpc_list=json.loads(cpc)
            first_codes=[e.get('code') for e in cpc_list if e.get('first')==True and e.get('code')]
            code=first_codes[0] if first_codes else (cpc_list[0].get('code') if cpc_list else None)
            if code:
                primary_sub=code[:4]
        except Exception:
            pass
    if primary_sub:
        rows.append({'assignee':assignee,'subclass':primary_sub})

# unique pairs
uniq=sorted({(r['assignee'], r['subclass']) for r in rows})
print('__RESULT__:')
print(json.dumps({'pairs':uniq, 'count_pairs':len(uniq), 'count_assignees':len({a for a,_ in uniq})}))"""

env_args = {'var_call_23VvrFdA40JcWZBuqH9jRbLo': ['publicationinfo'], 'var_call_7lw1L8BPzvfVu1w1VqgpeU3c': ['cpc_definition'], 'var_call_kiOeirk9Z6qjJK8KB6oCKo89': [], 'var_call_L8fDs73ZbOWv1aufcn7fQYRG': 'file_storage/call_L8fDs73ZbOWv1aufcn7fQYRG.json', 'var_call_FMaB2Nlmx7boT6wAirTHAU4w': {'uc_publications_count': 58, 'unique_cited_pubnums_in_uc_patents': 1112, 'sample_uc_pubnums': ['AU-2003297741-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C']}, 'var_call_83ldsRl8mhGM7kfK3kFRZn1Q': 'file_storage/call_83ldsRl8mhGM7kfK3kFRZn1Q.json'}

exec(code, env_args)
