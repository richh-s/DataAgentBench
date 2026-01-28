code = """import json, re
# Load candidate records (result of earlier OR-query)
path_cand = var_call_fgSdFd0nlzrQTl13vaBBtYLD
with open(path_cand, 'r') as f:
    cand_records = json.load(f)
# Load UNIV CA records
path_univ = var_call_o3PfwbtrF1Uq9E4KQ2atPaw9
with open(path_univ, 'r') as f:
    univ_records = json.load(f)
# Load target publication numbers list
target_pubs = var_call_9d8lYiSLsGbc6ekXKj5tAhZ5
target_set = set(target_pubs)

# Build mapping from publication_number -> primary CPC codes from univ_records
pub_to_primary = {}
for rec in univ_records:
    # find publication numbers in Patents_info
    info = rec.get('Patents_info','')
    found = re.findall(r"\b[A-Z]{2}-[0-9A-Za-z-]+\b", info)
    # also look into citation field for publication_number entries
    try:
        cites = json.loads(rec.get('citation') or '[]')
    except Exception:
        try:
            cites = json.loads((rec.get('citation') or '').replace("'", '"'))
        except Exception:
            cites = []
    for c in cites:
        if isinstance(c, dict):
            pn = c.get('publication_number')
            if pn:
                found.append(pn)
    # parse cpc primary codes
    prim = []
    raw_cpc = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(raw_cpc)
    except Exception:
        try:
            cpcs = json.loads(raw_cpc.replace("'","\""))
        except Exception:
            cpcs = []
    for c in cpcs:
        if isinstance(c, dict) and c.get('first') and c.get('code'):
            prim.append(c.get('code'))
    for p in found:
        if p in target_set:
            pub_to_primary[p] = prim

# Now scan candidate records and collect assignees citing any target pubs
citing_map = {}
for rec in cand_records:
    cit_field = rec.get('citation')
    if not cit_field:
        continue
    try:
        citations = json.loads(cit_field)
    except Exception:
        try:
            citations = json.loads(cit_field.replace("'","\""))
        except Exception:
            citations = []
    cited_pubs = [c.get('publication_number') for c in citations if isinstance(c, dict) and c.get('publication_number')]
    matched = [p for p in cited_pubs if p in target_set]
    if not matched:
        continue
    # extract assignee heuristically from Patents_info
    info = rec.get('Patents_info','')
    assignee = None
    m = re.match(r"^([A-Z0-9 &,'\.\-/]+?)\s+(?:holds|hold|is assigned to|assigned to|owns|has|having|with pub|with publication|is owned by|held by)\b", info, flags=re.IGNORECASE)
    if m:
        assignee = m.group(1).strip().strip(',')
    else:
        # try 'assigned to XYZ' elsewhere
        m2 = re.search(r"assigned to\s+([A-Z0-9 &,'\.\-/]+?)\b", info, flags=re.IGNORECASE)
        if m2:
            assignee = m2.group(1).strip().strip(',')
        else:
            if ',' in info:
                assignee = info.split(',')[0].strip()
            else:
                assignee = info.strip()
    if not assignee:
        continue
    if 'UNIV' in assignee.upper() and 'CALIFORNIA' in assignee.upper():
        continue
    # collect primary codes from matched cited pubs
    codes = set()
    for mp in matched:
        pcs = pub_to_primary.get(mp)
        if pcs:
            for pc in pcs:
                codes.add(pc)
        else:
            # try to find the publication in univ_records by searching Patents_info
            for ur in univ_records:
                if mp in (ur.get('Patents_info') or ''):
                    try:
                        cpcs2 = json.loads(ur.get('cpc') or '[]')
                    except Exception:
                        try:
                            cpcs2 = json.loads((ur.get('cpc') or '').replace("'","\""))
                        except Exception:
                            cpcs2 = []
                    for c2 in cpcs2:
                        if isinstance(c2, dict) and c2.get('first') and c2.get('code'):
                            codes.add(c2.get('code'))
    if codes:
        citing_map.setdefault(assignee, set()).update(codes)

# prepare outputs
res = {'citing_map': {k: sorted(list(v)) for k,v in citing_map.items()}, 'all_codes': sorted(list({c for codes in citing_map.values() for c in codes}))}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_GHHlpoJLIGHealc6HCfay9RQ': ['publicationinfo'], 'var_call_3LJBg0Bx7wVqc6J2Bvzo7KKF': ['cpc_definition'], 'var_call_o3PfwbtrF1Uq9E4KQ2atPaw9': 'file_storage/call_o3PfwbtrF1Uq9E4KQ2atPaw9.json', 'var_call_9d8lYiSLsGbc6ekXKj5tAhZ5': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_BdNFFy7hXbD4Cv4pMaxIaYEM': 'file_storage/call_BdNFFy7hXbD4Cv4pMaxIaYEM.json', 'var_call_u4G7qeZ2I320L1Idc2fyilVW': {'result_list': [], 'all_codes': []}, 'var_call_fgSdFd0nlzrQTl13vaBBtYLD': 'file_storage/call_fgSdFd0nlzrQTl13vaBBtYLD.json', 'var_call_HM6Z0LipS4ASbFkm4w3B7Xer': {'univ_pubs': [], 'assignees_citing_count': 0, 'assignees_sample': []}, 'var_call_UuZBmw2tmByh7kkx98tKvMZG': {'pub_count': 0, 'pubs': []}}

exec(code, env_args)
