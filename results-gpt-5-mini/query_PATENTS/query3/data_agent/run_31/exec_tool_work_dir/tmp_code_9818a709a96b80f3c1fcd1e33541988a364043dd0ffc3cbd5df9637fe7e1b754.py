code = """import json, re
# load full publicationinfo
path = var_call_TN5wfhKsY8mqFlo2iPnYzJ80
with open(path, 'r', encoding='utf-8') as f:
    all_records = json.load(f)

# helpers
def norm_pub(p):
    if not p:
        return None
    return re.sub(r'[^A-Z0-9]', '', p.upper())

assignee_re = re.compile(r"([A-Z0-9 &'`.,\-()]+?)\s+(?:HOLDS|HOLD|IS OWNED BY|IS ASSIGNED TO|OWNS|ASSIGNED TO|OWNED BY|IS THE OWNER|HAS)\b", re.I)

def extract_assignee(text):
    if not text:
        return None
    m = assignee_re.search(text)
    if m:
        return m.group(1).strip().upper()
    # fallback find UNIV or UNIVERSITY phrase
    m2 = re.search(r"(UNIV(?:ERSITY)?[^,\.\)]+)", text, re.I)
    if m2:
        return m2.group(1).strip().upper()
    # otherwise take leading token
    parts = re.split(r',|\(|\.', text)
    if parts:
        first = parts[0].strip().upper()
        if len(first) <= 120:
            return first
    return None

# collect UNIV CALIFORNIA publication numbers
univ_pub_norms = set()
for rec in all_records:
    info = rec.get('Patents_info') or ''
    assignee = extract_assignee(info) or ''
    if 'UNIV' in assignee and 'CALIF' in assignee or 'UNIVERSITY' in assignee and 'CALIF' in assignee:
        # extract publication number from text: look for token like XX-... or US-... or pattern with letters and digits
        m = re.search(r"([A-Z]{2}-[A-Z0-9\-]+)", info)
        if m:
            pub = m.group(1)
            univ_pub_norms.add(norm_pub(pub))
        else:
            # try to find US or other with number and maybe B1 etc
            m2 = re.search(r"(US-?\d{4,}[A-Z0-9\-]*)", info, re.I)
            if m2:
                univ_pub_norms.add(norm_pub(m2.group(1)))
            else:
                # try any sequence like [A-Z]{2,}-\d+
                m3 = re.search(r"([A-Z]{2,}\-?\d{4,}[A-Z0-9\-]*)", info)
                if m3:
                    univ_pub_norms.add(norm_pub(m3.group(1)))

# iterate all records to find citations
assignee_to_codes = {}
unique_codes = set()
for rec in all_records:
    citation_text = rec.get('citation')
    if not citation_text:
        continue
    try:
        cited = json.loads(citation_text)
    except Exception:
        try:
            cited = json.loads(citation_text.replace("'", '"'))
        except Exception:
            cited = []
    cited_pub_norms = set()
    for c in cited:
        if not isinstance(c, dict):
            continue
        pn = c.get('publication_number')
        if pn:
            pn_norm = norm_pub(pn)
            cited_pub_norms.add(pn_norm)
    if not (cited_pub_norms & univ_pub_norms):
        continue
    # this record cites a Univ California publication
    assignee = extract_assignee(rec.get('Patents_info') or '') or 'UNKNOWN'
    # skip Univ California itself
    if ('UNIV' in assignee and 'CALIF' in assignee) or ('UNIVERSITY' in assignee and 'CALIF' in assignee):
        continue
    # parse cpc codes
    cpc_text = rec.get('cpc')
    codes = []
    if cpc_text:
        try:
            cpcs = json.loads(cpc_text)
        except Exception:
            try:
                cpcs = json.loads(cpc_text.replace("'", '"'))
            except Exception:
                cpcs = []
        # get entries where first==True
        for entry in cpcs:
            if isinstance(entry, dict) and entry.get('first'):
                code = entry.get('code')
                if code:
                    codes.append(code)
        if not codes:
            # fallback take first dict code
            for entry in cpcs:
                if isinstance(entry, dict) and entry.get('code'):
                    codes.append(entry.get('code'))
                    break
    if not codes:
        codes = []
    # add to mapping
    assignee_to_codes.setdefault(assignee, set()).update(codes)
    unique_codes.update(codes)

# convert sets to lists
assignee_to_codes = {k: sorted(list(v)) for k, v in assignee_to_codes.items()}
unique_codes = sorted(list(unique_codes))

out = {'assignee_to_codes': assignee_to_codes, 'unique_codes': unique_codes}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_F5v6lSca8gMqGoulhxsR6sXO': ['publicationinfo'], 'var_call_XecM1LWxftI3Z5Me1UkrrAKm': ['cpc_definition'], 'var_call_MUwagFTKlV8OPZsO1zCTFIqz': 'file_storage/call_MUwagFTKlV8OPZsO1zCTFIqz.json', 'var_call_nYNT9kePHM00LmaGtBNtHH5A': 'file_storage/call_nYNT9kePHM00LmaGtBNtHH5A.json', 'var_call_TN5wfhKsY8mqFlo2iPnYzJ80': 'file_storage/call_TN5wfhKsY8mqFlo2iPnYzJ80.json', 'var_call_36y4q0XKchL2Q3QD6S3FK2Xb': {'assignee_to_codes': {}, 'unique_codes': []}, 'var_call_AbxYEVWaZYETHTlZtHsJuHtE': {'count': 169, 'samples': [{'rowid': '1173', 'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}, {'rowid': '6244', 'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation_preview': '[]'}, {'rowid': '6967', 'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2001053519-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",'}, {'rowid': '10358', 'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "ABU-AWWAD, F. M. \\"A QSAR STUDY of the Activity of Some Fluorinated Anesthetics\\" Der Pharma Chemica ('}, {'rowid': '14719', 'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'citation_preview': '[]'}, {'rowid': '17880', 'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "FEBS LETTERS=1976",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": ""'}, {'rowid': '20566', 'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "PRS",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2003032003-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",'}, {'rowid': '21654', 'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'citation_preview': '[]'}, {'rowid': '23096', 'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'citation_preview': '[]'}, {'rowid': '26944', 'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'citation_preview': '[]'}, {'rowid': '29441', 'Patents_info': 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "DE-1509371-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'rowid': '31022', 'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2002182660-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",'}, {'rowid': '31321', 'Patents_info': 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4861760-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}, {'rowid': '31849', 'Patents_info': 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "WO-9622024-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'rowid': '32410', 'Patents_info': 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "WO-9823639-A2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'rowid': '38103', 'Patents_info': 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'citation_preview': '[]'}, {'rowid': '38489', 'Patents_info': 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'citation_preview': '[]'}, {'rowid': '44126', 'Patents_info': 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-3222562-A",\n    "type": "Y"\n  },\n  {\n    "application_number": "",\n  '}, {'rowid': '45431', 'Patents_info': 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.', 'citation_preview': '[]'}, {'rowid': '45586', 'Patents_info': 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.', 'citation_preview': '[]'}]}}

exec(code, env_args)
