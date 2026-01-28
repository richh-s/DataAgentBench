code = """import json, re

# Load the large query results from storage
with open(var_call_BLNKyl7rtSaOD6Sk0NFwqoCO, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_BaySDfSi2nsssDzAodScC4DF, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build CPC symbol -> titleFull mapping
cpc_map = {d.get('symbol'): d.get('titleFull') for d in cpc_defs}

# Helper to extract publication numbers from a free text
pubnum_regex = re.compile(r'\b[A-Z]{2,3}-\d{4,}[A-Z0-9\-]*\b')

def extract_pubnums_from_text(s):
    if not s:
        return []
    return pubnum_regex.findall(s)

# Identify UC-assigned patents by inspecting Patents_info for 'UNIV' and 'CALIF'
uc_pubnums = set()
for r in pubs:
    patinfo = r.get('Patents_info') or ''
    if re.search(r'univ', patinfo, re.I) and re.search(r'calif', patinfo, re.I):
        # extract publication numbers from this row
        pnums = extract_pubnums_from_text(patinfo)
        for p in pnums:
            uc_pubnums.add(p)

# Fallback: also look for 'UNIVERSITY OF CALIFORNIA' exact
for r in pubs:
    patinfo = r.get('Patents_info') or ''
    if 'UNIVERSITY OF CALIFORNIA' in patinfo.upper():
        pnums = extract_pubnums_from_text(patinfo)
        for p in pnums:
            uc_pubnums.add(p)

# Function to extract assignee
assignee_pattern = re.compile(r'^(.*?)\s+(?:holds|is assigned to|assigned to|assigned|has|owns|owned by|owner|for|belong|of)\b', re.I)
assignee_label = re.compile(r'Assignee[:\s]+([^,\.]+)', re.I)

def extract_assignee(patinfo):
    if not patinfo:
        return ''
    m = assignee_pattern.search(patinfo)
    if m:
        name = m.group(1).strip()
        return re.sub(r'\s+', ' ', name)
    m = assignee_label.search(patinfo)
    if m:
        return m.group(1).strip()
    # fallback: take leading chunk of up to 6 words
    tokens = patinfo.split()
    return ' '.join(tokens[:6])

# Now iterate over publications to find those that cite any uc_pubnums
citing_assignee_to_titles = {}
for r in pubs:
    citation_str = r.get('citation') or '[]'
    try:
        citations = json.loads(citation_str)
    except Exception:
        # try to find publication numbers via regex in the citation text
        citations = []
        for p in pubnum_regex.findall(citation_str):
            citations.append({'publication_number': p})
    cites_uc = False
    for c in citations:
        pubnum = (c.get('publication_number') or '').strip()
        if pubnum in uc_pubnums:
            cites_uc = True
            break
    if not cites_uc:
        continue
    # extract assignee of the citing publication
    assignee = extract_assignee(r.get('Patents_info') or '')
    if not assignee:
        continue
    # normalize assignee for UC check
    if re.search(r'univ', assignee, re.I) and re.search(r'calif', assignee, re.I):
        # skip UC itself
        continue
    # parse cpc field and get primary codes (first==True)
    cpc_str = r.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_str)
    except Exception:
        cpcs = []
    primary_codes = [entry.get('code') for entry in cpcs if entry.get('first')]
    # if none marked first, optionally take first entry's code
    if not primary_codes and cpcs:
        if cpcs[0].get('code'):
            primary_codes = [cpcs[0].get('code')]
    # map codes to titleFull
    titles = []
    for code in primary_codes:
        if not code:
            continue
        title = cpc_map.get(code)
        if title:
            titles.append(title)
        else:
            # try to match only class/subclass part (e.g., H01M4/1315 -> H01M4/13?)
            title = cpc_map.get(code.split()[0])
            if title:
                titles.append(title)
    if not titles:
        # mark unknown
        titles = ['(no primary CPC title found)']
    citing_assignee_to_titles.setdefault(assignee, set()).update(titles)

# Convert sets to sorted lists
result = {k: sorted(list(v)) for k,v in citing_assignee_to_titles.items()}

# Print according to required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9b0W6joJVGbRrFUERRe48eCn': ['publicationinfo'], 'var_call_idbpfPTnKQVP3DdiIqxId7TW': ['cpc_definition'], 'var_call_BLNKyl7rtSaOD6Sk0NFwqoCO': 'file_storage/call_BLNKyl7rtSaOD6Sk0NFwqoCO.json', 'var_call_BaySDfSi2nsssDzAodScC4DF': 'file_storage/call_BaySDfSi2nsssDzAodScC4DF.json'}

exec(code, env_args)
