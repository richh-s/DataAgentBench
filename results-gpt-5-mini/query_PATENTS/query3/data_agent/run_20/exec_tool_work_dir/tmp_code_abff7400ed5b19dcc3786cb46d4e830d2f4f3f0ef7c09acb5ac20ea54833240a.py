code = """import json, re
with open(var_call_UCPD1RS4AZvlswJyAis5URH1,'r') as f:
    univ_rows = json.load(f)
with open(var_call_TXF5iLgHVwuGHi0geYBudpqL,'r') as f:
    citing_rows = json.load(f)

pattern = re.compile(r"\b(?:US|WO|EP|AU|JP|CN|KR|TW|CA|RO|PT|IL|AT|FR|DE)-[A-Z0-9\-]*\d+[A-Z0-9\-]*\b", re.IGNORECASE)

univ_pubnums = set()
for r in univ_rows:
    text = r.get('Patents_info','')
    for m in pattern.findall(text):
        # normalize to upper
        univ_pubnums.add(m.upper())

# find citing patents that cite any of these
mappings = []
unique_primary_cpcs = set()

# helper to get assignee
import re

def extract_assignee(text):
    if not text:
        return None
    text = text.strip()
    # try before ' holds the' etc
    for sep in [' holds the', ' holds', ' is assigned to', ' is owned by', ' owns the', ' belonging to', ' is belonging to', ' held by', ',']:
        idx = text.lower().find(sep)
        if idx!=-1:
            name = text[:idx]
            return name.strip().upper()
    return text.upper()

for r in citing_rows:
    citation_field = r.get('citation')
    if not citation_field:
        continue
    try:
        citations = json.loads(citation_field) if isinstance(citation_field, str) else citation_field
    except:
        citations = []
    matched = False
    for c in citations:
        if not isinstance(c, dict):
            continue
        pub = c.get('publication_number')
        if not pub:
            continue
        if pub.strip().upper() in univ_pubnums:
            matched = True
            break
    if not matched:
        continue
    assignee = extract_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee:
        continue
    # get primary cpcs
    primary = []
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
                    primary.append(code)
                    unique_primary_cpcs.add(code)
    if not primary and isinstance(cpcs, list) and len(cpcs)>0:
        e = cpcs[0]
        if isinstance(e, dict) and e.get('code'):
            primary.append(e.get('code'))
            unique_primary_cpcs.add(e.get('code'))
    mappings.append({'assignee': assignee, 'primary_cpcs': primary})

print('__RESULT__:')
print(json.dumps({'num_univ_pubnums': len(univ_pubnums), 'num_matches': len(mappings), 'unique_primary_cpcs': sorted(list(unique_primary_cpcs)), 'mappings_sample': mappings[:50]}))"""

env_args = {'var_call_JmtpD4VJGFoecQO8VCX0zY1M': 'file_storage/call_JmtpD4VJGFoecQO8VCX0zY1M.json', 'var_call_UCPD1RS4AZvlswJyAis5URH1': 'file_storage/call_UCPD1RS4AZvlswJyAis5URH1.json', 'var_call_TXF5iLgHVwuGHi0geYBudpqL': 'file_storage/call_TXF5iLgHVwuGHi0geYBudpqL.json', 'var_call_2Md769yXdot8j6FoexQHqNUj': {'mappings': [], 'unique_primary_cpcs': []}, 'var_call_M2l4E4jBDPonKyZnVB92otkn': {'num_univ_rows': 169, 'num_citing_rows': 137678, 'num_univ_pubnums': 0, 'num_cited_pubnums': 8987, 'sample_univ': [], 'sample_cited': ['AT-294301-B', 'AT-305676-B', 'AU-2005314079-B2', 'AU-2006279558-A1', 'AU-4099585-A', 'AU-5531486-A', 'CA-1051802-A', 'CA-1095306-A', 'CA-2031433-A1', 'CA-2046037-A1', 'CA-2465692-A1', 'CA-2473135-A1', 'CA-2525371-A1', 'CA-2525382-A1', 'CA-2582365-A1', 'CA-2617872-A1', 'CA-2636249-A1', 'CA-2700258-A1', 'CA-2921163-A1', 'CA-2938521-A1']}, 'var_call_xqyFtUhvRTxPi6GiMnM9fzn1': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.', 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.']}

exec(code, env_args)
