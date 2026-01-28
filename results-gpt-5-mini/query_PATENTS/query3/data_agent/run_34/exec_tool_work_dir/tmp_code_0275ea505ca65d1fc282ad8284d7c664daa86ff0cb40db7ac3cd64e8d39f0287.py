code = """import json, re

# Load full publicationinfo
path = var_call_F0o6KLAYCTaTzUnkOyFIfKph
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load pub_map (pubnum keyed) created earlier
with open(var_call_TN169ZanZUXhtwpDfJvr6vx6, 'r', encoding='utf-8') as f:
    pub_map = json.load(f)

# Load target list of Univ California pubnums
target_list = set(var_call_8dLYepMYcQpSGalErIUrRFS4)

# helper normalize: remove non-alphanumeric and uppercase
norm = lambda s: re.sub(r'[^A-Z0-9]', '', s.upper()) if s else ''

# build normalized mapping for target pubnums
norm_target = {norm(p): p for p in target_list}

# helper to extract assignee from Patents_info
def extract_assignee(s):
    if not s:
        return 'UNKNOWN'
    s = s.strip()
    m = re.search(r'owned by\s+([^,\.]+)', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'is owned by\s+([^,\.]+)', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'held by\s+([^,\.]+)', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'([^,\.]+?)\s+holds the', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'([^,\.]+?)\s+has pub', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    if ',' in s:
        return s.split(',')[0].strip()
    return s[:200]

# helper to detect Univ California
def is_univ_california(name):
    if not name:
        return False
    up = name.upper()
    return ('CALIFORNIA' in up) and (('UNIV' in up) or ('UNIVERSITY' in up) or ('REGENTS' in up))

citing_map = {}

for row in data:
    info = row.get('Patents_info') or ''
    citing_assignee = extract_assignee(info) or 'UNKNOWN'
    if is_univ_california(citing_assignee):
        continue
    citation_field = row.get('citation') or '[]'
    try:
        citations = json.loads(citation_field)
    except Exception:
        citations = []
    cited_any = False
    codes = set()
    for c in citations:
        cited_pub = c.get('publication_number')
        if not cited_pub:
            continue
        n = norm(cited_pub)
        if not n:
            continue
        if n in norm_target:
            cited_any = True
            target_pub = norm_target[n]
            # get primary_codes from pub_map (original keys)
            info_cited = pub_map.get(target_pub)
            if info_cited:
                for pc in info_cited.get('primary_codes', []):
                    if pc:
                        codes.add(pc)
    if cited_any and codes:
        if citing_assignee not in citing_map:
            citing_map[citing_assignee] = set()
        citing_map[citing_assignee].update(codes)

unique_codes = sorted({c for s in citing_map.values() for c in s})

result = {'citing_map': {k: sorted(list(v)) for k,v in citing_map.items()}, 'unique_codes': unique_codes}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QrKpS3xCrEvOFTzyHkiOaGa7': ['publicationinfo'], 'var_call_04o2xQiS5aWuOHXcmBa2upJ6': ['cpc_definition'], 'var_call_iFNFnXpgt1jRdEhcOq4ig4jD': 'file_storage/call_iFNFnXpgt1jRdEhcOq4ig4jD.json', 'var_call_F0o6KLAYCTaTzUnkOyFIfKph': 'file_storage/call_F0o6KLAYCTaTzUnkOyFIfKph.json', 'var_call_euL4YTFiEWaffgYDXkUUpE6y': {'citing_map': {}, 'unique_codes': []}, 'var_call_TN169ZanZUXhtwpDfJvr6vx6': 'file_storage/call_TN169ZanZUXhtwpDfJvr6vx6.json', 'var_call_8dLYepMYcQpSGalErIUrRFS4': ['AU-2001257114-A1', 'AU-2001296493-B2', 'AU-2002254753-B2', 'AU-2003247814-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2009234210-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2898989-A', 'AU-7724398-A', 'CA-2220674-A1', 'CA-2298540-A1', 'CA-2494262-A1', 'CA-2550552-A1', 'CA-2562038-A', 'CA-3055214-A1', 'CA-3161617-A1', 'CA-3225295-A1', 'CN-200380105631-A', 'CN-96195210-A', 'EP-00959970-A', 'EP-00992018-A', 'EP-07753965-A', 'EP-08826523-A', 'EP-21763795-A', 'EP-22746465-A', 'EP-96907882-A', 'IL-14014099-A', 'IL-24402916-A', 'IL-25502617-A', 'IL-27417620-A', 'JP-13313985-A', 'JP-2009181101-A', 'KR-19940700442-A', 'KR-20057010360-A', 'KR-20167024476-A', 'KR-20187008669-A', 'KR-20207004898-A', 'MX-2013002850-A', 'PE-2012000906-A', 'PT-14764430-T', 'RO-7944874-A', 'TW-107142982-A', 'US-2003112494-A1', 'US-2005136639-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-201514981715-A', 'US-201515313510-A', 'US-201515329526-A', 'US-201615554660-A', 'US-201715422925-A', 'US-201715469746-A', 'US-201715625819-A', 'US-201715646074-A', 'US-201716099227-A', 'US-201716319139-A', 'US-201716335976-A', 'US-201815950106-A', 'US-201816612511-A', 'US-201916362297-A', 'US-201916396723-A', 'US-201916537416-A', 'US-201916977341-A', 'US-201917293905-A', 'US-202016743881-A', 'US-202016883515-A', 'US-202016952492-A', 'US-202017021925-A', 'US-202017422807-A', 'US-202117197897-A', 'US-202117472182-A', 'US-202117791452-A', 'US-202117926000-A', 'US-202318169681-A', 'US-202318184298-A', 'US-27746394-A', 'US-3666017D-A', 'US-37750473-A', 'US-39137803-A', 'US-39548599-A', 'US-41229799-A', 'US-55161904-A', 'US-68078803-A', 'US-91189497-A', 'US-97493601-A', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2018067976-A1', 'WO-2020055916-A9', 'WO-2020068183-A3', 'WO-2020096950-A1', 'WO-2021102420-A1', 'WO-2022178138-A1', 'WO-2022245977-A2', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2024044766-A3', 'WO-2024050335-A2', 'WO-2024112568-A1'], 'var_call_hoPijUw3pqNinZZeVxyZK0eY': {'citing_map': {}, 'unique_codes': []}}

exec(code, env_args)
