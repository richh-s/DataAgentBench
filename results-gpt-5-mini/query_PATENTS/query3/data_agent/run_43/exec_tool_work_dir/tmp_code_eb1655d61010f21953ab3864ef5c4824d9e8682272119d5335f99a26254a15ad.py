code = """import json, re
path = var_call_E1sMXDo1vEG9H9KEBrJuUZmc
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Helper to extract publication numbers from Patents_info
pubnum_patterns = [
    re.compile(r'pub\.?\s*number\s*([A-Z]{2}-[0-9A-Z\-]+)', re.IGNORECASE),
    re.compile(r'publication number\s*([A-Z]{2}-[0-9A-Z\-]+)', re.IGNORECASE),
    re.compile(r'publication number\s*([A-Z]{2}[0-9]{5,}[A-Z0-9\-]*)', re.IGNORECASE),
    re.compile(r'\b([A-Z]{2}-[0-9]{4,}[A-Z0-9\-]*)\b'),
    re.compile(r'\b([A-Z]{2}-[0-9]{2,}-[A-Z0-9]+)\b')
]
# Helper to parse assignee from Patents_info using heuristics
def parse_assignee(text):
    if not text or not text.strip():
        return None
    t = text.strip()
    # check 'assigned to' or 'is assigned to' or 'is owned by' patterns
    m = re.search(r'assigned to\s+([A-Z0-9 \.,&\-()]+?)(?:\s+and\b|\s+has\b|\s+with\b|\.|,|$)', t, re.IGNORECASE)
    if m:
        return m.group(1).strip().upper()
    m = re.search(r'owned by\s+([A-Z0-9 \.,&\-()]+?)(?:\s+and\b|\s+has\b|\s+with\b|\.|,|$)', t, re.IGNORECASE)
    if m:
        return m.group(1).strip().upper()
    m = re.search(r'holds the\b', t, re.IGNORECASE)
    if m:
        # take text before 'holds the'
        pre = t[:m.start()].strip()
        return pre.upper()
    m = re.search(r'^([A-Z0-9 &,\.\-()]{3,}?)\s+has\b', t)
    if m:
        return m.group(1).strip().upper()
    # otherwise take leading uppercase sequence
    m = re.match(r'^([A-Z0-9& ,\.\-()]{3,}?)\b(?:\s|,|\.)', t)
    if m:
        return m.group(1).strip().upper()
    return t.upper()

# Build mapping pubnum -> assignee
pub_to_assignee = {}
for rec in records:
    pi = rec.get('Patents_info') or ''
    assignee = parse_assignee(pi) or ''
    # find pub numbers in pi using patterns
    found = set()
    for p in pubnum_patterns:
        for m in p.findall(pi):
            if isinstance(m, tuple):
                num = m[0]
            else:
                num = m
            num = num.strip()
            if len(num) > 3:
                found.add(num)
    # also check for patterns like US-11466906-B2 in citations etc
    for num in found:
        pub_to_assignee[num] = assignee

# Now find citing records that cite any pubnum assigned to UNIV CALIFORNIA
uc_names = ['UNIV CALIFORNIA', 'UNIVERSITY OF CALIFORNIA']

citing_records = []
for rec in records:
    cit = rec.get('citation') or ''
    try:
        cit_list = json.loads(cit) if cit.strip().startswith('[') else []
    except Exception:
        cit_list = []
    cites_uc = False
    for item in cit_list:
        pubnum = item.get('publication_number','')
        if not pubnum:
            continue
        # normalize
        pubnum = pubnum.strip()
        if pubnum in pub_to_assignee and any(u in (pub_to_assignee[pubnum] or '') for u in uc_names):
            cites_uc = True
            break
    if cites_uc:
        citing_records.append(rec)

# For each citing record, get assignee and primary cpc codes
results = {}
for rec in citing_records:
    assignee = parse_assignee(rec.get('Patents_info') or '') or ''
    if any(u in assignee for u in uc_names):
        continue
    # parse cpc json
    cpc_field = rec.get('cpc') or ''
    primary_codes = []
    try:
        cpc_list = json.loads(cpc_field) if cpc_field.strip().startswith('[') else []
    except Exception:
        cpc_list = []
    for c in cpc_list:
        if isinstance(c, dict) and c.get('first'):
            code = c.get('code')
            if code:
                primary_codes.append(code)
    if not primary_codes:
        # fallback: take first code if exists
        if cpc_list and isinstance(cpc_list, list) and isinstance(cpc_list[0], dict) and cpc_list[0].get('code'):
            primary_codes.append(cpc_list[0].get('code'))
    if not primary_codes:
        continue
    results.setdefault(assignee, set()).update(primary_codes)

# Convert sets to sorted lists
out = {k: sorted(list(v)) for k, v in results.items()}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_TbqAJZFKU2tYJY3RZLuEn1w5': 'file_storage/call_TbqAJZFKU2tYJY3RZLuEn1w5.json', 'var_call_69At5P7fh0Ou7fb0zFYvoQOh': [], 'var_call_E1sMXDo1vEG9H9KEBrJuUZmc': 'file_storage/call_E1sMXDo1vEG9H9KEBrJuUZmc.json'}

exec(code, env_args)
