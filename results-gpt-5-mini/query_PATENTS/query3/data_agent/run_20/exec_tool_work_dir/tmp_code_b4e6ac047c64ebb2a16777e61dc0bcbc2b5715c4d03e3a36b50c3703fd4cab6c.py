code = """import json, re
# Load UNIV pubnums from previous execute_python result var_call_t008jIddZZ4mk14CQxsKFzMy
s = var_call_t008jIddZZ4mk14CQxsKFzMy
# s is the printed output string like: {"count": 169, "pubnums": [...]}
# find the first '{'
idx = s.find('{')
if idx!=-1:
    sjson = s[idx:]
else:
    sjson = s
try:
    parsed = json.loads(sjson)
    univ_pubnums = set([p.upper() for p in parsed.get('pubnums',[])])
except Exception:
    univ_pubnums = set()

# Load citing rows from file path stored in var_call_TXF5iLgHVwuGHi0geYBudpqL
import os
with open(var_call_TXF5iLgHVwuGHi0geYBudpqL, 'r') as f:
    citing_rows = json.load(f)

# helper functions
def extract_assignee(text):
    if not text:
        return None
    text = text.strip()
    lowers = text.lower()
    for sep in [' holds the', ' holds', ' is assigned to', ' is owned by', ' owns the', ' belonging to', ' is belonging to', ' held by', ',']:
        idx = lowers.find(sep)
        if idx!=-1:
            name = text[:idx]
            return name.strip().upper()
    return text.upper()

# Parse citations and find matches
assignee_map = {}  # assignee -> set of primary cpcs
for r in citing_rows:
    citation_field = r.get('citation')
    if not citation_field:
        continue
    try:
        citations = json.loads(citation_field) if isinstance(citation_field, str) else citation_field
    except:
        # try replacing single quotes
        try:
            citations = json.loads(citation_field.replace("'", '"'))
        except:
            citations = []
    matched = False
    for c in citations:
        if isinstance(c, dict):
            pub = c.get('publication_number')
            if pub and pub.strip().upper() in univ_pubnums:
                matched = True
                break
    if not matched:
        continue
    assignee = extract_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee:
        continue
    # parse cpc
    primary_codes = set()
    cpc_field = r.get('cpc')
    try:
        cpcs = json.loads(cpc_field) if isinstance(cpc_field, str) else cpc_field
    except:
        cpcs = []
    if isinstance(cpcs, list):
        for e in cpcs:
            if isinstance(e, dict) and e.get('first'):
                code = e.get('code')
                if code:
                    primary_codes.add(code)
    if not primary_codes and isinstance(cpcs, list) and len(cpcs)>0:
        e = cpcs[0]
        if isinstance(e, dict) and e.get('code'):
            primary_codes.add(e.get('code'))
    if assignee not in assignee_map:
        assignee_map[assignee] = set()
    assignee_map[assignee].update(primary_codes)

# Prepare output
assignees = []
unique_primary_cpcs = set()
for a, codes in assignee_map.items():
    codes_list = sorted(list(codes))
    assignees.append({'assignee': a, 'primary_cpcs': codes_list})
    unique_primary_cpcs.update(codes_list)

output = {'assignees': assignees, 'unique_primary_cpcs': sorted(list(unique_primary_cpcs))}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_JmtpD4VJGFoecQO8VCX0zY1M': 'file_storage/call_JmtpD4VJGFoecQO8VCX0zY1M.json', 'var_call_UCPD1RS4AZvlswJyAis5URH1': 'file_storage/call_UCPD1RS4AZvlswJyAis5URH1.json', 'var_call_TXF5iLgHVwuGHi0geYBudpqL': 'file_storage/call_TXF5iLgHVwuGHi0geYBudpqL.json', 'var_call_2Md769yXdot8j6FoexQHqNUj': {'mappings': [], 'unique_primary_cpcs': []}, 'var_call_M2l4E4jBDPonKyZnVB92otkn': {'num_univ_rows': 169, 'num_citing_rows': 137678, 'num_univ_pubnums': 0, 'num_cited_pubnums': 8987, 'sample_univ': [], 'sample_cited': ['AT-294301-B', 'AT-305676-B', 'AU-2005314079-B2', 'AU-2006279558-A1', 'AU-4099585-A', 'AU-5531486-A', 'CA-1051802-A', 'CA-1095306-A', 'CA-2031433-A1', 'CA-2046037-A1', 'CA-2465692-A1', 'CA-2473135-A1', 'CA-2525371-A1', 'CA-2525382-A1', 'CA-2582365-A1', 'CA-2617872-A1', 'CA-2636249-A1', 'CA-2700258-A1', 'CA-2921163-A1', 'CA-2938521-A1']}, 'var_call_xqyFtUhvRTxPi6GiMnM9fzn1': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.', 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.'], 'var_call_MoJazxouiwpIlw5r53SdmZZ4': {'num_univ_pubnums': 0, 'num_matches': 0, 'unique_primary_cpcs': [], 'mappings_sample': []}, 'var_call_RDoG4FKrf1eT8TtgnUNTCwvK': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.', 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.', 'Patent filing (app. number AU-2898989-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2898989-A.', 'UNIV CALIFORNIA holds the RO patent filing (application no. RO-7944874-A), with pub. number RO-70061-A.', 'UNIV CALIFORNIA holds the WO patent filing (application number US-2017015812-W), with publication number WO-2017136335-A1.', 'In WO, the patent application (no. US-2019059638-W) is held by UNIV CALIFORNIA and has publication no. WO-2020096950-A1.', 'The WO patent filing (application no. US-2020061827-W) is assigned to UNIV CALIFORNIA and has pub. number WO-2021102420-A1.', 'In WO, the patent filing (app. number US-2012039471-W) is belonging to UNIV CALIFORNIA and has pub. number WO-2012162563-A2.', 'The US application (ID US-201916537416-A) is owned by UNIV CALIFORNIA and has publication no. US-10900049-B2.', 'The US patent filing (application no. US-201816612511-A) is assigned to UNIV CALIFORNIA and has pub. number US-11376346-B2.', 'UNIV CALIFORNIA holds the US patent application (number US-201715646074-A), with publication no. US-2017369950-A1.', 'UNIV CALIFORNIA holds the KR patent filing (app. number KR-20187008669-A), with publication no. KR-20180041236-A.', 'The CN patent filing (application no. CN-200380105631-A) is owned by UNIV CALIFORNIA and has pub. number CN-100339724-C.', 'UNIV CALIFORNIA holds the US application (no. US-8864206-A), with publication number US-2009031436-A1.', 'UNIV CALIFORNIA holds the AU patent filing (application number AU-2005269556-A), with publication number AU-2005269556-A1.', 'The US patent filing (application no. US-201916362297-A) is assigned to UNIV CALIFORNIA and has publication no. US-11248107-B2.', 'Patent filing (application no. US-2019021660-W) from WO, assigned to UNIV CALIFORNIA, with publication number WO-2019173834-A1.', 'UNIV CALIFORNIA holds the US patent filing (app. number US-201715422925-A), with pub. number US-2017145219-A1.', 'The US patent filing (application no. US-201815950106-A) is held by UNIV CALIFORNIA and has publication no. US-2018304537-A1.', 'In US, the application (ID US-202016883515-A) is owned by UNIV CALIFORNIA and has publication number US-2021002329-A1.', 'The KR application (number KR-20207004898-A) is belonging to UNIV CALIFORNIA and has pub. number KR-20200041324-A.', 'In CN, the application (no. CN-201180052574-A) is belonging to UNIV CALIFORNIA and has pub. number CN-103189548-A.', 'The CA application (no. CA-2298540-A) is held by UNIV CALIFORNIA and has pub. number CA-2298540-A1.', 'UNIV CALIFORNIA holds the AU application (number AU-2001296493-A), with publication no. AU-2001296493-B2.', 'In AU, the application (ID AU-2008329628-A) is belonging to UNIV CALIFORNIA and has publication no. AU-2008329628-B2.', 'Application (no. US-201916401060-A) from US, assigned to UNIV CALIFORNIA, with publication no. US-10765865-B2.', 'In JP, the application (ID JP-2004321293-A) is belonging to UNIV CALIFORNIA and has publication number JP-2005104983-A.', 'The IL patent application (no. IL-14014099-A) is assigned to UNIV CALIFORNIA and has publication no. IL-140140-A0.', 'The US application (number US-202017021925-A) is assigned to UNIV CALIFORNIA and has pub. number US-2021000566-A1.', 'In US, the patent application (ID US-17323505-A) is held by UNIV CALIFORNIA and has pub. number US-2006051790-A1.', 'Patent filing (app. number KR-20207010098-A) from KR, belonging to UNIV CALIFORNIA, with publication no. KR-20200084864-A.', 'The PT application (number PT-14764430-T) is assigned to UNIV CALIFORNIA and has publication number PT-2970346-T.'], 'var_call_t008jIddZZ4mk14CQxsKFzMy': {'count': 169, 'pubnums': ['AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-B2', 'AU-2002254753-B2', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008329628-B2', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5366398-A', 'AU-5938296-A', 'AU-6535890-A', 'AU-7724398-A', 'BR-112021021092-A8', 'BR-9610580-A', 'CA-2220674-A1', 'CA-2278751-A1', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3027364-A1', 'CA-3055214-A1', 'CA-3161617-A1', 'CA-3225295-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103237558-A', 'CN-103687626-A', 'CN-1120376-C', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-1224461-B1', 'EP-2029921-A4', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-3866867-A1', 'EP-4284234-A1', 'FR-2194760-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-140140-A0', 'IL-236725-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-100228821-B1', 'KR-20050085437-A', 'KR-20080078049-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20180041236-A', 'KR-20200041324-A', 'KR-20200084864-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10337029-B2', 'US-10359432-B2', 'US-10744347-B2', 'US-10765865-B2', 'US-10900049-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11248107-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11445941-B2', 'US-11546022-B2', 'US-11607427-B2', 'US-11667770-B2', 'US-11960018-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005136639-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2008047008-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017050153-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017194630-A1', 'US-2017281687-A1', 'US-2017294981-A1', 'US-2017369950-A1', 'US-2018080022-A1', 'US-2018243924-A1', 'US-2018277766-A1', 'US-2018304537-A1', 'US-2018348310-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2022123166-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023314781-A1', 'US-2023321419-A1', 'US-2023340506-A1', 'US-3666017-A', 'US-3842373-A', 'US-5304932-A', 'US-5547866-A', 'US-6030830-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-8361933-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2018152537-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2020096950-A1', 'WO-2021102420-A1', 'WO-2022178138-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024050335-A2', 'WO-2024112568-A1', 'ZA-200802422-B']}}

exec(code, env_args)
