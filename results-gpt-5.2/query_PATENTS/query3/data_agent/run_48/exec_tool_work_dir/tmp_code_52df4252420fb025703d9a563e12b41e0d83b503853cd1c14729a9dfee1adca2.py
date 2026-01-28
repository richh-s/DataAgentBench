code = """import json, re

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

all_pubs = load_records(var_call_NroPSr8KWeFNwOsE3Qzqb8Rv)
cpc_defs = load_records(var_call_8GGYsLd0C75M2hfVRT2gvpjY)

sym2title = {r['symbol']: r.get('titleFull') for r in cpc_defs if r.get('symbol')}

# extract UC publication numbers from all_pubs where assignee contains UNIV CALIFORNIA

def extract_assignee(pi):
    m = re.search(r"(?:owned by|assigned to)\s+(.+?)\s+and has", pi, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip().strip('.')
    m = re.search(r"^(.+?)\s+holds\b", pi, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip().strip('.')
    return None

def extract_pubnum(pi):
    for pat in [r"pub\. number\s+([A-Z]{2}-[0-9A-Z]+(?:-[A-Z0-9]+)?)\.", r"publication number\s+([A-Z]{2}-[0-9A-Z]+(?:-[A-Z0-9]+)?)\."]:
        m=re.search(pat, pi)
        if m:
            return m.group(1)
    return None

def parse_json_list(s):
    if s is None:
        return []
    if isinstance(s, list):
        return s
    s=str(s).strip()
    if not s or s=='[]':
        return []
    try:
        return json.loads(s)
    except Exception:
        return []

def cpc_to_subclass(code):
    if not code:
        return None
    m=re.match(r"^([A-HY][0-9]{2}[A-Z])", code)
    return m.group(1) if m else None

def primary_subclass(cpc_field):
    cpcs=parse_json_list(cpc_field)
    # choose entries with first==true; if none, take first code
    first_codes=[e.get('code') for e in cpcs if isinstance(e, dict) and e.get('first') is True and e.get('code')]
    code = first_codes[0] if first_codes else (cpcs[0].get('code') if cpcs and isinstance(cpcs[0], dict) else None)
    return cpc_to_subclass(code)

uc_pubnums=set()
for r in all_pubs:
    pi=r.get('Patents_info','') or ''
    ass=extract_assignee(pi) or ''
    if 'UNIV CALIFORNIA' in ass.upper():
        pn=extract_pubnum(pi)
        if pn:
            uc_pubnums.add(pn)

# Find citing assignees (exclude UC) whose citation list includes any UC pubnum
pairs=set()
for r in all_pubs:
    pi=r.get('Patents_info','') or ''
    citing_ass=extract_assignee(pi)
    if not citing_ass:
        continue
    if 'UNIV CALIFORNIA' in citing_ass.upper():
        continue
    cites=parse_json_list(r.get('citation'))
    cited_pubs=set()
    for c in cites:
        if isinstance(c, dict):
            pn=c.get('publication_number')
            if pn:
                cited_pubs.add(pn)
    if not (cited_pubs & uc_pubnums):
        continue
    sub=primary_subclass(r.get('cpc'))
    if not sub:
        continue
    title=sym2title.get(sub)
    if not title:
        continue
    pairs.add((citing_ass, title))

out=[{'citing_assignee': a, 'cpc_subclass_titleFull': t} for a,t in sorted(pairs)]
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aEurZQskU9RMtLPBF2ylKUbf': 'file_storage/call_aEurZQskU9RMtLPBF2ylKUbf.json', 'var_call_8GGYsLd0C75M2hfVRT2gvpjY': 'file_storage/call_8GGYsLd0C75M2hfVRT2gvpjY.json', 'var_call_WWNsGNhSmW2vLT58moQX1G97': {'uc_publications': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2'], 'uc_publications_count': 112}, 'var_call_NroPSr8KWeFNwOsE3Qzqb8Rv': 'file_storage/call_NroPSr8KWeFNwOsE3Qzqb8Rv.json'}

exec(code, env_args)
