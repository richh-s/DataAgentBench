code = """import json, re
# Load_files from storage
full_path = var_call_TN5wfhKsY8mqFlo2iPnYzJ80
univ_path = var_call_nYNT9kePHM00LmaGtBNtHH5A
with open(univ_path, 'r', encoding='utf-8') as f:
    univ_records = json.load(f)
with open(full_path, 'r', encoding='utf-8') as f:
    full_records = json.load(f)

# helper normalize publication numbers
def norm(p):
    if not p:
        return None
    return re.sub(r'[^A-Z0-9]', '', p.upper())

# extract pubnums from univ_records: from Patents_info and also check if 'publication_number' in citation? but primary source is Patents_info
pubs = set()
for rec in univ_records:
    info = rec.get('Patents_info') or ''
    # find tokens like XX-123456... or US-123... or patterns like US1234567B2
    for m in re.finditer(r"[A-Z]{2}-[A-Z0-9\-]+", info.upper()):
        pubs.add(norm(m.group(0)))
    # also look for US- or other patterns without dash
    for m in re.finditer(r"(US-?\d{4,}[A-Z0-9\-]*)", info.upper()):
        pubs.add(norm(m.group(1)))
    # also any pattern like [A-Z]{2,}\-?\d{4,}[A-Z0-9\-]*
    for m in re.finditer(r"([A-Z]{2,}\-?\d{4,}[A-Z0-9\-]*)", info.upper()):
        pubs.add(norm(m.group(1)))

# clean empty
pubs = set([p for p in pubs if p])

# Now scan full_records for citations that include these pub nums
assignee_to_codes = {}
unique_codes = set()

def extract_assignee(text):
    if not text:
        return None
    # try common patterns
    m = re.search(r"^([A-Z0-9 &'`.,\-()]+?)\s+(?:HOLDS|HOLD|IS OWNED BY|IS ASSIGNED TO|OWNS|ASSIGNED TO|OWNED BY|IS THE OWNER|HAS)\b", text.upper())
    if m:
        return m.group(1).strip().upper()
    m2 = re.search(r"(UNIV(?:ERSITY)?[^,\.\)]+)", text, re.I)
    if m2:
        return m2.group(1).strip().upper()
    parts = re.split(r',|\(|\.', text)
    if parts:
        first = parts[0].strip().upper()
        return first
    return None

for rec in full_records:
    cit_text = rec.get('citation')
    if not cit_text:
        continue
    try:
        cited = json.loads(cit_text)
    except Exception:
        try:
            cited = json.loads(cit_text.replace("'", '"'))
        except Exception:
            cited = []
    cited_norms = set()
    for c in cited:
        if isinstance(c, dict):
            pn = c.get('publication_number')
            if pn:
                cited_norms.add(norm(pn))
    if not (cited_norms & pubs):
        continue
    # this record cites Univ California
    assignee = extract_assignee(rec.get('Patents_info') or '') or 'UNKNOWN'
    # skip Univ California itself
    if ('UNIV' in assignee and 'CALIF' in assignee) or ('UNIVERSITY' in assignee and 'CALIF' in assignee):
        continue
    # extract primary cpc codes
    codes = []
    cpc_text = rec.get('cpc')
    if cpc_text:
        try:
            cpcs = json.loads(cpc_text)
        except Exception:
            try:
                cpcs = json.loads(cpc_text.replace("'", '"'))
            except Exception:
                cpcs = []
        for e in cpcs:
            if isinstance(e, dict) and e.get('first'):
                code = e.get('code')
                if code:
                    codes.append(code)
        if not codes:
            # fallback first dict code
            for e in cpcs:
                if isinstance(e, dict) and e.get('code'):
                    codes.append(e.get('code'))
                    break
    # record mapping
    if assignee not in assignee_to_codes:
        assignee_to_codes[assignee] = set()
    for c in codes:
        assignee_to_codes[assignee].add(c)
        unique_codes.add(c)

# convert sets to lists and sort
assignee_to_codes = {k: sorted(list(v)) for k, v in assignee_to_codes.items()}
unique_codes = sorted([c for c in unique_codes if c])

out = {'assignee_to_codes': assignee_to_codes, 'unique_codes': unique_codes}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_F5v6lSca8gMqGoulhxsR6sXO': ['publicationinfo'], 'var_call_XecM1LWxftI3Z5Me1UkrrAKm': ['cpc_definition'], 'var_call_MUwagFTKlV8OPZsO1zCTFIqz': 'file_storage/call_MUwagFTKlV8OPZsO1zCTFIqz.json', 'var_call_nYNT9kePHM00LmaGtBNtHH5A': 'file_storage/call_nYNT9kePHM00LmaGtBNtHH5A.json', 'var_call_TN5wfhKsY8mqFlo2iPnYzJ80': 'file_storage/call_TN5wfhKsY8mqFlo2iPnYzJ80.json', 'var_call_36y4q0XKchL2Q3QD6S3FK2Xb': {'assignee_to_codes': {}, 'unique_codes': []}, 'var_call_AbxYEVWaZYETHTlZtHsJuHtE': {'count': 169, 'samples': [{'rowid': '1173', 'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}, {'rowid': '6244', 'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'citation_preview': '[]'}, {'rowid': '6967', 'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2001053519-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",'}, {'rowid': '10358', 'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "ABU-AWWAD, F. M. \\"A QSAR STUDY of the Activity of Some Fluorinated Anesthetics\\" Der Pharma Chemica ('}, {'rowid': '14719', 'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'citation_preview': '[]'}, {'rowid': '17880', 'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "FEBS LETTERS=1976",\n    "publication_number": "",\n    "type": ""\n  },\n  {\n    "application_number": ""'}, {'rowid': '20566', 'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "PRS",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2003032003-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",'}, {'rowid': '21654', 'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'citation_preview': '[]'}, {'rowid': '23096', 'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'citation_preview': '[]'}, {'rowid': '26944', 'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'citation_preview': '[]'}, {'rowid': '29441', 'Patents_info': 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "DE-1509371-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'rowid': '31022', 'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2002182660-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",'}, {'rowid': '31321', 'Patents_info': 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4861760-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}, {'rowid': '31849', 'Patents_info': 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "WO-9622024-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'rowid': '32410', 'Patents_info': 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "WO-9823639-A2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'rowid': '38103', 'Patents_info': 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'citation_preview': '[]'}, {'rowid': '38489', 'Patents_info': 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'citation_preview': '[]'}, {'rowid': '44126', 'Patents_info': 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-3222562-A",\n    "type": "Y"\n  },\n  {\n    "application_number": "",\n  '}, {'rowid': '45431', 'Patents_info': 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.', 'citation_preview': '[]'}, {'rowid': '45586', 'Patents_info': 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.', 'citation_preview': '[]'}]}}

exec(code, env_args)
