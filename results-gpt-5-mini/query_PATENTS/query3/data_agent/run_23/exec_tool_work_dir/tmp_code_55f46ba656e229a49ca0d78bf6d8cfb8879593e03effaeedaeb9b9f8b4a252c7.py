code = """import json, re
path = var_call_ip0VIxxQPAYpor7I60ZUMkDa
with open(path,'r') as f:
    records = json.load(f)

pubs = {}
pattern = re.compile(r"[A-Z]{2}-\d{4,}[A-Z0-9\-]*")
for r in records:
    pi = r.get('Patents_info','')
    rowid = r.get('rowid')
    matches = pattern.findall(pi)
    if matches:
        pubs[rowid] = list(set(matches))

print('__RESULT__:')
import json as _json
print(_json.dumps(pubs))"""

env_args = {'var_call_eeGrTDP9xc0GBQsFnafw3rqr': ['publicationinfo'], 'var_call_xqen9ghB96NH6273mIEFTd71': ['cpc_definition'], 'var_call_ip0VIxxQPAYpor7I60ZUMkDa': 'file_storage/call_ip0VIxxQPAYpor7I60ZUMkDa.json', 'var_call_rYqAvdmHeiUZh5JNCijZfp2u': [], 'var_call_NRgdJY9yHIQi0iR7akeETXNc': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.', 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.'], 'var_call_lk5rjpawdXDLd3O5cjtxkPco': [], 'var_call_JJYX5L8FBEtX3bO6hyCohtKZ': 'file_storage/call_JJYX5L8FBEtX3bO6hyCohtKZ.json'}

exec(code, env_args)
