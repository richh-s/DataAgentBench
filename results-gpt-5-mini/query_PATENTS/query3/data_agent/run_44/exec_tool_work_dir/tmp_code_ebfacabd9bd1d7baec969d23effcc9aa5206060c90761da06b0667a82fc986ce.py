code = """import json, re, ast
# load vars from storage
univ_var = var_call_cc68Z6aX2MXH8DgcWXYV034B
all_var = var_call_eiXMVRbHEswgJ2rp1nTqEsy4
if isinstance(univ_var, str):
    with open(univ_var, 'r', encoding='utf-8') as f:
        univ_records = json.load(f)
else:
    univ_records = univ_var
if isinstance(all_var, str):
    with open(all_var, 'r', encoding='utf-8') as f:
        all_records = json.load(f)
else:
    all_records = all_var

# extract publication numbers from UNIV CALIFORNIA Patents_info
pub_regex = re.compile(r"[A-Z]{2,3}-[A-Z0-9-]*\d+[A-Z0-9-]*")
univ_pubnums = set()
for r in univ_records:
    pi = r.get('Patents_info','') or ''
    for m in pub_regex.findall(pi):
        univ_pubnums.add(m.strip())

# helper to parse JSON-like fields
def parse_field(val):
    if not val:
        return []
    if isinstance(val, list):
        return val
    try:
        return json.loads(val)
    except Exception:
        try:
            return ast.literal_eval(val)
        except Exception:
            return []

# regex to extract assignee up to keywords
split_re = re.compile(r"^(.*?)(?:\s+(?:holds the|holds|is assigned to|is owned by|belongs to|is belonging to|belonging to|owned by|is held by|held by|assigned to|with publication|with pub|with pub\.|with publication number|with publication no\.|has publication|has pub|has publication number))", re.IGNORECASE)

assignee_map = {}
code_set = set()

for r in all_records:
    cit_arr = parse_field(r.get('citation',''))
    cited = set()
    for it in cit_arr:
        if isinstance(it, dict):
            pn = (it.get('publication_number') or '').strip()
            if pn:
                cited.add(pn)
    if not univ_pubnums:
        continue
    if cited.intersection(univ_pubnums):
        pi = r.get('Patents_info','') or ''
        if 'UNIV CALIFORNIA' in pi.upper():
            continue
        m = split_re.search(pi)
        if m:
            assignee = m.group(1).strip()
        else:
            assignee = pi.split(',')[0].strip()
        if not assignee:
            assignee = 'UNKNOWN'
        # parse cpc
        cpc_arr = parse_field(r.get('cpc',''))
        primary = []
        for c in cpc_arr:
            if isinstance(c, dict) and c.get('first'):
                code = c.get('code')
                if code:
                    primary.append(code)
        if not primary and cpc_arr:
            c = cpc_arr[0]
            if isinstance(c, dict) and c.get('code'):
                primary.append(c.get('code'))
        assignee_map.setdefault(assignee, set()).update(primary)
        for cc in primary:
            code_set.add(cc)

# prepare output
assignees = []
for a, codes in assignee_map.items():
    assignees.append({'assignee': a, 'cpc_codes': sorted(list(codes))})

out = {'assignees': assignees, 'cpc_codes': sorted(list(code_set)), 'num_univ_pubs': len(univ_pubnums)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cc68Z6aX2MXH8DgcWXYV034B': 'file_storage/call_cc68Z6aX2MXH8DgcWXYV034B.json', 'var_call_r1rLlChnwgV9fpjtfBZ4FUB9': [], 'var_call_gpK3xriqZczE4HtoLAE6feqr': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'], 'var_call_aImyVbUV9Z2hMgiWtgSxfFfT': 'file_storage/call_aImyVbUV9Z2hMgiWtgSxfFfT.json', 'var_call_eiXMVRbHEswgJ2rp1nTqEsy4': 'file_storage/call_eiXMVRbHEswgJ2rp1nTqEsy4.json', 'var_call_Ss5g2DXt2Jt33OTnaUSJGorR': {'assignees': [], 'cpc_codes': [], 'num_univ_pubs': 0}, 'var_call_KruG6acTUcCI2ekg6hWFoLUp': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.', 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.', 'Patent filing (app. number AU-2898989-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2898989-A.', 'UNIV CALIFORNIA holds the RO patent filing (application no. RO-7944874-A), with pub. number RO-70061-A.', 'UNIV CALIFORNIA holds the WO patent filing (application number US-2017015812-W), with publication number WO-2017136335-A1.', 'In WO, the patent application (no. US-2019059638-W) is held by UNIV CALIFORNIA and has publication no. WO-2020096950-A1.', 'The WO patent filing (application no. US-2020061827-W) is assigned to UNIV CALIFORNIA and has pub. number WO-2021102420-A1.', 'In WO, the patent filing (app. number US-2012039471-W) is belonging to UNIV CALIFORNIA and has pub. number WO-2012162563-A2.', 'The US application (ID US-201916537416-A) is owned by UNIV CALIFORNIA and has publication no. US-10900049-B2.', 'The US patent filing (application no. US-201816612511-A) is assigned to UNIV CALIFORNIA and has pub. number US-11376346-B2.', 'UNIV CALIFORNIA holds the US patent application (number US-201715646074-A), with publication no. US-2017369950-A1.', 'UNIV CALIFORNIA holds the KR patent filing (app. number KR-20187008669-A), with publication no. KR-20180041236-A.', 'The CN patent filing (application no. CN-200380105631-A) is owned by UNIV CALIFORNIA and has pub. number CN-100339724-C.', 'UNIV CALIFORNIA holds the US application (no. US-8864206-A), with publication number US-2009031436-A1.', 'UNIV CALIFORNIA holds the AU patent filing (application number AU-2005269556-A), with publication number AU-2005269556-A1.', 'The US patent filing (application no. US-201916362297-A) is assigned to UNIV CALIFORNIA and has publication no. US-11248107-B2.', 'Patent filing (application no. US-2019021660-W) from WO, assigned to UNIV CALIFORNIA, with publication number WO-2019173834-A1.', 'UNIV CALIFORNIA holds the US patent filing (app. number US-201715422925-A), with pub. number US-2017145219-A1.', 'The US patent filing (application no. US-201815950106-A) is held by UNIV CALIFORNIA and has publication no. US-2018304537-A1.', 'In US, the application (ID US-202016883515-A) is owned by UNIV CALIFORNIA and has publication number US-2021002329-A1.', 'The KR application (number KR-20207004898-A) is belonging to UNIV CALIFORNIA and has pub. number KR-20200041324-A.', 'In CN, the application (no. CN-201180052574-A) is belonging to UNIV CALIFORNIA and has pub. number CN-103189548-A.', 'The CA application (no. CA-2298540-A) is held by UNIV CALIFORNIA and has pub. number CA-2298540-A1.', 'UNIV CALIFORNIA holds the AU application (number AU-2001296493-A), with publication no. AU-2001296493-B2.', 'In AU, the application (ID AU-2008329628-A) is belonging to UNIV CALIFORNIA and has publication no. AU-2008329628-B2.', 'Application (no. US-201916401060-A) from US, assigned to UNIV CALIFORNIA, with publication no. US-10765865-B2.', 'In JP, the application (ID JP-2004321293-A) is belonging to UNIV CALIFORNIA and has publication number JP-2005104983-A.', 'The IL patent application (no. IL-14014099-A) is assigned to UNIV CALIFORNIA and has publication no. IL-140140-A0.', 'The US application (number US-202017021925-A) is assigned to UNIV CALIFORNIA and has pub. number US-2021000566-A1.', 'In US, the patent application (ID US-17323505-A) is held by UNIV CALIFORNIA and has pub. number US-2006051790-A1.', 'Patent filing (app. number KR-20207010098-A) from KR, belonging to UNIV CALIFORNIA, with publication no. KR-20200084864-A.', 'The PT application (number PT-14764430-T) is assigned to UNIV CALIFORNIA and has publication number PT-2970346-T.'], 'var_call_ZHMRTdkuLbRBukYpwLQDCtOf': {'assignees': [], 'cpc_codes': [], 'num_univ_pubs': 0}, 'var_call_jVQ18Wp3L5n3sxx1S0ISlFXs': 'file_storage/call_jVQ18Wp3L5n3sxx1S0ISlFXs.json'}

exec(code, env_args)
