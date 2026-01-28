code = """import json, re

# Load data from storage-provided file paths
with open(var_call_l55xEibBEPLvcbgsB4ym2Tu7, 'r') as f:
    uc_records = json.load(f)
with open(var_call_F0XFlqDiYITWL1MBYbrkembO, 'r') as f:
    all_records = json.load(f)
with open(var_call_lRNyp9wRymrVkIyIL4PoXol6, 'r') as f:
    cpc_defs = json.load(f)

# Build CPC definition mapping
cpc_map = {r['symbol']: r.get('titleFull') for r in cpc_defs}

# Helper to extract publication numbers from a text
pubnum_re = re.compile(r"\b[A-Z]{2}-\d{4,}[-A-Z0-9/]*\b")

def extract_pubnums(text):
    if not text:
        return []
    return pubnum_re.findall(text)

# Get UNIV CALIFORNIA publication numbers
uc_pubnums = set()
for rec in uc_records:
    txt = rec.get('Patents_info','')
    nums = extract_pubnums(txt)
    for n in nums:
        uc_pubnums.add(n)

# Also sometimes publication numbers may appear in citation fields of UC records
for rec in uc_records:
    cit = rec.get('citation')
    if cit and cit.strip():
        try:
            cited = json.loads(cit)
            for c in cited:
                pn = c.get('publication_number')
                if pn:
                    uc_pubnums.add(pn)
        except Exception:
            pass

# Function to extract assignee from Patents_info with heuristics
assignee_patterns = [
    re.compile(r'^(?P<assignee>[A-Z0-9 &.,\'"-]+?) holds', re.IGNORECASE),
    re.compile(r'is owned by (?P<assignee>[A-Z0-9 &.,\'"-]+)', re.IGNORECASE),
    re.compile(r'is assigned to (?P<assignee>[A-Z0-9 &.,\'"-]+)', re.IGNORECASE),
    re.compile(r'(?P<assignee>[A-Z0-9 &.,\'"-]+?) holds the', re.IGNORECASE),
    re.compile(r'(?P<assignee>[A-Z0-9 &.,\'"-]+?) has the', re.IGNORECASE),
    re.compile(r'(?P<assignee>[A-Z0-9 &.,\'"-]+?) owns the', re.IGNORECASE),
]

def extract_assignee(text):
    if not text:
        return 'UNKNOWN'
    for pat in assignee_patterns:
        m = pat.search(text)
        if m:
            name = m.group('assignee').strip()
            # cleanup leading commas or 'In US, the application (number...)'
            name = re.sub(r'^In [A-Z]{2}, the application.*?\)\s*', '', name)
            # uppercase the name
            name = name.strip()
            # Remove trailing punctuation
            name = name.strip(' ,.')
            # If name is short like 'In', skip
            if len(name) < 2:
                continue
            return name.upper()
    # fallback: find longest contiguous sequence of uppercase words
    candidates = re.findall(r'([A-Z][A-Z0-9&/\-\. ]{2,})', text)
    if candidates:
        # choose longest
        cand = max(candidates, key=len).strip()
        # cleanup
        cand = re.split(r' holds| has| owns| is ', cand)[0]
        return cand.strip().upper()
    return 'UNKNOWN'

# Now iterate all records to find citing documents
results = {}
for rec in all_records:
    cit = rec.get('citation')
    if not cit or not cit.strip():
        continue
    try:
        cited = json.loads(cit)
    except Exception:
        # try extracting pubnums from citation string
        cited = []
        for pn in extract_pubnums(cit):
            cited.append({'publication_number': pn})
    cited_pubnums = set()
    for c in cited:
        pn = c.get('publication_number') if isinstance(c, dict) else None
        if pn:
            cited_pubnums.add(pn)
    if not cited_pubnums:
        continue
    if uc_pubnums.intersection(cited_pubnums):
        # this record cites a UC patent
        assignee = extract_assignee(rec.get('Patents_info',''))
        if assignee == 'UNIV CALIFORNIA':
            continue
        # parse cpc field
        cpc_field = rec.get('cpc')
        primary_codes = []
        if cpc_field and cpc_field.strip():
            try:
                cpc_list = json.loads(cpc_field)
                for item in cpc_list:
                    if item.get('first'):
                        code = item.get('code')
                        if code and code not in primary_codes:
                            primary_codes.append(code)
                # if none marked first, take first code if available
                if not primary_codes and cpc_list:
                    code = cpc_list[0].get('code')
                    if code:
                        primary_codes.append(code)
            except Exception:
                # fallback: extract codes via regex
                for code in re.findall(r"[A-Z]\w+\d*/\d+", cpc_field):
                    primary_codes.append(code)
        if not primary_codes:
            primary_codes = ['UNKNOWN']
        # map codes to titles
        titles = []
        for code in primary_codes:
            title = cpc_map.get(code)
            if title:
                titles.append(title)
            else:
                # try to find by prefix (e.g., code like F25B21/00 may be stored as F25B21/00)
                # try exact match failed, so try symbol startswith code or vice versa
                found = None
                if code != 'UNKNOWN':
                    for sym, t in cpc_map.items():
                        if sym == code or sym.startswith(code) or code.startswith(sym):
                            found = t
                            break
                if found:
                    titles.append(found)
                else:
                    titles.append(None)
        # store unique titles
        uniq_titles = []
        for t in titles:
            if t not in uniq_titles:
                uniq_titles.append(t)
        results[assignee] = uniq_titles

# Prepare output list
output = []
for assignee, titles in results.items():
    # represent None titles as null
    output.append({'assignee': assignee, 'cpc_titles': titles})

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_6Kreubw6sda70vrL4hVhh4Px': ['publicationinfo'], 'var_call_c23BeMWTAwQXdF8yov9bBp9t': ['cpc_definition'], 'var_call_l55xEibBEPLvcbgsB4ym2Tu7': 'file_storage/call_l55xEibBEPLvcbgsB4ym2Tu7.json', 'var_call_F0XFlqDiYITWL1MBYbrkembO': 'file_storage/call_F0XFlqDiYITWL1MBYbrkembO.json', 'var_call_lRNyp9wRymrVkIyIL4PoXol6': 'file_storage/call_lRNyp9wRymrVkIyIL4PoXol6.json'}

exec(code, env_args)
