code = """import json, re

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

uc_rows = load_records(var_call_podeueb7ZgQ1Fvj9LRgBnJmT)
citing_rows = load_records(var_call_RjFbYg8rlVVbtVPvEEMwOAyx)
cpc_defs = load_records(var_call_tnXJkoGwQIL9QloKmbYghE1p)

# UC publication numbers

def extract_pub_number(patents_info:str):
    if not patents_info:
        return None
    for pat in [r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', r'publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)']:
        m = re.search(pat, patents_info)
        if m:
            return m.group(1)
    return None

uc_pub = set()
for r in uc_rows:
    p = extract_pub_number(r.get('Patents_info',''))
    if p:
        uc_pub.add(p)

# map UC pub -> UC primary CPC subclass (first=true; subclass= first 4 chars of code, e.g., H01M)
# choose first entry with first==true; fall back to first code in list.

def parse_cpc_list(s):
    if not s:
        return []
    try:
        return json.loads(s)
    except Exception:
        return []

def primary_subclass_from_cpc_list(lst):
    if not lst:
        return None
    primary = None
    for e in lst:
        if isinstance(e, dict) and e.get('first') is True and e.get('code'):
            primary = e['code']
            break
    if primary is None:
        for e in lst:
            if isinstance(e, dict) and e.get('code'):
                primary = e['code']
                break
    if not primary:
        return None
    m = re.match(r'^([A-HY]\d{2}[A-Z])', primary)
    return m.group(1) if m else None

uc_pub_to_subclass = {}
for r in uc_rows:
    pub = extract_pub_number(r.get('Patents_info',''))
    if not pub:
        continue
    subclass = primary_subclass_from_cpc_list(parse_cpc_list(r.get('cpc')))
    if subclass:
        uc_pub_to_subclass[pub] = subclass

# CPC title map
cpc_title = {d['symbol']: d.get('titleFull') for d in cpc_defs if isinstance(d, dict) and 'symbol' in d}

# parse citations in citing patents, and if cite UC pubnum, collect citing assignee and subclass title

def extract_assignee(patents_info:str):
    if not patents_info:
        return None
    m = re.search(r'^(.*?)\s+holds\s+the', patents_info)
    if m:
        return m.group(1).strip().strip('.')
    m = re.search(r'(?:owned by|assigned to)\s+(.+?)\s+and has', patents_info)
    if m:
        return m.group(1).strip().strip('.')
    return None

def parse_citation_list(s):
    if not s:
        return []
    try:
        return json.loads(s)
    except Exception:
        return []

pairs=set()
for r in citing_rows:
    assignee = extract_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    if assignee.strip().upper() == 'UNIV CALIFORNIA':
        continue
    cites = parse_citation_list(r.get('citation'))
    for c in cites:
        if not isinstance(c, dict):
            continue
        pn = c.get('publication_number')
        if pn in uc_pub:
            subclass = uc_pub_to_subclass.get(pn)
            if subclass and subclass in cpc_title and cpc_title[subclass]:
                pairs.add((assignee, cpc_title[subclass]))

# sort
out = sorted([{'citing_assignee':a, 'primary_cpc_subclass_title':t} for a,t in pairs], key=lambda x:(x['citing_assignee'], x['primary_cpc_subclass_title']))
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_podeueb7ZgQ1Fvj9LRgBnJmT': 'file_storage/call_podeueb7ZgQ1Fvj9LRgBnJmT.json', 'var_call_tnXJkoGwQIL9QloKmbYghE1p': 'file_storage/call_tnXJkoGwQIL9QloKmbYghE1p.json', 'var_call_vMfoWvFtF5MQSAYLxDQ8og8v': {'uc_publication_numbers': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'where_clause': "citation LIKE '%AU-2003247814-A1%' OR citation LIKE '%AU-2003297741-A1%' OR citation LIKE '%AU-2004253879-A1%' OR citation LIKE '%AU-2005269556-A1%' OR citation LIKE '%AU-2007297661-A1%' OR citation LIKE '%AU-2008349842-A1%' OR citation LIKE '%AU-2010214112-B2%' OR citation LIKE '%AU-2015364602-B2%' OR citation LIKE '%AU-2017356943-A1%' OR citation LIKE '%AU-2019275518-B2%' OR citation LIKE '%AU-2409401-A%' OR citation LIKE '%AU-2898989-A%' OR citation LIKE '%AU-3353000-A%' OR citation LIKE '%AU-5938296-A%' OR citation LIKE '%AU-6535890-A%' OR citation LIKE '%CA-2283629-C%' OR citation LIKE '%CA-2298540-A1%' OR citation LIKE '%CA-2550552-A1%' OR citation LIKE '%CA-2562038-C%' OR citation LIKE '%CA-2718348-C%' OR citation LIKE '%CA-3161617-A1%' OR citation LIKE '%CN-100339724-C%' OR citation LIKE '%CN-101584047-A%' OR citation LIKE '%CN-102067370-B%' OR citation LIKE '%CN-102584712-A%' OR citation LIKE '%CN-103189548-A%' OR citation LIKE '%CN-103687626-A%' OR citation LIKE '%EP-0826155-A4%' OR citation LIKE '%EP-1212462-A1%' OR citation LIKE '%EP-2210307-A4%' OR citation LIKE '%EP-3668487-A4%' OR citation LIKE '%EP-4284234-A1%' OR citation LIKE '%HK-1052178-A1%' OR citation LIKE '%HK-1250569-A1%' OR citation LIKE '%HR-P20201231-T1%' OR citation LIKE '%ID-23426-A%' OR citation LIKE '%IL-244029-A0%' OR citation LIKE '%IL-274176-A%' OR citation LIKE '%JP-2005104983-A%' OR citation LIKE '%JP-2009260386-A%' OR citation LIKE '%JP-2014224156-A%' OR citation LIKE '%JP-S6163700-A%' OR citation LIKE '%KR-20050085437-A%' OR citation LIKE '%KR-20110004413-A%' OR citation LIKE '%KR-20160119166-A%' OR citation LIKE '%KR-20200041324-A%' OR citation LIKE '%MX-2013002850-A%' OR citation LIKE '%PE-20130764-A1%' OR citation LIKE '%PT-2970346-T%' OR citation LIKE '%RO-70061-A%' OR citation LIKE '%TW-201925402-A%' OR citation LIKE '%US-10359432-B2%' OR citation LIKE '%US-10744347-B2%' OR citation LIKE '%US-11014955-B2%' OR citation LIKE '%US-11072681-B2%' OR citation LIKE '%US-11376346-B2%' OR citation LIKE '%US-11421276-B2%' OR citation LIKE '%US-11546022-B2%' OR citation LIKE '%US-11667770-B2%' OR citation LIKE '%US-12025581-B2%' OR citation LIKE '%US-2003112494-A1%' OR citation LIKE '%US-2004115131-A1%' OR citation LIKE '%US-2005234013-A1%' OR citation LIKE '%US-2006051790-A1%' OR citation LIKE '%US-2006292670-A1%' OR citation LIKE '%US-2009031436-A1%' OR citation LIKE '%US-2010025717-A1%' OR citation LIKE '%US-2017087258-A1%' OR citation LIKE '%US-2017145219-A1%' OR citation LIKE '%US-2017281687-A1%' OR citation LIKE '%US-2018243924-A1%' OR citation LIKE '%US-2019169580-A1%' OR citation LIKE '%US-2019209590-A1%' OR citation LIKE '%US-2019328740-A1%' OR citation LIKE '%US-2020025859-A1%' OR citation LIKE '%US-2020283856-A1%' OR citation LIKE '%US-2021000566-A1%' OR citation LIKE '%US-2021002329-A1%' OR citation LIKE '%US-2021039104-A1%' OR citation LIKE '%US-2021101879-A1%' OR citation LIKE '%US-2021181673-A1%' OR citation LIKE '%US-2021282642-A1%' OR citation LIKE '%US-2022018060-A1%' OR citation LIKE '%US-2022074631-A1%' OR citation LIKE '%US-2023155090-A1%' OR citation LIKE '%US-2023171142-A1%' OR citation LIKE '%US-2023279470-A1%' OR citation LIKE '%US-2023321419-A1%' OR citation LIKE '%US-5304932-A%' OR citation LIKE '%US-5547866-A%' OR citation LIKE '%US-6237292-B1%' OR citation LIKE '%US-6750960-B2%' OR citation LIKE '%US-6767662-B2%' OR citation LIKE '%US-6980295-B2%' OR citation LIKE '%US-7052856-B2%' OR citation LIKE '%US-7745569-B2%' OR citation LIKE '%US-9061071-B2%' OR citation LIKE '%WO-2010045542-A3%' OR citation LIKE '%WO-2012158833-A3%' OR citation LIKE '%WO-2012162563-A2%' OR citation LIKE '%WO-2014152660-A1%' OR citation LIKE '%WO-2017136335-A1%' OR citation LIKE '%WO-2017214343-A1%' OR citation LIKE '%WO-2018026404-A3%' OR citation LIKE '%WO-2018067976-A1%' OR citation LIKE '%WO-2019067860-A1%' OR citation LIKE '%WO-2019173834-A1%' OR citation LIKE '%WO-2020055916-A9%' OR citation LIKE '%WO-2021102420-A1%' OR citation LIKE '%WO-2023212447-A2%' OR citation LIKE '%WO-2023225482-A3%' OR citation LIKE '%WO-2023239670-A1%' OR citation LIKE '%WO-2024044766-A3%' OR citation LIKE '%WO-2024112568-A1%'", 'uc_count': 114}, 'var_call_RjFbYg8rlVVbtVPvEEMwOAyx': 'file_storage/call_RjFbYg8rlVVbtVPvEEMwOAyx.json'}

exec(code, env_args)
