code = """import json, re

# Load data from previous tool results
with open(var_call_rJquDDjrbHBrjKQFxnTtOKA7, 'r') as f:
    pubs = json.load(f)
with open(var_call_QpZ82zBriMpIatbiH6PftoTB, 'r') as f:
    cpc_defs = json.load(f)

# Build CPC symbol to titleFull mapping
cpc_map = {row['symbol']: row.get('titleFull') for row in cpc_defs}

# Helper to extract publication numbers from Patents_info
pubnum_regex = re.compile(r'[A-Z]{2}-\d{4,}[A-Z0-9-]*')

# Build mapping from publication_number -> record (may map multiple numbers)
pubnum_to_record = {}
for rec in pubs:
    pi = rec.get('Patents_info') or ''
    found = pubnum_regex.findall(pi)
    # Also check title_localized if none found
    if not found:
        tl = rec.get('title_localized') or ''
        found = pubnum_regex.findall(tl)
    for num in found:
        pubnum_to_record[num] = rec

# Helper to parse assignee from Patents_info
assignee_regex = re.compile(r'^([A-Z0-9 &,\.\-]{2,}?)(?:\s+holds|\s+has|\s+is|\s+assigned|\s+owns|\s+for\b|\s+filed|\s+of\b|\s+relates|\s+provides)', re.IGNORECASE)

def extract_assignee(patents_info):
    if not patents_info:
        return None
    m = assignee_regex.search(patents_info)
    if m:
        name = m.group(1).strip()
        # normalize spacing
        name = re.sub(r'\s+', ' ', name)
        return name
    # fallback: try uppercase sequence at start
    m2 = re.match(r'^([A-Z][A-Z0-9 &,\.\-]{1,100})', patents_info)
    if m2:
        return m2.group(1).strip()
    return None

# Helper to parse citation JSON string
def parse_citation(citation_str):
    if not citation_str:
        return []
    try:
        cit = json.loads(citation_str)
        if isinstance(cit, list):
            return cit
        return []
    except Exception:
        # try to fix single quotes
        try:
            cit = json.loads(citation_str.replace("'", '"'))
            return cit if isinstance(cit, list) else []
        except Exception:
            return []

# Helper to parse cpc JSON string
def parse_cpc(cpc_str):
    if not cpc_str:
        return []
    try:
        c = json.loads(cpc_str)
        return c if isinstance(c, list) else []
    except Exception:
        try:
            c = json.loads(cpc_str.replace("'", '"'))
            return c if isinstance(c, list) else []
        except Exception:
            return []

# Find all records that are assigned to UNIV CALIFORNIA
uc_pubnums = set()
for rec in pubs:
    pi = rec.get('Patents_info') or ''
    if 'UNIV CALIFORNIA' in pi.upper():
        found = pubnum_regex.findall(pi)
        for num in found:
            uc_pubnums.add(num)

# If none found via pubnum extraction, also try mapping by checking records where Patents_info contains UC and maybe there's no pubnum; use rowid as key? But citations reference publication_number, so must rely on matches.

# Now iterate over all publications to see which cite any UC pubnum
result = {}
for rec in pubs:
    citation_list = parse_citation(rec.get('citation'))
    if not citation_list:
        continue
    # check each cited pub
    cites_uc = False
    titles = set()
    for cited in citation_list:
        cited_num = cited.get('publication_number') if isinstance(cited, dict) else None
        if not cited_num:
            continue
        # normalize
        cited_num = cited_num.strip()
        if cited_num in uc_pubnums:
            # Mark citing assignee
            cites_uc = True
            # get the cited record to find its primary cpc
            cited_rec = pubnum_to_record.get(cited_num)
            if cited_rec:
                cpcs = parse_cpc(cited_rec.get('cpc'))
                primary = None
                for entry in cpcs:
                    if isinstance(entry, dict) and entry.get('first'):
                        primary = entry.get('code')
                        break
                if not primary and cpcs:
                    # fallback to first code
                    first_entry = cpcs[0]
                    if isinstance(first_entry, dict):
                        primary = first_entry.get('code')
                if primary:
                    # Map to titleFull; exact match on symbol
                    title = cpc_map.get(primary)
                    if title:
                        titles.add(title)
                    else:
                        # try simplified: sometimes symbol in cpc_defs uses no slash? Keep code as is
                        titles.add(f"{primary} (title not found)")
    if cites_uc:
        # extract assignee of citing rec
        assignee = extract_assignee(rec.get('Patents_info') or '')
        if not assignee:
            # try title_localized
            assignee = extract_assignee(rec.get('title_localized') or '')
        if assignee:
            if 'UNIV CALIFORNIA' in assignee.upper():
                continue
            if assignee not in result:
                result[assignee] = set()
            for t in titles:
                result[assignee].add(t)

# Convert sets to sorted lists
out = {k: sorted(list(v)) for k, v in result.items()}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_f1NxnOrTtLo7uXalQydsvLVQ': ['publicationinfo'], 'var_call_DBbu160mgEXm8f6FuFEclOtl': ['cpc_definition'], 'var_call_rJquDDjrbHBrjKQFxnTtOKA7': 'file_storage/call_rJquDDjrbHBrjKQFxnTtOKA7.json', 'var_call_QpZ82zBriMpIatbiH6PftoTB': 'file_storage/call_QpZ82zBriMpIatbiH6PftoTB.json'}

exec(code, env_args)
