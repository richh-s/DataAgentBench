code = """import json, re
# Load full publicationinfo
with open(var_call_5I4DtjpcM4Fv7fjmRPlhswNj, 'r') as f:
    allrecs = json.load(f)
# Build mapping from publication_number to record
pub_to_rec = {}
for rec in allrecs:
    # try to extract publication number from Patents_info
    pi = rec.get('Patents_info') or ''
    m = re.search(r'publication (?:no\.|number|number|number)\s*([A-Z]{2,3}-[0-9]{4,}[A-Z0-9\-]*)', pi, flags=re.IGNORECASE)
    if m:
        pub = m.group(1).upper()
        pub_to_rec[pub] = rec
    else:
        # maybe 'has publication number US-11081687-B2' variants
        m2 = re.search(r'pub\. number\s*([A-Z]{2,3}-[0-9]{4,}[A-Z0-9\-]*)', pi, flags=re.IGNORECASE)
        if m2:
            pub = m2.group(1).upper()
            pub_to_rec[pub] = rec
# Let's show some keys
keys = list(pub_to_rec.keys())[:50]
print('__RESULT__:')
print(json.dumps(keys))"""

env_args = {'var_call_5I4DtjpcM4Fv7fjmRPlhswNj': 'file_storage/call_5I4DtjpcM4Fv7fjmRPlhswNj.json', 'var_call_3VyetCwrZExI2Xpet9Um2Z3I': 'file_storage/call_3VyetCwrZExI2Xpet9Um2Z3I.json', 'var_call_aQiaaKewuvuNUgNV4DvyEt09': {'pairs': [], 'codes': []}, 'var_call_dEoQDTzU3g8MBJxJTTtcYTmC': 'file_storage/call_dEoQDTzU3g8MBJxJTTtcYTmC.json', 'var_call_nxN5eBvJXYwbAZgZ0FnUqKrV': [], 'var_call_Lb2aFYNCzIUGMiHjFYMERzCW': 'file_storage/call_Lb2aFYNCzIUGMiHjFYMERzCW.json', 'var_call_ejIAYQLOHqeJ95QlU8d5FeRT': {'univ_pubnums': [], 'assignees': {}, 'codes': []}, 'var_call_t4S4NSfolHw3HxJaXMVQ6zn0': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'The EP patent filing (app. number EP-21763795-A) is owned by THE REGENTS OF UNIV OF CALIFORNIA and has publication number EP-4114888-A1.', 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.']}

exec(code, env_args)
