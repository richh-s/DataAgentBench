code = """import json, re

# Load data files from storage variables
with open(var_call_I4hk2pqe9rYk4bmj5JQZTH25, 'r', encoding='utf-8') as f:
    uc_records = json.load(f)
with open(var_call_RW7kbA3pxaFUAPSgP4dmIzLU, 'r', encoding='utf-8') as f:
    other_records = json.load(f)

# Helper to extract publication number from Patents_info
pub_patterns = [r'pub(?:lication)?\.?\s*number[s]?\s*[:]?\s*([A-Z0-9\-]+)',
                r'with\s+pub(?:lication)?\.?\s*number\s*[:]?\s*([A-Z0-9\-]+)',
                r'publication\s+number\s*[:]?\s*([A-Z0-9\-]+)',
                r'pub\.\s*number\s*([A-Z0-9\-]+)']

uc_pubnums = set()
for rec in uc_records:
    text = rec.get('Patents_info','')
    found = None
    for pat in pub_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            found = m.group(1).strip()
            break
    if not found:
        # Fallback: look for pattern like US- or WO- or TW- followed by numbers and optional suffix
        m = re.search(r'([A-Z]{2}-[0-9]{4,}[A-Z0-9\-]*)', text)
        if m:
            found = m.group(1).strip()
    if found:
        uc_pubnums.add(found)

# Process other records to find which cite UC publications
assignee_to_codes = {}
records_found = []
for rec in other_records:
    patinfo = rec.get('Patents_info','')
    cit_str = rec.get('citation','')
    try:
        citations = json.loads(cit_str) if cit_str else []
    except Exception:
        # if it's already a list
        citations = cit_str if isinstance(cit_str, list) else []
    cites_uc = False
    for c in citations:
        pubnum = c.get('publication_number','') if isinstance(c, dict) else ''
        if pubnum and pubnum in uc_pubnums:
            cites_uc = True
            break
    if not cites_uc:
        continue
    # Extract assignee name from Patents_info
    assignee = None
    m = re.match(r'^(.*?)\s+(?:holds|holds the|is assigned to|assigned to|is owned by|owned by|has|owns|holds an|has the)\b', patinfo, re.IGNORECASE)
    if m:
        assignee = m.group(1).strip()
    else:
        # Try splitting by known separators
        for sep in [' holds', ' is assigned to', ' assigned to', ' is owned by', ' owned by', ' has ', ' owns ', ' - ']:
            if sep in patinfo:
                assignee = patinfo.split(sep)[0].strip()
                break
    if not assignee:
        # As last resort, take up to first comma
        assignee = patinfo.split(',')[0].strip()
    # Normalize whitespace
    assignee = re.sub('\s+', ' ', assignee)

    # Extract primary CPC code
    cpc_str = rec.get('cpc','')
    primary_code = None
    try:
        cpc_list = json.loads(cpc_str) if cpc_str else []
    except Exception:
        cpc_list = cpc_str if isinstance(cpc_str, list) else []
    if isinstance(cpc_list, list):
        for entry in cpc_list:
            if isinstance(entry, dict) and entry.get('first'):
                primary_code = entry.get('code')
                break
        if not primary_code and len(cpc_list) > 0:
            # take first code available
            first = cpc_list[0]
            if isinstance(first, dict):
                primary_code = first.get('code')
            else:
                primary_code = first
    # store
    if assignee not in assignee_to_codes:
        assignee_to_codes[assignee] = set()
    if primary_code:
        assignee_to_codes[assignee].add(primary_code)

# Convert sets to sorted lists
assignee_to_codes_list = {k: sorted(list(v)) for k,v in assignee_to_codes.items()}
unique_codes = sorted({code for codes in assignee_to_codes_list.values() for code in codes})

output = {'assignee_to_codes': assignee_to_codes_list, 'codes': unique_codes}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_I4hk2pqe9rYk4bmj5JQZTH25': 'file_storage/call_I4hk2pqe9rYk4bmj5JQZTH25.json', 'var_call_RW7kbA3pxaFUAPSgP4dmIzLU': 'file_storage/call_RW7kbA3pxaFUAPSgP4dmIzLU.json'}

exec(code, env_args)
