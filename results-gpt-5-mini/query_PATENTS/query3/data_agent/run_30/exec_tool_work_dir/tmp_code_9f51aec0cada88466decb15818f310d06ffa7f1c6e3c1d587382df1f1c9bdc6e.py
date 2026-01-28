code = """import json, re
# Load all records
with open(var_call_5I4DtjpcM4Fv7fjmRPlhswNj, 'r') as f:
    allrecs = json.load(f)

# Build map from publication_number to list of records that cite it
pub_to_citing = {}
for rec in allrecs:
    citations = rec.get('citation') or []
    if isinstance(citations, str):
        try:
            citations = json.loads(citations)
        except:
            citations = []
    for c in citations:
        if isinstance(c, dict):
            p = (c.get('publication_number') or '').upper().strip()
            if p:
                pub_to_citing.setdefault(p, []).append(rec)
# Now find Univ California publication numbers from earlier list of Patents_info keys
univ_pubs = [k for k in pub_to_citing.keys() if 'UNIV' in '']
# Instead, find all publication numbers that belong to Univ California by checking Patents_info across allrecs
univ_pubnums = set()
for rec in allrecs:
    pi = rec.get('Patents_info') or ''
    if 'UNIV' in pi.upper() or 'UNIVERSITY OF CALIFORNIA' in pi.upper() or 'REGENTS OF UNIV OF CALIFORNIA' in pi.upper():
        m = re.search(r'([A-Z]{2,3}-[0-9]{4,}[A-Z0-9\-]*)', (pi.upper()))
        if m:
            univ_pubnums.add(m.group(1))
# Now for each univ_pub, get citing records
assignee_to_codes = {}
all_codes = set()
for up in univ_pubnums:
    citing = pub_to_citing.get(up, [])
    for rec in citing:
        pi = rec.get('Patents_info') or ''
        # extract assignee
        m = re.search(r'^(.*?) holds|owned by ([^,\.]+)|is owned by ([^,\.]+)|is assigned to ([^,\.]+)', pi, flags=re.IGNORECASE)
        assignee = None
        if m:
            for g in m.groups():
                if g:
                    assignee = g.strip(); break
        if not assignee:
            assignee = pi.split(' ')[0]
        an = re.sub(r'[^A-Z0-9 &\-\.]+',' ', assignee.upper()).strip()
        if 'UNIV' in an and 'CALIFORNIA' in an:
            continue
        # primary cpc
        primary = None
        cpc_field = rec.get('cpc')
        if cpc_field:
            try:
                cpcs = json.loads(cpc_field)
            except:
                cpcs = []
            for it in cpcs:
                if isinstance(it, dict) and it.get('first'):
                    primary = it.get('code'); break
            if not primary and cpcs:
                if isinstance(cpcs[0], dict): primary = cpcs[0].get('code')
        if an not in assignee_to_codes:
            assignee_to_codes[an] = set()
        if primary:
            assignee_to_codes[an].add(primary); all_codes.add(primary)

print('__RESULT__:')
print(json.dumps({'univ_pubnums': sorted(list(univ_pubnums)),'assignees': {k:list(v) for k,v in assignee_to_codes.items()}, 'codes': sorted(list(all_codes))}))"""

env_args = {'var_call_5I4DtjpcM4Fv7fjmRPlhswNj': 'file_storage/call_5I4DtjpcM4Fv7fjmRPlhswNj.json', 'var_call_3VyetCwrZExI2Xpet9Um2Z3I': 'file_storage/call_3VyetCwrZExI2Xpet9Um2Z3I.json', 'var_call_aQiaaKewuvuNUgNV4DvyEt09': {'pairs': [], 'codes': []}, 'var_call_dEoQDTzU3g8MBJxJTTtcYTmC': 'file_storage/call_dEoQDTzU3g8MBJxJTTtcYTmC.json', 'var_call_nxN5eBvJXYwbAZgZ0FnUqKrV': [], 'var_call_Lb2aFYNCzIUGMiHjFYMERzCW': 'file_storage/call_Lb2aFYNCzIUGMiHjFYMERzCW.json', 'var_call_ejIAYQLOHqeJ95QlU8d5FeRT': {'univ_pubnums': [], 'assignees': {}, 'codes': []}, 'var_call_t4S4NSfolHw3HxJaXMVQ6zn0': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'The EP patent filing (app. number EP-21763795-A) is owned by THE REGENTS OF UNIV OF CALIFORNIA and has publication number EP-4114888-A1.', 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.'], 'var_call_Igfcem8S67QyNMRoogvuC7Hx': ['US-11081687-B2', 'US-10794458-B2', 'US-11124615-B2', 'US-10610606-B2', 'US-10957507-B2', 'US-10933114-B2', 'US-11169125-B2', 'US-10695419-B2', 'US-10950222-B2', 'US-11168653-B2', 'US-10853219-B2', 'US-11136369-B2', 'US-11076136-B2', 'US-10898606-B2', 'US-11182846-B2', 'US-11130385-B2', 'US-10720793-B2', 'US-11141094-B2', 'US-10918785-B2', 'US-11601114-B2', 'US-10924243-B2', 'US-11018783-B2', 'US-11072514-B2', 'US-10859440-B2', 'US-10875306-B2', 'US-10692314-B2', 'US-10904976-B2', 'US-10704655-B2', 'US-10897184-B2', 'US-10826200-B2', 'US-11128943-B2', 'US-10809655-B2', 'US-11273226-B2', 'US-11024606-B2', 'US-11231876-B2', 'US-11126940-B2', 'US-11911287-B2', 'US-10868205-B2', 'US-11082077-B2', 'US-11202094-B2', 'US-11025166-B2', 'US-10974840-B2', 'US-11032098-B2', 'US-11713774-B2', 'US-11307152-B2', 'US-11371080-B2', 'US-11478419-B2', 'US-11137932-B2', 'US-11813423-B2', 'US-10868012-B2']}

exec(code, env_args)
