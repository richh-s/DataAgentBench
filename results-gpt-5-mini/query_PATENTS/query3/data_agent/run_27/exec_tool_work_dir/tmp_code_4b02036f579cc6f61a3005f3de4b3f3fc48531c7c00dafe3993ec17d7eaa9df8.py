code = """import json, re
path_uc = var_call_JWwOoz2mOIB25IYurOvjgP1M
path_all = var_call_o7WhSWD2Ix8GZwBlSyK49Vbx
with open(path_uc, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)
with open(path_all, 'r', encoding='utf-8') as f:
    all_rows = json.load(f)

# extract UC publication numbers from uc_rows citations or Patents_info
uc_pubnums = set()
for rec in uc_rows:
    cit = rec.get('citation','')
    try:
        cs = json.loads(cit) if cit and cit.strip().startswith('[') else []
    except Exception:
        cs = []
    for c in cs:
        pn = c.get('publication_number')
        if pn:
            uc_pubnums.add(pn)
    # also try parse pub number from Patents_info
    pi = rec.get('Patents_info','')
    m = re.search(r'pub\. number\s+([A-Z0-9\-]+)', pi)
    if m:
        uc_pubnums.add(m.group(1))
    m2 = re.search(r'publication number\s+([A-Z0-9\-]+)', pi)
    if m2:
        uc_pubnums.add(m2.group(1))
    m3 = re.search(r'with pub\. number\s+([A-Z0-9\-]+)', pi)
    if m3:
        uc_pubnums.add(m3.group(1))

# Now scan all_rows for citations that reference any uc_pubnums
pairs = []
seen = set()
for rec in all_rows:
    cit = rec.get('citation','')
    try:
        cs = json.loads(cit) if cit and cit.strip().startswith('[') else []
    except Exception:
        cs = []
    cites_uc = False
    for c in cs:
        pn = c.get('publication_number')
        if pn and pn in uc_pubnums:
            cites_uc = True
            break
    if not cites_uc:
        continue
    # extract assignee from Patents_info
    pi = rec.get('Patents_info','')
    assignee = None
    # common patterns
    patterns = [r'^([A-Z0-9 &,.\-]+?) (?:holds|hold|owns|owned|is owned by|is assigned to|is by|has|has been assigned to) ',
                r'assigned to ([A-Z0-9 &,.\-]+?)(?:\s|,|\.)',
                r'owned by ([A-Z0-9 &,.\-]+?)(?:\s|,|\.)',
                r'^(?:In [A-Z]{2}, the patent|In [A-Z]{2}, the application).*? is assigned to ([A-Z0-9 &,.\-]+?)(?: and|,|\.)',
                r'^(.*?) holds the',
                r'^(.*?) owns the']
    for pat in patterns:
        m = re.search(pat, pi)
        if m:
            g = m.group(1).strip()
            # cleanup trailing phrases like 'In US, the application (number X) is owned by UNIV CALIFORNIA and has pub. number Y.'
            # If g contains 'In US, the application (number US-...)', skip
            if 'application' in g.lower() and len(g.split())>6:
                # try a different group if available
                continue
            assignee = g
            break
    if not assignee:
        # fallback: take leading token before 'holds'
        m = re.match(r'^([^,\.]+)', pi)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        continue
    # normalize
    assignee = re.sub(r'\s+', ' ', assignee)
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    # parse cpc primary code(s)
    cpc_str = rec.get('cpc','')
    try:
        cpcs = json.loads(cpc_str) if cpc_str and cpc_str.strip().startswith('[') else []
    except Exception:
        cpcs = []
    primary_codes = []
    for cp in cpcs:
        if isinstance(cp, dict) and cp.get('first'):
            code = cp.get('code')
            if code:
                primary_codes.append(code)
    # if none marked first, fallback to first code in list
    if not primary_codes and cpcs:
        for cp in cpcs:
            code = cp.get('code') if isinstance(cp, dict) else None
            if code:
                primary_codes.append(code)
                break
    for code in primary_codes:
        key = (assignee, code)
        if key in seen:
            continue
        seen.add(key)
        pairs.append({'assignee': assignee, 'code': code})

# sort by assignee
pairs = sorted(pairs, key=lambda x: (x['assignee'].lower(), x['code']))
print('__RESULT__:')
print(json.dumps(pairs))"""

env_args = {'var_call_RI57H59YoXXdiFWZsUYvmLDR': ['publicationinfo'], 'var_call_pKbEylT8SZftCAfPr1MfqEdM': ['cpc_definition'], 'var_call_JWwOoz2mOIB25IYurOvjgP1M': 'file_storage/call_JWwOoz2mOIB25IYurOvjgP1M.json', 'var_call_urUDqRWAs7PWYnfScunsrhrI': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_o7WhSWD2Ix8GZwBlSyK49Vbx': 'file_storage/call_o7WhSWD2Ix8GZwBlSyK49Vbx.json'}

exec(code, env_args)
