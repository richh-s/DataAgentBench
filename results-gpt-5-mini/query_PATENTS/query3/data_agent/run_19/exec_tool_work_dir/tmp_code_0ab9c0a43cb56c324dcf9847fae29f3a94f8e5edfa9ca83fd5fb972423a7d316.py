code = """import json, re
path_univ = var_call_o3PfwbtrF1Uq9E4KQ2atPaw9
path_all = var_call_BdNFFy7hXbD4Cv4pMaxIaYEM
with open(path_univ,'r') as f:
    univ_records = json.load(f)
with open(path_all,'r') as f:
    all_records = json.load(f)

def norm(s):
    return re.sub(r'[^A-Z0-9]','', s.upper()) if s else ''

# collect UNIV publication numbers from Patents_info and citation fields
univ_pubnums = set()
pub_to_rec = {}
for rec in univ_records:
    info = rec.get('Patents_info','')
    found = re.findall(r"\b[A-Z]{2}-[0-9A-Za-z-]+\b", info)
    for p in found:
        univ_pubnums.add(p)
        pub_to_rec[p] = rec
    try:
        cites = json.loads(rec.get('citation') or '[]')
    except Exception:
        try:
            cites = json.loads((rec.get('citation') or '').replace("'","\""))
        except Exception:
            cites = []
    for c in cites:
        pn = c.get('publication_number')
        if pn:
            univ_pubnums.add(pn)
            if pn not in pub_to_rec:
                pub_to_rec[pn] = rec

# build normalized map
norm_to_orig = {}
for p in list(univ_pubnums):
    n = norm(p)
    if n:
        norm_to_orig[n] = p

# helper to get primary cpcs for a given publication original string
def get_primary_codes_for_pub(orig):
    rec = pub_to_rec.get(orig)
    codes = []
    if not rec:
        return codes
    try:
        cpcs = json.loads(rec.get('cpc') or '[]')
    except Exception:
        try:
            cpcs = json.loads((rec.get('cpc') or '').replace("'","\""))
        except Exception:
            cpcs = []
    for c in cpcs:
        if isinstance(c, dict) and c.get('first'):
            code = c.get('code')
            if code:
                codes.append(code)
    return codes

# scan all records' citations to find those citing univ pubs
citing_map = {}
all_codes = set()
for rec in all_records:
    cit_field = rec.get('citation','')
    if not cit_field:
        continue
    try:
        citations = json.loads(cit_field)
    except Exception:
        try:
            citations = json.loads(cit_field.replace("'","\""))
        except Exception:
            citations = []
    matched = set()
    for c in citations:
        pn = c.get('publication_number')
        if not pn:
            continue
        n = norm(pn)
        if n in norm_to_orig:
            matched.add(norm_to_orig[n])
    if not matched:
        continue
    # extract assignee from Patents_info
    info = rec.get('Patents_info','')
    assignee = None
    m = re.match(r"^([A-Z0-9 &,'\.\-/]+?)\s+(?:holds|hold|is assigned to|assigned to|owns|has|having|with pub|with publication|is owned by|held by)\b", info, flags=re.IGNORECASE)
    if m:
        assignee = m.group(1).strip().strip(',')
    else:
        m2 = re.search(r"assigned to\s+([A-Z0-9 &,'\.\-/]+?)\b", info, flags=re.IGNORECASE)
        if m2:
            assignee = m2.group(1).strip().strip(',')
        else:
            if ',' in info:
                assignee = info.split(',')[0].strip()
            else:
                assignee = ' '.join(info.split()[:5])
    if not assignee:
        continue
    if 'UNIV' in assignee.upper() and 'CALIFORNIA' in assignee.upper():
        continue
    # gather primary codes from matched cited pubs
    codes_for_assignee = set()
    for cited in matched:
        pcs = get_primary_codes_for_pub(cited)
        for p in pcs:
            codes_for_assignee.add(p)
        if not pcs:
            for rec2 in all_records:
                if cited in (rec2.get('Patents_info') or ''):
                    try:
                        cpcs2 = json.loads(rec2.get('cpc') or '[]')
                    except Exception:
                        try:
                            cpcs2 = json.loads((rec2.get('cpc') or '').replace("'","\""))
                        except Exception:
                            cpcs2 = []
                    for c2 in cpcs2:
                        if isinstance(c2, dict) and c2.get('first'):
                            codes_for_assignee.add(c2.get('code'))
    if codes_for_assignee:
        citing_map.setdefault(assignee, set()).update(codes_for_assignee)
        all_codes.update(codes_for_assignee)

# prepare output
out = {'citing_map': {k: sorted(list(v)) for k,v in citing_map.items()}, 'all_codes': sorted(list(all_codes))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GHHlpoJLIGHealc6HCfay9RQ': ['publicationinfo'], 'var_call_3LJBg0Bx7wVqc6J2Bvzo7KKF': ['cpc_definition'], 'var_call_o3PfwbtrF1Uq9E4KQ2atPaw9': 'file_storage/call_o3PfwbtrF1Uq9E4KQ2atPaw9.json', 'var_call_9d8lYiSLsGbc6ekXKj5tAhZ5': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_BdNFFy7hXbD4Cv4pMaxIaYEM': 'file_storage/call_BdNFFy7hXbD4Cv4pMaxIaYEM.json', 'var_call_u4G7qeZ2I320L1Idc2fyilVW': {'result_list': [], 'all_codes': []}}

exec(code, env_args)
