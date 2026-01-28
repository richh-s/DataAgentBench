code = """import json, re
path = var_call_5I4DtjpcM4Fv7fjmRPlhswNj
with open(path, 'r') as f:
    allrecs = json.load(f)

# identify Univ California publications
univ_pubnums = set()
for rec in allrecs:
    pi = rec.get('Patents_info') or ''
    up = pi.upper()
    if ('UNIV' in up and 'CALIFORNIA' in up) or ('UNIVERSITY OF CALIFORNIA' in up) or ('REGENTS OF UNIV' in up and 'CALIFORNIA' in up):
        # extract all publication-like tokens
        for m in re.finditer(r"\b[A-Z]{2,3}-[0-9]{4,}[A-Z0-9\-]*\b", up):
            univ_pubnums.add(m.group(0))
# fallback: sometimes 'pub. number' or 'publication number' captured above

# build map of cited publication numbers -> citing records
pub_to_citing = {}
for rec in allrecs:
    citations = rec.get('citation') or []
    if isinstance(citations, str):
        try:
            citations = json.loads(citations)
        except:
            citations = []
    if not isinstance(citations, list):
        continue
    for c in citations:
        if isinstance(c, dict):
            p = (c.get('publication_number') or '').upper().strip()
            if p:
                pub_to_citing.setdefault(p, []).append(rec)

# Now find citing records that cite any univ_pubnums
assignee_to_codes = {}
all_codes = set()

def extract_assignee(pi):
    s = pi or ''
    up = s.upper()
    # try patterns
    patterns = [r'IS OWNED BY ([^,\.]+)', r'OWNED BY ([^,\.]+)', r'IS ASSIGNED TO ([^,\.]+)', r'ASSIGNED TO ([^,\.]+)', r'HOLDS THE [A-Z ]*PATENT [^(]*\(([^)]+)\)', r'^(.*?) HOLDS', r'^(.*?) HOLDS THE', r'^(.*?) HOLDS THE', r'^(.*?) HOLDS', r'^(.*?) HOLDS THE', r'^(.*?) HOLDS', r'^(.*?) HAS PUBLICATION', r'^(.*?) HOLDS', r'^(.*?)\s\(']
    for pat in patterns:
        m = re.search(pat, s, flags=re.IGNORECASE)
        if m:
            g = m.group(1).strip()
            # remove trailing 'and has' or 'and'
            g = re.split(r' and | with |,', g)[0].strip()
            return g
    # fallback: first token sequence before comma
    return s.split(',')[0].strip()

for up in list(univ_pubnums):
    citing = pub_to_citing.get(up, [])
    for rec in citing:
        pi = rec.get('Patents_info') or ''
        assignee = extract_assignee(pi)
        if not assignee:
            continue
        an = re.sub(r'[^A-Z0-9 &\-\.]+',' ', assignee.upper()).strip()
        if 'UNIV' in an and 'CALIFORNIA' in an:
            continue
        # determine primary cpc
        primary = None
        cpc_field = rec.get('cpc')
        if cpc_field:
            try:
                cpcs = json.loads(cpc_field)
            except:
                cpcs = []
            if isinstance(cpcs, list):
                for it in cpcs:
                    if isinstance(it, dict) and it.get('first'):
                        primary = it.get('code')
                        break
                if not primary and len(cpcs)>0 and isinstance(cpcs[0], dict):
                    primary = cpcs[0].get('code')
        if an not in assignee_to_codes:
            assignee_to_codes[an] = set()
        if primary:
            assignee_to_codes[an].add(primary)
            all_codes.add(primary)

# prepare result
res = {
    'univ_pubnums_count': len(univ_pubnums),
    'univ_pubnums_sample': list(sorted(list(univ_pubnums)))[:20],
    'assignees': {k: sorted(list(v)) for k,v in assignee_to_codes.items()},
    'codes': sorted(list(all_codes))
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_5I4DtjpcM4Fv7fjmRPlhswNj': 'file_storage/call_5I4DtjpcM4Fv7fjmRPlhswNj.json', 'var_call_3VyetCwrZExI2Xpet9Um2Z3I': 'file_storage/call_3VyetCwrZExI2Xpet9Um2Z3I.json', 'var_call_aQiaaKewuvuNUgNV4DvyEt09': {'pairs': [], 'codes': []}, 'var_call_dEoQDTzU3g8MBJxJTTtcYTmC': 'file_storage/call_dEoQDTzU3g8MBJxJTTtcYTmC.json', 'var_call_nxN5eBvJXYwbAZgZ0FnUqKrV': [], 'var_call_Lb2aFYNCzIUGMiHjFYMERzCW': 'file_storage/call_Lb2aFYNCzIUGMiHjFYMERzCW.json', 'var_call_ejIAYQLOHqeJ95QlU8d5FeRT': {'univ_pubnums': [], 'assignees': {}, 'codes': []}, 'var_call_t4S4NSfolHw3HxJaXMVQ6zn0': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'The EP patent filing (app. number EP-21763795-A) is owned by THE REGENTS OF UNIV OF CALIFORNIA and has publication number EP-4114888-A1.', 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.'], 'var_call_Igfcem8S67QyNMRoogvuC7Hx': ['US-11081687-B2', 'US-10794458-B2', 'US-11124615-B2', 'US-10610606-B2', 'US-10957507-B2', 'US-10933114-B2', 'US-11169125-B2', 'US-10695419-B2', 'US-10950222-B2', 'US-11168653-B2', 'US-10853219-B2', 'US-11136369-B2', 'US-11076136-B2', 'US-10898606-B2', 'US-11182846-B2', 'US-11130385-B2', 'US-10720793-B2', 'US-11141094-B2', 'US-10918785-B2', 'US-11601114-B2', 'US-10924243-B2', 'US-11018783-B2', 'US-11072514-B2', 'US-10859440-B2', 'US-10875306-B2', 'US-10692314-B2', 'US-10904976-B2', 'US-10704655-B2', 'US-10897184-B2', 'US-10826200-B2', 'US-11128943-B2', 'US-10809655-B2', 'US-11273226-B2', 'US-11024606-B2', 'US-11231876-B2', 'US-11126940-B2', 'US-11911287-B2', 'US-10868205-B2', 'US-11082077-B2', 'US-11202094-B2', 'US-11025166-B2', 'US-10974840-B2', 'US-11032098-B2', 'US-11713774-B2', 'US-11307152-B2', 'US-11371080-B2', 'US-11478419-B2', 'US-11137932-B2', 'US-11813423-B2', 'US-10868012-B2'], 'var_call_zKZnqCokJgv0xKzGi1atG7xH': {'univ_pubnums': ['US-201916400501-A', 'US-201917255566-A', 'US-202017075052-A', 'US-202117198827-A'], 'assignees': {}, 'codes': []}, 'var_call_e2fEOEju9owEpr8d19Prk6Nj': 'file_storage/call_e2fEOEju9owEpr8d19Prk6Nj.json'}

exec(code, env_args)
