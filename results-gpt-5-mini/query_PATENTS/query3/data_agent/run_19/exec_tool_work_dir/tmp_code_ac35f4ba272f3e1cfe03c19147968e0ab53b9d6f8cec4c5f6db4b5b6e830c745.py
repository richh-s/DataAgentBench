code = """import json, re
path_univ = var_call_o3PfwbtrF1Uq9E4KQ2atPaw9
path_all = var_call_BdNFFy7hXbD4Cv4pMaxIaYEM
with open(path_univ,'r') as f:
    univ_records = json.load(f)
with open(path_all,'r') as f:
    all_records = json.load(f)

def norm_pub(p):
    if not p: return None
    return re.sub(r'[^A-Z0-9]','', p.upper())

# Build univ pub set normalized
univ_pubnums = set()
pub_to_record = {}
for rec in univ_records:
    info = rec.get('Patents_info','')
    # find publication numbers in Patents_info and also maybe in citation lists but we rely on Patents_info
    found = re.findall(r"\b[A-Z]{2}-[0-9A-Za-z-]+\b", info)
    # also consider patterns like US-11421276-B2
    for p in found:
        univ_pubnums.add(p)
        pub_to_record[p] = rec
# Also include publication numbers that appear in citations of the univ_records
for rec in univ_records:
    try:
        citations = json.loads(rec.get('citation') or '[]')
    except Exception:
        try:
            citations = json.loads((rec.get('citation') or '').replace("'","\""))
        except Exception:
            citations = []
    for c in citations:
        pn = c.get('publication_number')
        if pn:
            univ_pubnums.add(pn)
            if pn not in pub_to_record:
                pub_to_record[pn] = rec

univ_norm_set = {norm_pub(p): p for p in univ_pubnums if norm_pub(p)}

# helper to get primary cpcs from a record
def get_primary_cpcs_from_rec(rec):
    try:
        cpcs = json.loads(rec.get('cpc') or '[]')
    except Exception:
        try:
            cpcs = json.loads((rec.get('cpc') or '').replace("'","\""))
        except Exception:
            cpcs = []
    prim = []
    for c in cpcs:
        if isinstance(c, dict) and c.get('first'):
            code = c.get('code')
            if code:
                prim.append(code)
    return prim

# Now scan all_records citations and match normalized
citing_map = {}
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
    matched_any = False
    matched_pub_originals = set()
    for c in citations:
        pn = c.get('publication_number')
        if not pn: continue
        n = norm_pub(pn)
        if n and n in univ_norm_set:
            matched_any = True
            matched_pub_originals.add(univ_norm_set[n])
    if not matched_any:
        continue
    # extract assignee
    info = rec.get('Patents_info','')
    assignee = None
    m = re.match(r"^([A-Z0-9 &,'\.\-/]+?)\s+(?:holds|hold|is assigned to|assigned to|owns|is owned by|held by|has|having|with publication|with pub\.|with pub|represents)\b", info, flags=re.IGNORECASE)
    if m:
        assignee = m.group(1).strip().strip(',')
    else:
        # look for 'in US, the patent application ... is assigned to XYZ' pattern later in string
        m2 = re.search(r"assigned to\s+([A-Z0-9 &,'\.\-/]+?)\s*(?:and|with|,|\(|has|holds|having|which)", info, flags=re.IGNORECASE)
        if m2:
            assignee = m2.group(1).strip().strip(',')
        else:
            # take leading token until first comma
            if ',' in info:
                assignee = info.split(',')[0].strip()
            else:
                assignee = ' '.join(info.split()[:5])
    if not assignee:
        continue
    assignee_norm = assignee.strip()
    if 'UNIV' in assignee_norm.upper() and 'CALIFORNIA' in assignee_norm.upper():
        continue
    # gather primary cpcs from matched cited pubs
    codes = set()
    for cited in matched_pub_originals:
        rec_univ = pub_to_record.get(cited)
        if rec_univ:
            pcs = get_primary_cpcs_from_rec(rec_univ)
            for pc in pcs:
                codes.add(pc)
        # if still none, try to find record in all_records where Patents_info contains cited string
        if not codes:
            for rec2 in all_records:
                if cited in (rec2.get('Patents_info') or ''):
                    pcs = get_primary_cpcs_from_rec(rec2)
                    for pc in pcs:
                        codes.add(pc)
    if codes:
        citing_map.setdefault(assignee_norm, set()).update(codes)

# prepare result
result_list = []
all_codes = set()
for assignee, codes in citing_map.items():
    codes_sorted = sorted(codes)
    result_list.append({'assignee': assignee, 'primary_cpc_codes': codes_sorted})
    all_codes.update(codes)

out = {'result_list': result_list, 'all_codes': sorted(all_codes)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GHHlpoJLIGHealc6HCfay9RQ': ['publicationinfo'], 'var_call_3LJBg0Bx7wVqc6J2Bvzo7KKF': ['cpc_definition'], 'var_call_o3PfwbtrF1Uq9E4KQ2atPaw9': 'file_storage/call_o3PfwbtrF1Uq9E4KQ2atPaw9.json', 'var_call_9d8lYiSLsGbc6ekXKj5tAhZ5': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_BdNFFy7hXbD4Cv4pMaxIaYEM': 'file_storage/call_BdNFFy7hXbD4Cv4pMaxIaYEM.json', 'var_call_u4G7qeZ2I320L1Idc2fyilVW': {'result_list': [], 'all_codes': []}}

exec(code, env_args)
