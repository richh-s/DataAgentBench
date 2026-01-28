code = """import json, re
# Load full publicationinfo results from storage
path = var_call_TN5wfhKsY8mqFlo2iPnYzJ80
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# helper to extract publication number
pubnum_re = re.compile(r"[A-Z]{2}-\d{4,}[A-Z0-9\-]*")

def extract_pubnum(text):
    if not text:
        return None
    m = pubnum_re.search(text)
    return m.group(0) if m else None

# helper to extract assignee
assignee_re1 = re.compile(r"^(?P<assignee>[A-Z0-9 &\.,'\-()]+?)\s+(?:holds|hold|is owned by|is assigned to|owns|assigned to|owned by|owns the|is the owner|has)\b", re.I)
assignee_re2 = re.compile(r"is owned by\s+(?P<assignee>[^\.]+)", re.I)
assignee_re3 = re.compile(r"is assigned to\s+(?P<assignee>[^\.]+)", re.I)
assignee_re4 = re.compile(r"owned by\s+(?P<assignee>[^\.]+)", re.I)

def extract_assignee(text):
    if not text:
        return None
    text = text.strip()
    m = assignee_re1.search(text)
    if m:
        return m.group('assignee').strip().upper()
    for r in (assignee_re2, assignee_re3, assignee_re4):
        m = r.search(text)
        if m:
            return m.group('assignee').strip().upper()
    # fallback: if starts with 'In ' patterns like 'In US, the application (number ...) is owned by UNIV CALIF...'
    # try to find pattern 'UNIV' or 'UNIVERSITY' in text
    m2 = re.search(r"(UNIV(?:ERSITY)?[^,\.\)]+)", text, re.I)
    if m2:
        return m2.group(1).strip().upper()
    # As final fallback take leading token before first comma or 'holds'
    parts = re.split(r',|\(|\.', text)
    if parts:
        first = parts[0].strip().upper()
        # limit length
        if len(first) <= 80:
            return first
    return None

# Build mapping publication_number -> assignee for all records
pub_to_assignee = {}
records_by_pub = {}
for rec in data:
    info = rec.get('Patents_info') or ''
    pubnum = extract_pubnum(info)
    assignee = extract_assignee(info)
    if pubnum:
        pub_to_assignee[pubnum] = assignee
        records_by_pub[pubnum] = rec

# identify target publication numbers assigned to UNIV CALIFORNIA
target_pubnums = set()
for pubnum, assignee in pub_to_assignee.items():
    if assignee and 'UNIV' in assignee and 'CALIF' in assignee:
        target_pubnums.add(pubnum)
    elif assignee and 'UNIVERSITY' in assignee and 'CALIF' in assignee:
        target_pubnums.add(pubnum)

# Now find citing patents (records whose citation list includes any target pubnum)
assignee_to_codes = {}
unique_codes = set()
for rec in data:
    citation_text = rec.get('citation')
    if not citation_text:
        continue
    try:
        cited = json.loads(citation_text)
    except Exception:
        # try to fix single quotes
        try:
            cited = json.loads(citation_text.replace("'", '"'))
        except Exception:
            cited = []
    cited_pubnums = set()
    for c in cited:
        pn = c.get('publication_number') if isinstance(c, dict) else None
        if pn:
            cited_pubnums.add(pn)
    if not (cited_pubnums & target_pubnums):
        continue
    # this record cites a UNIV CALIFORNIA patent
    assignee = extract_assignee(rec.get('Patents_info') or '') or 'UNKNOWN'
    # parse cpc
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
        # find codes where first==True
        for entry in cpcs:
            if isinstance(entry, dict) and entry.get('first'):
                code = entry.get('code')
                if code:
                    codes.append(code)
        # fallback: if no first==True, take first entry's code
        if not codes and cpcs and isinstance(cpcs[0], dict):
            code = cpcs[0].get('code')
            if code:
                codes.append(code)
    if not codes:
        codes = []
    # add to mapping
    if assignee not in assignee_to_codes:
        assignee_to_codes[assignee] = set()
    for code in codes:
        assignee_to_codes[assignee].add(code)
        unique_codes.add(code)

# Remove UNIV CALIFORNIA itself from assignee list
assignee_to_codes = {a: list(codes) for a, codes in assignee_to_codes.items() if not (a and 'UNIV' in a and 'CALIF' in a or a and 'UNIVERSITY' in a and 'CALIF' in a)}

result = {'assignee_to_codes': assignee_to_codes, 'unique_codes': sorted(list(unique_codes))}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_F5v6lSca8gMqGoulhxsR6sXO': ['publicationinfo'], 'var_call_XecM1LWxftI3Z5Me1UkrrAKm': ['cpc_definition'], 'var_call_MUwagFTKlV8OPZsO1zCTFIqz': 'file_storage/call_MUwagFTKlV8OPZsO1zCTFIqz.json', 'var_call_nYNT9kePHM00LmaGtBNtHH5A': 'file_storage/call_nYNT9kePHM00LmaGtBNtHH5A.json', 'var_call_TN5wfhKsY8mqFlo2iPnYzJ80': 'file_storage/call_TN5wfhKsY8mqFlo2iPnYzJ80.json'}

exec(code, env_args)
