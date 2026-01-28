code = """import json, re
# Load UNIV CALIFORNIA records file
path_univ = var_call_o3PfwbtrF1Uq9E4KQ2atPaw9
with open(path_univ, 'r') as f:
    univ_records = json.load(f)
# Load full publicationinfo
path_all = var_call_BdNFFy7hXbD4Cv4pMaxIaYEM
with open(path_all, 'r') as f:
    all_records = json.load(f)

# helper to extract publication numbers from Patents_info
def extract_pubnums_from_info(info):
    pubnums = set()
    # common patterns like US-12345-A1, TW-..., WO-..., EP-...
    for m in re.findall(r"\b[A-Z]{2}-[0-9A-Za-z-]+\b", info):
        pubnums.add(m)
    return pubnums

# Build set of UNIV CA publication numbers
univ_pubnums = set()
for rec in univ_records:
    info = rec.get('Patents_info','')
    pubnums = extract_pubnums_from_info(info)
    univ_pubnums.update(pubnums)
# Also try to get publication numbers from a field if exists
for rec in univ_records:
    # some records may include publication number in other keys, but we rely on Patents_info
    pass

# Build map from UNIV pubnum to its primary CPC codes
univ_pub_to_primary_cpcs = {}
for rec in univ_records:
    # try to find its own pubnum
    info = rec.get('Patents_info','')
    pubnums = extract_pubnums_from_info(info)
    pubnum = None
    if pubnums:
        # Heuristic: prefer US if present
        us = [p for p in pubnums if p.startswith('US-')]
        if us:
            pubnum = sorted(us)[0]
        else:
            pubnum = sorted(pubnums)[0]
    # parse cpc field
    cpc_list = []
    try:
        cpc_list = json.loads(rec.get('cpc') or '[]')
    except Exception:
        # try to fix single quotes
        try:
            cpc_list = json.loads(rec.get('cpc').replace("'", '"'))
        except Exception:
            cpc_list = []
    primary_codes = []
    for c in cpc_list:
        if isinstance(c, dict) and c.get('first'):
            code = c.get('code')
            if code:
                primary_codes.append(code)
    if pubnum:
        univ_pub_to_primary_cpcs[pubnum] = primary_codes

# Now scan all records to find citations referencing any univ_pubnums
citing_map = {}  # assignee -> set of primary codes
for rec in all_records:
    cit_field = rec.get('citation','')
    if not cit_field:
        continue
    try:
        citations = json.loads(cit_field)
    except Exception:
        # try replace single quotes
        try:
            citations = json.loads(cit_field.replace("'", '"'))
        except Exception:
            citations = []
    cited_pubnums = [c.get('publication_number') for c in citations if isinstance(c, dict) and c.get('publication_number')]
    # intersection
    matched = set(cited_pubnums) & set(univ_pubnums)
    if not matched:
        continue
    # extract assignee from Patents_info
    info = rec.get('Patents_info','')
    assignee = None
    # regex to capture org before keywords
    m = re.match(r"^([A-Z0-9 &,'\.\-/]+?)\s+(?:holds|hold|is assigned to|assigned to|owns|has|has the|with publication|having|has pub|has pub\.|has publication)\b", info, flags=re.IGNORECASE)
    if m:
        assignee = m.group(1).strip().strip(',')
    else:
        # fallback: take up to first comma
        if ',' in info:
            assignee = info.split(',')[0].strip()
        else:
            # take first 5 words
            assignee = ' '.join(info.split()[:5])
    if not assignee:
        continue
    # normalize
    assignee_norm = assignee.strip()
    if 'UNIV' in assignee_norm.upper() and 'CALIFORNIA' in assignee_norm.upper():
        # exclude UNIV CALIFORNIA
        continue
    # for each matched cited pub, get its primary codes
    codes = set()
    for cited in matched:
        pcs = univ_pub_to_primary_cpcs.get(cited, [])
        for pc in pcs:
            codes.add(pc)
    if not codes:
        # if no primary codes found, try to look at the cited publication record in all_records to get cpc
        for rec2 in all_records:
            # find rec2 whose Patents_info contains the cited pub
            if any(cited in (rec2.get('Patents_info') or '') for cited in matched):
                try:
                    cpcs = json.loads(rec2.get('cpc') or '[]')
                except Exception:
                    try:
                        cpcs = json.loads((rec2.get('cpc') or '').replace("'", '"'))
                    except Exception:
                        cpcs = []
                for c in cpcs:
                    if isinstance(c, dict) and c.get('first'):
                        code = c.get('code')
                        if code:
                            codes.add(code)
    if codes:
        citing_map.setdefault(assignee_norm, set()).update(codes)

# Prepare outputs
result_list = []
all_codes = set()
for assignee, codes in citing_map.items():
    codes_sorted = sorted(codes)
    result_list.append({'assignee': assignee, 'primary_cpc_codes': codes_sorted})
    all_codes.update(codes)

# Save intermediate results to be used by next query
out = {'result_list': result_list, 'all_codes': sorted(all_codes)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GHHlpoJLIGHealc6HCfay9RQ': ['publicationinfo'], 'var_call_3LJBg0Bx7wVqc6J2Bvzo7KKF': ['cpc_definition'], 'var_call_o3PfwbtrF1Uq9E4KQ2atPaw9': 'file_storage/call_o3PfwbtrF1Uq9E4KQ2atPaw9.json', 'var_call_9d8lYiSLsGbc6ekXKj5tAhZ5': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_BdNFFy7hXbD4Cv4pMaxIaYEM': 'file_storage/call_BdNFFy7hXbD4Cv4pMaxIaYEM.json'}

exec(code, env_args)
